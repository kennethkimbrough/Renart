"""Build a Renaissance subset of WikiArt as an image folder.

Source: the `huggan/wikiart` dataset on Hugging Face (about 81k paintings,
129 artists). Its `artist` and `genre` columns are integer class labels, so we
first read the label names from the dataset metadata, map the configured
slugs to label ids, and then scan the parquet shards reading only those two
columns. Image bytes are fetched only for the row groups that contain wanted
rows, which keeps the download far below the full ~30 GB.

Two subsets are built the same way:

* the main one, `<root>/{train,val,test}/<painter>/`, for the ten painters,
  with drawings and studies filtered out by genre;
* `<root>/ood/<painter>/`, a few painters outside the ten, used only to test
  whether the model can tell that a painting is by none of them.

Needs `huggingface_hub`, `pyarrow` and `pillow`; `datasets` is optional (it is
used to read the label names when available, with a fallback to the parquet
schema metadata).
"""

from __future__ import annotations

import io
import json
import random
import shutil
import time
from collections import defaultdict
from collections.abc import Callable

from PIL import Image

from .config import HF_DATASET, OOD_ARTISTS, SPLITS, DataConfig, split_for
from .data import write_stats


def _label_names(repo: str, column: str, parquet_path: str | None, fs) -> list[str] | None:
    """Label names for a ClassLabel column, or None if the column has none."""
    try:
        from datasets import load_dataset_builder
        feature = load_dataset_builder(repo).info.features.get(column)
        return list(feature.names) if feature is not None and hasattr(feature, "names") else None
    except Exception as exc:  # noqa: BLE001 - fall through to the parquet metadata
        print(f"  datasets builder unavailable ({exc!r}); reading parquet metadata")
    if parquet_path is None:
        raise RuntimeError("no parquet file to read label names from")
    import pyarrow.parquet as pq
    with fs.open(parquet_path, "rb") as f:
        meta = pq.ParquetFile(f).schema_arrow.metadata or {}
    hf_meta = json.loads(meta.get(b"huggingface", b"{}"))
    names = hf_meta.get("info", {}).get("features", {}).get(column, {}).get("names")
    if column == "artist" and not names:
        raise RuntimeError("could not find artist label names in parquet metadata")
    return list(names) if names else None


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


def keep_row(genre_label: int | None, excluded_genre_ids: set[int]) -> bool:
    """Whether a row passes the genre filter (rows with no genre label always pass)."""
    return genre_label is None or genre_label not in excluded_genre_ids


class _Source:
    """The dataset's shard list, label names and filesystem, resolved once."""

    def __init__(self, repo: str, seed: int, max_shards: int | None):
        from huggingface_hub import HfFileSystem
        files, self.revision = _parquet_files(repo)
        self.repo = repo
        self.fs = HfFileSystem()
        self.paths = [f"datasets/{repo}@{self.revision}/{f}" for f in files]
        self.artists = _label_names(repo, "artist", self.paths[0], self.fs)
        self.genres = _label_names(repo, "genre", self.paths[0], self.fs)
        print(f"{repo}: {len(files)} shards at {self.revision}, {len(self.artists)} artist labels, "
              f"{len(self.genres) if self.genres else 'no'} genre labels")
        rng = random.Random(seed)
        rng.shuffle(self.paths)
        if max_shards:
            self.paths = self.paths[:max_shards]

    def resolve(self, slugs: list[str], limit: int | None = None) -> tuple[dict[int, str], list[str]]:
        """Map painter slugs to label ids, in the given order, up to `limit`; also the missing ones."""
        wanted: dict[int, str] = {}
        missing: list[str] = []
        for slug in slugs:
            if slug in self.artists:
                if limit is None or len(wanted) < limit:
                    wanted[self.artists.index(slug)] = slug
            else:
                missing.append(slug)
        if missing:
            print(f"  not in dataset (skipped): {missing}")
        return wanted, missing

    def genre_ids(self, names: list[str]) -> set[int]:
        if not self.genres:
            return set()
        return {self.genres.index(g) for g in names if g in self.genres}

    def scan(self, wanted: dict[int, str], quota: int, excluded_genre_ids: set[int],
             on_image: Callable[[str, int, Image.Image], None]) -> dict:
        """Walk the shards and hand every kept image to `on_image(slug, index, image)`.

        Returns counts: rows scanned, images kept per painter and rows dropped
        by the genre filter per painter.
        """
        import pyarrow.parquet as pq
        totals: dict[str, int] = defaultdict(int)
        dropped: dict[str, int] = defaultdict(int)
        scanned = 0
        columns = ["artist", "genre"] if excluded_genre_ids else ["artist"]

        def done() -> bool:
            return all(totals[s] >= quota for s in wanted.values())

        for path in self.paths:
            if done():
                break
            with self.fs.open(path, "rb") as f:
                pf = pq.ParquetFile(f)
                for rg in range(pf.metadata.num_row_groups):
                    if done():
                        break
                    table = pf.read_row_group(rg, columns=columns)
                    labels = table.column("artist").to_pylist()
                    genres = table.column("genre").to_pylist() if "genre" in columns else [None] * len(labels)
                    scanned += len(labels)
                    hits = []
                    for i, lab in enumerate(labels):
                        if lab not in wanted or totals[wanted[lab]] >= quota:
                            continue
                        if keep_row(genres[i], excluded_genre_ids):
                            hits.append(i)
                        else:
                            dropped[wanted[lab]] += 1
                    if not hits:
                        continue
                    images = pf.read_row_group(rg, columns=["image"]).column("image")
                    for i in hits:
                        slug = wanted[labels[i]]
                        if totals[slug] >= quota:
                            continue
                        try:
                            img = _decode(images[i].as_py())
                        except Exception as exc:  # noqa: BLE001 - skip undecodable rows
                            print(f"  skipping undecodable image ({exc!r})")
                            continue
                        on_image(slug, totals[slug], img)
                        totals[slug] += 1
            print(f"  scanned {scanned} rows; " +
                  ", ".join(f"{s}={totals[s]}" for s in wanted.values()), flush=True)
        return {"scanned": scanned, "totals": dict(totals), "dropped": dict(dropped)}


