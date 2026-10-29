"""Build a balanced Renaissance subset of WikiArt as an image folder.

Source: the `huggan/wikiart` dataset on Hugging Face (about 81k paintings,
129 artists). Its `artist` column is an integer class label, so we first read
the label names from the dataset metadata, map the configured artist slugs to
label ids, and then scan the parquet shards reading only the `artist` column.
Image bytes are fetched only for the row groups that contain wanted artists,
which keeps the download far below the full ~30 GB.

Needs `huggingface_hub`, `pyarrow` and `pillow`; `datasets` is optional (it is
used to read the label names when available, with a fallback to the parquet
schema metadata).
"""

from __future__ import annotations

import io
import json
import random
import time
from collections import defaultdict

from PIL import Image

from .config import HF_DATASET, DataConfig
from .data import write_stats


def _artist_names(repo: str, parquet_path: str | None, fs) -> list[str]:
    """Label names for the `artist` column."""
    try:
        from datasets import load_dataset_builder
        builder = load_dataset_builder(repo)
        return list(builder.info.features["artist"].names)
    except Exception as exc:  # noqa: BLE001 - fall through to the parquet metadata
        print(f"  datasets builder unavailable ({exc!r}); reading parquet metadata")
    if parquet_path is None:
        raise RuntimeError("no parquet file to read label names from")
    import pyarrow.parquet as pq
    with fs.open(parquet_path, "rb") as f:
        meta = pq.ParquetFile(f).schema_arrow.metadata or {}
    hf_meta = json.loads(meta.get(b"huggingface", b"{}"))
    names = hf_meta.get("info", {}).get("features", {}).get("artist", {}).get("names")
    if not names:
        raise RuntimeError("could not find artist label names in parquet metadata")
    return list(names)


def _parquet_files(repo: str) -> tuple[list[str], str]:
    from huggingface_hub import HfApi
    api = HfApi()
    for revision in ("main", "refs/convert/parquet"):
        files = [f for f in api.list_repo_files(repo, repo_type="dataset", revision=revision)
                 if f.endswith(".parquet") and "train" in f]
        if files:
            return sorted(files), revision
    raise RuntimeError(f"no parquet shards found in {repo}")


def _decode(cell) -> Image.Image:
    """A parquet image cell is a struct {bytes, path} (or raw bytes)."""
    data = cell["bytes"] if isinstance(cell, dict) else cell
    return Image.open(io.BytesIO(data))


def prepare_image(img: Image.Image, size: tuple[int, int]) -> Image.Image:
    """Resize the short side, then centre-crop, so paintings aren't stretched."""
    img = img.convert("RGB")
    w, h = img.size
    scale = max(size[0] / w, size[1] / h)
    img = img.resize((max(size[0], round(w * scale)), max(size[1], round(h * scale))), Image.LANCZOS)
    w, h = img.size
    left, top = (w - size[0]) // 2, (h - size[1]) // 2
    return img.crop((left, top, left + size[0], top + size[1]))


def download_wikiart(cfg: DataConfig, repo: str = HF_DATASET, max_shards: int | None = None) -> dict:
    """Download the subset described by `cfg`. Returns the stats dict."""
    import pyarrow.parquet as pq
    from huggingface_hub import HfFileSystem

    started = time.time()
    files, revision = _parquet_files(repo)
    fs = HfFileSystem()
    paths = [f"datasets/{repo}@{revision}/{f}" for f in files]
    names = _artist_names(repo, paths[0], fs)
    print(f"{repo}: {len(files)} shards at {revision}, {len(names)} artist labels")

    wanted: dict[int, str] = {}
    missing: list[str] = []
    for slug in cfg.artists:
        if slug in names:
            if len(wanted) < cfg.max_artists:
                wanted[names.index(slug)] = slug
        else:
            missing.append(slug)
    if missing:
        print(f"  not in dataset (skipped): {missing}")
    if len(wanted) < 2:
        raise RuntimeError(f"fewer than 2 configured artists exist in {repo}: {sorted(names)}")
    print(f"  selected artists: {list(wanted.values())}")

    rng = random.Random(cfg.seed)
    rng.shuffle(paths)
    if max_shards:
        paths = paths[:max_shards]

    counts: dict[str, dict[str, int]] = {slug: {"train": 0, "val": 0} for slug in wanted.values()}
    totals: dict[str, int] = defaultdict(int)
    quota = cfg.images_per_artist
    scanned = 0

    def done() -> bool:
        return all(totals[s] >= quota for s in wanted.values())

    for path in paths:
        if done():
            break
        with fs.open(path, "rb") as f:
            pf = pq.ParquetFile(f)
            for rg in range(pf.metadata.num_row_groups):
                if done():
                    break
                labels = pf.read_row_group(rg, columns=["artist"]).column("artist").to_pylist()
                scanned += len(labels)
                hits = [i for i, lab in enumerate(labels)
                        if lab in wanted and totals[wanted[lab]] < quota]
                if not hits:
                    continue
                images = pf.read_row_group(rg, columns=["image"]).column("image")
                for i in hits:
                    slug = wanted[labels[i]]
                    if totals[slug] >= quota:
                        continue
                    try:
                        img = prepare_image(_decode(images[i].as_py()), cfg.image_size)
                    except Exception as exc:  # noqa: BLE001 - skip undecodable rows
                        print(f"  skipping undecodable image ({exc!r})")
                        continue
                    n = totals[slug]
                    split = "val" if (n % 5 == 4) else "train"  # 20% validation, deterministic
                    out_dir = cfg.root / split / slug
                    out_dir.mkdir(parents=True, exist_ok=True)
                    img.save(out_dir / f"wikiart_{n:04d}.jpg", "JPEG", quality=92)
                    totals[slug] += 1
                    counts[slug][split] += 1
        print(f"  scanned {scanned} rows; " +
              ", ".join(f"{s}={totals[s]}" for s in wanted.values()), flush=True)

    # Drop artists that ended up with too few images to evaluate.
    for slug in list(counts):
        if totals[slug] < 10:
            print(f"  dropping {slug}: only {totals[slug]} images")
            del counts[slug]
            for split in ("train", "val"):
                d = cfg.root / split / slug
                if d.exists():
                    for p in d.iterdir():
                        p.unlink()
                    d.rmdir()

    stats_path = write_stats(cfg.root, counts, {
        "source": f"{repo}@{revision}",
        "images_per_artist_cap": quota,
        "rows_scanned": scanned,
        "seconds": round(time.time() - started, 1),
        "image_size": list(cfg.image_size),
        "missing_from_dataset": missing,
    })
    print(f"wrote {stats_path}")
    return json.loads(stats_path.read_text())
