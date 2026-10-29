"""Project configuration: artist list, image size and default paths.

Artist names are the slugs used by the `huggan/wikiart` dataset on Hugging Face.
The downloader resolves them against the dataset's own label list at run time
and reports any that are missing, so adding an artist means adding a slug here.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

# Renaissance painters present in huggan/wikiart, in priority order. The
# downloader keeps the first `max_artists` that exist in the dataset.
DEFAULT_ARTISTS: list[str] = [
    "leonardo-da-vinci",
    "raphael",
    "titian",
    "sandro-botticelli",
    "michelangelo",
    "giovanni-bellini",
    "andrea-mantegna",
    "fra-angelico",
    "piero-della-francesca",
    "tintoretto",
    "paolo-veronese",
    "giorgione",
    "albrecht-durer",
    "hieronymus-bosch",
    "pieter-bruegel-the-elder",
    "hans-memling",
    "jan-van-eyck",
    "el-greco",
]

IMAGE_SIZE: tuple[int, int] = (224, 224)
HF_DATASET = "huggan/wikiart"


@dataclass
class DataConfig:
    root: Path = Path("data/renaissance")
    artists: list[str] = field(default_factory=lambda: list(DEFAULT_ARTISTS))
    max_artists: int = 10
    images_per_artist: int = 150
    val_fraction: float = 0.2
    seed: int = 42
    image_size: tuple[int, int] = IMAGE_SIZE

    @property
    def train_dir(self) -> Path:
        return self.root / "train"

    @property
    def val_dir(self) -> Path:
        return self.root / "val"

    @property
    def stats_path(self) -> Path:
        return self.root / "dataset_stats.json"


def smoke_config(root: Path | str = "data/smoke") -> DataConfig:
    """A tiny configuration for exercising the pipeline end to end."""
    return DataConfig(root=Path(root), max_artists=2, images_per_artist=20)


def pretty_name(slug: str) -> str:
    """'leonardo-da-vinci' -> 'Leonardo Da Vinci' (good enough for charts)."""
    return " ".join(part.capitalize() for part in slug.split("-"))
