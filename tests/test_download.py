from PIL import Image

from renart.config import DEFAULT_ARTISTS, DataConfig, pretty_name, smoke_config
from renart.download import prepare_image


def test_prepare_image_crops_without_stretching():
    img = Image.new("RGB", (400, 200), (10, 20, 30))
    out = prepare_image(img, (224, 224))
    assert out.size == (224, 224)
    tall = prepare_image(Image.new("RGB", (100, 300)), (224, 224))
    assert tall.size == (224, 224)


def test_configs():
    cfg = DataConfig()
    assert cfg.train_dir.name == "train" and cfg.artists == DEFAULT_ARTISTS
    smoke = smoke_config("x")
    assert smoke.max_artists == 2 and smoke.images_per_artist == 20
    assert pretty_name("leonardo-da-vinci") == "Leonardo Da Vinci"
