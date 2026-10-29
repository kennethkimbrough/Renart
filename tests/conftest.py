"""Synthetic image fixtures: two 'artists' with distinguishable palettes and textures."""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pytest
from PIL import Image

SIZE = (224, 224)


def synthetic_painting(style: str, seed: int, size: tuple[int, int] = SIZE) -> np.ndarray:
    """Style 'warm' = reddish, smooth horizontal bands; 'cool' = bluish, noisy diagonal strokes."""
    rng = np.random.RandomState(seed)
    h, w = size[1], size[0]
    yy, xx = np.mgrid[0:h, 0:w]
    if style == "warm":
        base = np.stack([
            180 + 40 * np.sin(yy / 15.0 + seed),
            90 + 30 * np.sin(yy / 23.0),
            60 + 20 * np.cos(yy / 31.0),
        ], axis=-1)
        noise = rng.normal(0, 4, (h, w, 3))
    else:
        diag = np.sin((xx + yy) / 6.0 + seed) * 35
        base = np.stack([
            60 + diag,
            90 + diag,
            170 + diag,
        ], axis=-1)
        noise = rng.normal(0, 18, (h, w, 3))
    return np.clip(base + noise, 0, 255).astype(np.uint8)


@pytest.fixture
def synthetic_dataset(tmp_path: Path) -> Path:
    """An image folder with train/val splits for two synthetic artists."""
    root = tmp_path / "data"
    for style in ("warm", "cool"):
        for split, n in (("train", 12), ("val", 4)):
            d = root / split / f"artist-{style}"
            d.mkdir(parents=True)
            offset = 0 if split == "train" else 100
            for i in range(n):
                Image.fromarray(synthetic_painting(style, seed=offset + i)).save(d / f"img_{i:03d}.jpg")
    return root
