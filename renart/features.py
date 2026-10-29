"""Hand-crafted image features for the classical baseline.

Two families, both computed on a 224x224 RGB array:

* colour: per-channel RGB histograms, HSV statistics, a hue histogram, and a
  dominant-colour palette found by k-means (the idea from the old
  `coloranalysis.r`, with the palette sorted by cluster weight so the vector
  is stable);
* texture / stroke: Sobel-gradient statistics at two scales, a
  magnitude-weighted edge-orientation histogram (a crude "which way do the
  strokes run" signal), orientation anisotropy and entropy, a curvature proxy
  from the change in gradient direction along edges, and a Laplacian sharpness
  measure. These replace the stroke-dynamics ideas from `paintstroke.r`, which
  only worked on synthetic vector strokes, with measures that apply to a
  photograph of a painting.

Everything here is deterministic for a given input.
"""

from __future__ import annotations

import numpy as np
from scipy import ndimage
from sklearn.cluster import KMeans

RGB_BINS = 8
HUE_BINS = 12
ORIENTATION_BINS = 8
PALETTE_SIZE = 5


def rgb_to_hsv(rgb: np.ndarray) -> np.ndarray:
    """Vectorised RGB (0..1) -> HSV (h in 0..1, s, v in 0..1)."""
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    maxc = rgb.max(axis=-1)
    minc = rgb.min(axis=-1)
    v = maxc
    delta = maxc - minc
    s = np.where(maxc > 0, delta / np.maximum(maxc, 1e-12), 0.0)
    safe_delta = np.where(delta > 0, delta, 1.0)
    h = np.zeros_like(maxc)
    is_r = (maxc == r) & (delta > 0)
    is_g = (maxc == g) & (delta > 0) & ~is_r
    is_b = (delta > 0) & ~is_r & ~is_g
    h = np.where(is_r, ((g - b) / safe_delta) % 6, h)
    h = np.where(is_g, (b - r) / safe_delta + 2, h)
    h = np.where(is_b, (r - g) / safe_delta + 4, h)
    h = h / 6.0
    return np.stack([h, s, v], axis=-1)


def colour_features(image: np.ndarray) -> np.ndarray:
    rgb = image.astype(np.float64) / 255.0
    pixels = rgb.reshape(-1, 3)

    hist_parts = []
    for c in range(3):
        hist, _ = np.histogram(pixels[:, c], bins=RGB_BINS, range=(0.0, 1.0))
        hist_parts.append(hist / pixels.shape[0])
    rgb_hist = np.concatenate(hist_parts)

    hsv = rgb_to_hsv(rgb).reshape(-1, 3)
    h, s, v = hsv[:, 0], hsv[:, 1], hsv[:, 2]
    # Circular hue statistics, weighted by saturation so grey pixels don't vote.
    angles = h * 2 * np.pi
    weights = s + 1e-6
    mean_vec = np.array([np.average(np.cos(angles), weights=weights),
                         np.average(np.sin(angles), weights=weights)])
    hue_concentration = float(np.linalg.norm(mean_vec))
    hue_hist, _ = np.histogram(h, bins=HUE_BINS, range=(0.0, 1.0), weights=weights)
    hue_hist = hue_hist / max(hue_hist.sum(), 1e-12)
    hsv_stats = np.array([
        mean_vec[0], mean_vec[1], hue_concentration,
        s.mean(), s.std(), v.mean(), v.std(),
        np.percentile(v, 10), np.percentile(v, 90),
        float((s < 0.15).mean()),  # fraction of near-grey pixels
    ])

    # Dominant palette: k-means on a fixed subsample, sorted by cluster weight.
    rng = np.random.RandomState(0)
    sample = pixels[rng.choice(pixels.shape[0], size=min(2000, pixels.shape[0]), replace=False)]
    km = KMeans(n_clusters=PALETTE_SIZE, n_init=3, random_state=0).fit(sample)
    counts = np.bincount(km.labels_, minlength=PALETTE_SIZE) / sample.shape[0]
    order = np.argsort(-counts)
    palette = km.cluster_centers_[order].ravel()
    palette_weights = counts[order]
    # Palette spread: mean pairwise distance between dominant colours.
    centers = km.cluster_centers_
    diffs = centers[:, None, :] - centers[None, :, :]
    spread = float(np.sqrt((diffs ** 2).sum(-1)).mean())

    return np.concatenate([rgb_hist, hue_hist, hsv_stats, palette, palette_weights, [spread]])


