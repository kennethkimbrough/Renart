import json

from renart.data import load_dataset, load_image, write_stats


def test_load_dataset_shares_class_order(synthetic_dataset):
    train, val = load_dataset(synthetic_dataset)
    assert train.classes == val.classes == ["artist-cool", "artist-warm"]
    assert len(train) == 24 and len(val) == 8
    assert sorted(set(train.labels.tolist())) == [0, 1]


def test_load_image_resizes(synthetic_dataset):
    train, _ = load_dataset(synthetic_dataset)
    img = load_image(train.paths[0], (64, 64))
    assert img.shape == (64, 64, 3) and img.dtype.kind == "u"


def test_write_stats(tmp_path):
    path = write_stats(tmp_path, {"a": {"train": 3, "val": 1}}, {"source": "test"})
    stats = json.loads(path.read_text())
    assert stats["total_images"] == 4 and stats["source"] == "test"