def _remove(path) -> None:
    if path.exists():
        shutil.rmtree(path)


def download_wikiart(cfg: DataConfig, repo: str = HF_DATASET, max_shards: int | None = None,
                     source: _Source | None = None) -> dict:
    """Download the subset described by `cfg` into train/val/test. Returns the stats dict."""
    started = time.time()
    src = source or _Source(repo, cfg.seed, max_shards)
    wanted, missing = src.resolve(cfg.artists, cfg.max_artists)
    if len(wanted) < 2:
        raise RuntimeError(f"fewer than 2 configured artists exist in {repo}: {sorted(src.artists)}")
    print(f"  selected artists: {list(wanted.values())}")
    excluded = src.genre_ids(cfg.exclude_genres)
    if cfg.exclude_genres and not excluded:
        print(f"  genre filter {cfg.exclude_genres} not applied: no matching genre labels in the dataset")

    counts: dict[str, dict[str, int]] = {slug: {s: 0 for s in SPLITS} for slug in wanted.values()}

    def save(slug: str, n: int, img: Image.Image) -> None:
        split = split_for(n)
        out_dir = cfg.root / split / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        prepare_image(img, cfg.image_size).save(out_dir / f"wikiart_{n:04d}.jpg", "JPEG", quality=92)
        counts[slug][split] += 1

    result = src.scan(wanted, cfg.images_per_artist, excluded, save)

    # Drop artists that ended up with too few images to evaluate.
    for slug in list(counts):
        if sum(counts[slug].values()) < 20:
            print(f"  dropping {slug}: only {sum(counts[slug].values())} images")
            del counts[slug]
            for split in SPLITS:
                _remove(cfg.root / split / slug)

    stats_path = write_stats(cfg.root, counts, {
        "source": f"{repo}@{src.revision}",
        "images_per_artist_cap": cfg.images_per_artist,
        "split": {"train": 0.70, "val": 0.15, "test": 0.15, "rule": "renart.config.split_for"},
        "excluded_genres": cfg.exclude_genres if excluded else [],
        "excluded_counts": {s: result["dropped"].get(s, 0) for s in counts},
        "rows_scanned": result["scanned"],
        "seconds": round(time.time() - started, 1),
        "image_size": list(cfg.image_size),
        "missing_from_dataset": missing,
    })
    print(f"wrote {stats_path}")
    return json.loads(stats_path.read_text())


def download_ood(cfg: DataConfig, artists: list[str] | None = None, per_artist: int = 25,
                 repo: str = HF_DATASET, max_shards: int | None = None, source: _Source | None = None) -> dict:
    """Download a few images each for painters outside the main set, into `<root>/ood/<painter>/`."""
    started = time.time()
    src = source or _Source(repo, cfg.seed, max_shards)
    slugs = artists or OOD_ARTISTS
    wanted, missing = src.resolve(slugs)
    if not wanted:
        raise RuntimeError(f"none of the out-of-set painters exist in {repo}: {slugs}")
    in_set = set(cfg.artists[:cfg.max_artists])
    overlap = [s for s in wanted.values() if s in in_set]
    if overlap:
        raise ValueError(f"out-of-set painters must not be in the main set: {overlap}")
    excluded = src.genre_ids(cfg.exclude_genres)
    counts: dict[str, int] = defaultdict(int)

    def save(slug: str, n: int, img: Image.Image) -> None:
        out_dir = cfg.ood_dir / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        prepare_image(img, cfg.image_size).save(out_dir / f"wikiart_{n:04d}.jpg", "JPEG", quality=92)
        counts[slug] += 1

    result = src.scan(wanted, per_artist, excluded, save)
    stats = {
        "artists": sorted(counts),
        "counts": dict(counts),
        "total_images": int(sum(counts.values())),
        "source": f"{repo}@{src.revision}",
        "per_artist_cap": per_artist,
        "rows_scanned": result["scanned"],
        "seconds": round(time.time() - started, 1),
        "missing_from_dataset": missing,
    }
    cfg.ood_dir.mkdir(parents=True, exist_ok=True)
    path = cfg.ood_dir / "ood_stats.json"
    path.write_text(json.dumps(stats, indent=2))
    print(f"wrote {path}")
    return stats
