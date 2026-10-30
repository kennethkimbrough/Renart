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

# Painters outside the ten, used only to measure whether the model notices a
# painting is by none of them. Two Baroque painters who learned from the
# Venetians, two Dutch Golden Age painters, and two Impressionists. Any slug
# missing from the dataset is skipped and reported.
OOD_ARTISTS: list[str] = [
    "caravaggio",
    "peter-paul-rubens",
    "rembrandt",
    "johannes-vermeer",
    "claude-monet",
    "vincent-van-gogh",
]

# WikiArt genres dropped from the training subset. Drawings and studies are
# mostly pen or chalk on paper: a model that sees them learns "paper" for the
# painters who left many (Leonardo, Michelangelo), not their brushwork.
EXCLUDED_GENRES: list[str] = ["sketch_and_study"]

IMAGE_SIZE: tuple[int, int] = (224, 224)
HF_DATASET = "huggan/wikiart"

SPLITS = ("train", "val", "test")


def split_for(n: int) -> str:
    """Deterministic split for the n-th kept image of a painter: 70% train, 15% val, 15% test.

    Validation picks the training epoch and the calibration temperature; the
    test split is scored once and reported. Spreading each split through the
    sequence (rather than taking the last 30%) keeps the three alike when the
    dataset shards arrive in a biased order.
    """
    r = n % 20
    if r in (4, 9, 14):
        return "val"
    if r in (2, 12, 17):
        return "test"
    return "train"


@dataclass
class DataConfig:
    root: Path = Path("data/renaissance")
    artists: list[str] = field(default_factory=lambda: list(DEFAULT_ARTISTS))
    max_artists: int = 10
    images_per_artist: int = 150
    exclude_genres: list[str] = field(default_factory=lambda: list(EXCLUDED_GENRES))
    seed: int = 42
    image_size: tuple[int, int] = IMAGE_SIZE

    @property
    def train_dir(self) -> Path:
        return self.root / "train"

    @property
    def val_dir(self) -> Path:
        return self.root / "val"

    @property
    def test_dir(self) -> Path:
        return self.root / "test"

    @property
    def ood_dir(self) -> Path:
        return self.root / "ood"

    @property
    def stats_path(self) -> Path:
        return self.root / "dataset_stats.json"


def smoke_config(root: Path | str = "data/smoke") -> DataConfig:
    """A tiny configuration for exercising the pipeline end to end."""
    return DataConfig(root=Path(root), max_artists=2, images_per_artist=20)


def pretty_name(slug: str) -> str:
    """'leonardo-da-vinci' -> 'Leonardo Da Vinci' (good enough for charts)."""
    return " ".join(part.capitalize() for part in slug.split("-"))
