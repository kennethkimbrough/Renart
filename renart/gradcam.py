"""Grad-CAM heatmaps: which regions of a painting drove the CNN's prediction.

Hooks the last convolutional stage of ResNet-18, weights its activations by
the gradient of the predicted class score, and overlays the result on the
image. Needs torch, so it runs in the training workflow, not in tests.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

from .cnn import load_cnn, transforms
from .data import ImageFolder


def gradcam_map(model, x) -> tuple[np.ndarray, int, float]:
    """Return (heatmap in [0,1] at feature-map resolution, predicted class, prob)."""
    import torch
    feats: list = []
    grads: list = []
    layer = model.layer4 if hasattr(model, "layer4") else model.features[-1]
    h1 = layer.register_forward_hook(lambda m, i, o: feats.append(o))
    h2 = layer.register_full_backward_hook(lambda m, gi, go: grads.append(go[0]))
    model.eval()
    model.zero_grad()
    logits = model(x)
    probs = torch.softmax(logits, dim=1)[0]
    cls = int(probs.argmax())
    logits[0, cls].backward()
    h1.remove()
    h2.remove()
    a = feats[0][0]            # C x h x w
    g = grads[0][0]            # C x h x w
    weights = g.mean(dim=(1, 2))
    cam = torch.relu((weights[:, None, None] * a).sum(0))
    cam = cam / (cam.max() + 1e-8)
    return cam.detach().numpy(), cls, float(probs[cls])


def render_gradcam(model_path: Path, folder: ImageFolder, out_path: Path, n: int = 6, seed: int = 0) -> Path:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from PIL import Image

    model, classes = load_cnn(model_path)
    tf = transforms(train=False)
    rng = np.random.RandomState(seed)
    # One image per class where possible, so the figure shows variety.
    picks: list[int] = []
    for c in range(len(classes)):
        idx = np.flatnonzero(folder.labels == c)
        if len(idx):
            picks.append(int(rng.choice(idx)))
    picks = picks[:n]
    cols = 3
    rows = (len(picks) + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(cols * 3.4, rows * 3.6))
    axes = np.atleast_1d(axes).ravel()
    for ax in axes:
        ax.axis("off")
    for ax, i in zip(axes, picks):
        with Image.open(folder.paths[i]) as img:
            rgb = img.convert("RGB").resize((224, 224))
            x = tf(rgb).unsqueeze(0).requires_grad_(False)
        cam, cls, p = gradcam_map(model, x)
        cam_img = np.asarray(Image.fromarray((cam * 255).astype(np.uint8)).resize((224, 224), Image.BILINEAR)) / 255.0
        ax.imshow(rgb)
        ax.imshow(cam_img, cmap="jet", alpha=0.45)
        truth = classes[int(folder.labels[i])]
        ok = "✓" if cls == int(folder.labels[i]) else "✗"
        ax.set_title(f"{ok} {classes[cls]} ({p:.2f})\ntrue: {truth}", fontsize=8)
    fig.suptitle("Grad-CAM: regions that drove each prediction", fontsize=11)
    fig.tight_layout()
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=130)
    plt.close(fig)
    return out_path