def _gradient_stats(gray: np.ndarray) -> np.ndarray:
    gx = ndimage.sobel(gray, axis=1)
    gy = ndimage.sobel(gray, axis=0)
    mag = np.hypot(gx, gy)
    theta = np.arctan2(gy, gx) % np.pi  # orientation is sign-free

    orient_hist, _ = np.histogram(theta, bins=ORIENTATION_BINS, range=(0.0, np.pi), weights=mag)
    orient_hist = orient_hist / max(orient_hist.sum(), 1e-12)
    probs = orient_hist[orient_hist > 0]
    entropy = float(-(probs * np.log(probs)).sum())
    # Anisotropy: length of the doubled-angle mean vector (1 = all one direction).
    doubled = 2 * theta
    aniso = float(np.hypot(np.average(np.cos(doubled), weights=mag + 1e-9),
                           np.average(np.sin(doubled), weights=mag + 1e-9)))

    # Curvature proxy: how fast the orientation changes along strong edges.
    strong = mag > np.percentile(mag, 80)
    dtheta_x = np.abs(np.diff(theta, axis=1))
    dtheta_x = np.minimum(dtheta_x, np.pi - dtheta_x)
    curvature = float(dtheta_x[strong[:, 1:] & strong[:, :-1]].mean()) if strong.sum() > 2 else 0.0

    lap = ndimage.laplace(gray)
    edge_density = float(strong.mean())
    return np.concatenate([
        orient_hist,
        [mag.mean(), mag.std(), np.percentile(mag, 90), entropy, aniso, curvature,
         lap.var(), edge_density],
    ])


def texture_features(image: np.ndarray) -> np.ndarray:
    gray = image.astype(np.float64).mean(axis=-1) / 255.0
    fine = _gradient_stats(gray)
    coarse = _gradient_stats(ndimage.zoom(gray, 0.5, order=1))
    # Local contrast: std of 8x8 block means vs mean of block stds.
    h, w = gray.shape
    blocks = gray[: h - h % 8, : w - w % 8].reshape(h // 8, 8, w // 8, 8)
    block_means = blocks.mean(axis=(1, 3))
    block_stds = blocks.std(axis=(1, 3))
    local = np.array([block_means.std(), block_stds.mean(), block_stds.std()])
    return np.concatenate([fine, coarse, local])


def extract_features(image: np.ndarray) -> np.ndarray:
    """Full feature vector for one RGB uint8 image."""
    if image.ndim != 3 or image.shape[-1] != 3:
        raise ValueError(f"expected an HxWx3 image, got shape {image.shape}")
    return np.concatenate([colour_features(image), texture_features(image)]).astype(np.float32)


def feature_names() -> list[str]:
    names: list[str] = []
    names += [f"rgb_hist_{c}_{i}" for c in "rgb" for i in range(RGB_BINS)]
    names += [f"hue_hist_{i}" for i in range(HUE_BINS)]
    names += ["hue_cos", "hue_sin", "hue_concentration", "sat_mean", "sat_std",
              "val_mean", "val_std", "val_p10", "val_p90", "grey_fraction"]
    names += [f"palette_{k}_{c}" for k in range(PALETTE_SIZE) for c in "rgb"]
    names += [f"palette_weight_{k}" for k in range(PALETTE_SIZE)]
    names += ["palette_spread"]
    for scale in ("fine", "coarse"):
        names += [f"{scale}_orient_{i}" for i in range(ORIENTATION_BINS)]
        names += [f"{scale}_{n}" for n in ("grad_mean", "grad_std", "grad_p90", "orient_entropy",
                                            "anisotropy", "curvature", "laplacian_var", "edge_density")]
    names += ["block_mean_std", "block_std_mean", "block_std_std"]
    return names
