"""Loading an image-folder dataset (`<root>/<split>/<artist>/*.jpg`)."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from PIL import Image

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}


@dataclass
class ImageFolder:
    """Paths and integer labels for one split."""

    paths: list[Path]
    labels: np.ndarray
    classes: list[str]

    def __len__(self) -> int:
        return len(self.paths)


def list_classes(split_dir: Path) -> list[str]:
    return sorted(p.name for p in split_dir.iterdir() if p.is_dir())


def load_split(split_dir: Path, classes: list[str] | None = None) -> ImageFolder:
    """Scan one split directory. `classes` fixes the label order across splits."""
    split_dir = Path(split_dir)
    if not split_dir.is_dir():
        raise FileNotFoundError(f"missing split directory: {split_dir}")
    classes = classes or list_classes(split_dir)
    index = {c: i for i, c in enumerate(classes)}
    paths: list[Path] = []
    labels: list[int] = []
    for cls in classes:
        cls_dir = split_dir / cls
        if not cls_dir.is_dir():
            continue
        for p in sorted(cls_dir.iterdir()):
            if p.suffix.lower() in IMAGE_EXTENSIONS:
                paths.append(p)
                labels.append(index[cls])
    return ImageFolder(paths=paths, labels=np.asarray(labels, dtype=np.int64), classes=classes)


def load_dataset(root: Path) -> tuple[ImageFolder, ImageFolder]:
    """Load train and val splits with a shared class list."""
    root = Path(root)
    classes = list_classes(root / "train")
    train = load_split(root / "train", classes)
    val = load_split(root / "val", classes)
    return train, val


def load_image(path: Path, size: tuple[int, int] | None = None) -> np.ndarray:
    """Read an image as an RGB uint8 array, optionally resized."""
    with Image.open(path) as img:
        img = img.convert("RGB")
        if size is not None and img.size != size:
            img = img.resize(size, Image.LANCZOS)
        return np.asarray(img)


def write_stats(root: Path, counts: dict[str, dict[str, int]], extra: dict | None = None) -> Path:
    """Persist per-artist, per-split counts next to the data."""
    stats = {
        "artists": sorted(counts),
        "counts": counts,
        "total_images": int(sum(sum(v.values()) for v in counts.values())),
    }
    if extra:
        stats.update(extra)
    path = Path(root) / "dataset_stats.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(stats, indent=2))
    return path
