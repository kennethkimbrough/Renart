import numpy as np
import pytest

from renart.features import extract_features, feature_names, rgb_to_hsv
from tests.conftest import synthetic_painting


def test_feature_vector_matches_names():
    vec = extract_features(synthetic_painting("warm", 1))
    assert vec.shape == (len(feature_names()),)
    assert np.isfinite(vec).all()


def test_features_are_deterministic():
    img = synthetic_painting("cool", 3)
    assert np.array_equal(extract_features(img), extract_features(img))


def test_hsv_matches_known_colours():
    rgb = np.array([[[1.0, 0.0, 0.0]], [[0.0, 1.0, 0.0]], [[0.0, 0.0, 1.0]], [[0.5, 0.5, 0.5]]])
    hsv = rgb_to_hsv(rgb)
    np.testing.assert_allclose(hsv[0, 0], [0.0, 1.0, 1.0])
    np.testing.assert_allclose(hsv[1, 0], [1 / 3, 1.0, 1.0])
    np.testing.assert_allclose(hsv[2, 0], [2 / 3, 1.0, 1.0])
    np.testing.assert_allclose(hsv[3, 0], [0.0, 0.0, 0.5])


def test_palette_separates_styles():
    names = feature_names()
    warm = extract_features(synthetic_painting("warm", 5))
    cool = extract_features(synthetic_painting("cool", 5))
    r = names.index("palette_0_r")
    b = names.index("palette_0_b")
    assert warm[r] > warm[b]
    assert cool[b] > cool[r]


def test_orientation_histogram_sees_stroke_direction():
    names = feature_names()
    warm = extract_features(synthetic_painting("warm", 2))  # smooth bands under fine noise
    cool = extract_features(synthetic_painting("cool", 2))  # diagonal strokes
    aniso = names.index("fine_anisotropy")
    assert cool[aniso] > warm[aniso]  # consistent diagonal strokes are more anisotropic than noisy bands


def test_rejects_grayscale():
    with pytest.raises(ValueError):
        extract_features(np.zeros((32, 32), dtype=np.uint8))
