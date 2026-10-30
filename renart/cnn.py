"""Transfer-learning CNN (ResNet-18 pretrained on ImageNet) for artist attribution.

PyTorch is imported lazily so the rest of the package works without it.
Training on CPU is the expected path: with ~1,500 images at 224x224 and only
the last ResNet stage unfrozen, an epoch takes a few minutes on a GitHub
Actions runner.
"""

from __future__ import annotations

import json
import time
from pathlib import Path

import numpy as np

from .data import ImageFolder

IMAGENET_MEAN = [0.485, 0.456, 0.406]
IMAGENET_STD = [0.229, 0.224, 0.225]


def _torch():
    import torch
    import torchvision
    return torch, torchvision


class _FolderDataset:
    """Minimal torch Dataset over an ImageFolder."""

    def __init__(self, folder: ImageFolder, transform):
        from PIL import Image
        self.folder = folder
        self.transform = transform
        self._open = Image.open

    def __len__(self):
        return len(self.folder)

    def __getitem__(self, i):
        with self._open(self.folder.paths[i]) as img:
            x = self.transform(img.convert("RGB"))
        return x, int(self.folder.labels[i])


def build_model(n_classes: int, pretrained: bool = True, arch: str = "resnet18", unfreeze: int = 1):
    """`unfreeze` is how many of the last ResNet stages train (1 = layer4 only, 2 = layer3 + layer4)."""
    torch, _torchvision = _torch()
    from torchvision import models
    if arch == "resnet18":
        weights = models.ResNet18_Weights.IMAGENET1K_V1 if pretrained else None
        model = models.resnet18(weights=weights)
        stages = tuple(f"layer{i}" for i in range(5 - max(1, min(unfreeze, 4)), 5)) + ("fc",)
        for name, p in model.named_parameters():
            p.requires_grad = name.startswith(stages)
        model.fc = torch.nn.Sequential(torch.nn.Dropout(0.3),
                                       torch.nn.Linear(model.fc.in_features, n_classes))
    elif arch == "efficientnet_b0":
        weights = models.EfficientNet_B0_Weights.IMAGENET1K_V1 if pretrained else None
        model = models.efficientnet_b0(weights=weights)
        for name, p in model.named_parameters():
            p.requires_grad = name.startswith(("features.7", "features.8", "classifier"))
        in_features = model.classifier[1].in_features
        model.classifier = torch.nn.Sequential(torch.nn.Dropout(0.3),
                                               torch.nn.Linear(in_features, n_classes))
    else:
        raise ValueError(f"unknown arch {arch}")
    return model


def transforms(train: bool, size: int = 224):
    _, _torchvision = _torch()
    from torchvision import transforms as T
    norm = T.Normalize(IMAGENET_MEAN, IMAGENET_STD)
    if train:
        return T.Compose([
            T.RandomResizedCrop(size, scale=(0.6, 1.0)),
            T.RandomHorizontalFlip(),
            T.ColorJitter(brightness=0.15, contrast=0.15, saturation=0.1),
            T.ToTensor(), norm,
        ])
    return T.Compose([T.Resize(size), T.CenterCrop(size), T.ToTensor(), norm])


def predict_logits(model, folder: ImageFolder, batch_size: int = 64, workers: int = 2) -> np.ndarray:
    torch, _ = _torch()
    ds = _FolderDataset(folder, transforms(train=False))
    loader = torch.utils.data.DataLoader(ds, batch_size=batch_size, shuffle=False, num_workers=workers)
    model.eval()
    out = []
    with torch.no_grad():
        for x, _ in loader:
            out.append(model(x).cpu().numpy())
    return np.concatenate(out) if out else np.zeros((0, 0))


def predict_probs(model, folder: ImageFolder, batch_size: int = 64, workers: int = 2) -> np.ndarray:
    from .metrics import softmax
    return softmax(predict_logits(model, folder, batch_size=batch_size, workers=workers))


def train_cnn(train: ImageFolder, val: ImageFolder, out_dir: Path, epochs: int = 8,
              batch_size: int = 32, lr: float = 3e-4, arch: str = "resnet18",
              pretrained: bool = True, workers: int = 2, seed: int = 0, unfreeze: int = 1,
              test: ImageFolder | None = None) -> dict:
    """Fine-tune, keep the best validation epoch, return history + val logits (+ test logits)."""
    torch, _ = _torch()
    torch.manual_seed(seed)
    np.random.seed(seed)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    model = build_model(len(train.classes), pretrained=pretrained, arch=arch, unfreeze=unfreeze)
    params = [p for p in model.parameters() if p.requires_grad]
    opt = torch.optim.AdamW(params, lr=lr, weight_decay=1e-4)
    sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=max(epochs, 1))
    loss_fn = torch.nn.CrossEntropyLoss(label_smoothing=0.05)

    train_loader = torch.utils.data.DataLoader(
        _FolderDataset(train, transforms(train=True)), batch_size=batch_size,
        shuffle=True, num_workers=workers, drop_last=False)

    history = []
    best_acc, best_state, best_logits = -1.0, None, None
    for epoch in range(epochs):
        t0 = time.time()
        model.train()
        total, correct, loss_sum = 0, 0, 0.0
        for x, y in train_loader:
            opt.zero_grad()
            logits = model(x)
            loss = loss_fn(logits, y)
            loss.backward()
            opt.step()
            loss_sum += float(loss) * len(y)
            correct += int((logits.argmax(1) == y).sum())
            total += len(y)
        sched.step()
        logits = predict_logits(model, val, batch_size=max(batch_size, 64), workers=workers)
        val_acc = float((logits.argmax(1) == val.labels).mean()) if len(val) else float("nan")
        row = {"epoch": epoch + 1, "train_loss": loss_sum / max(total, 1),
               "train_acc": correct / max(total, 1), "val_acc": val_acc,
               "seconds": round(time.time() - t0, 1)}
        history.append(row)
        print(json.dumps(row), flush=True)
        if val_acc > best_acc:
            best_acc, best_logits = val_acc, logits
            best_state = {k: v.detach().clone() for k, v in model.state_dict().items()}

    if best_state is not None:
        model.load_state_dict(best_state)
    torch.save({"state_dict": model.state_dict(), "classes": train.classes, "arch": arch, "unfreeze": unfreeze},
               out_dir / "cnn.pt")
    (out_dir / "cnn_history.json").write_text(json.dumps(history, indent=2))
    out = {"history": history, "best_val_acc": best_acc, "val_logits": best_logits,
           "model_path": str(out_dir / "cnn.pt"), "test_logits": None}
    if test is not None and len(test):
        out["test_logits"] = predict_logits(model, test, batch_size=max(batch_size, 64), workers=workers)
    return out


def load_cnn(path: Path):
    torch, _ = _torch()
    blob = torch.load(path, map_location="cpu", weights_only=False)
    model = build_model(len(blob["classes"]), pretrained=False, arch=blob.get("arch", "resnet18"),
                        unfreeze=blob.get("unfreeze", 1))
    model.load_state_dict(blob["state_dict"])
    model.eval()
    return model, blob["classes"]


def predict_image(model, classes: list[str], image_path: Path, top_k: int = 3,
                  temperature: float = 1.0) -> list[tuple[str, float]]:
    torch, _ = _torch()
    from PIL import Image

    from .metrics import softmax
    with Image.open(image_path) as img:
        x = transforms(train=False)(img.convert("RGB")).unsqueeze(0)
    with torch.no_grad():
        probs = softmax(model(x).numpy(), temperature)[0]
    order = np.argsort(-probs)[:top_k]
    return [(classes[i], float(probs[i])) for i in order]


def export_onnx(model_path: Path, out_path: Path, opset: int = 17) -> Path:
    """Export the saved CNN to ONNX (input: float32 NCHW, ImageNet-normalised; output: logits).

    The browser demo runs this file with onnxruntime-web, so the preprocessing
    it needs (resize short side to 224, centre crop, ImageNet mean/std) is
    written next to it by `renart_model.json`.
    """
    torch, _ = _torch()
    model, _classes = load_cnn(model_path)
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    dummy = torch.zeros(1, 3, 224, 224)
    kwargs = {"opset_version": opset, "input_names": ["image"], "output_names": ["logits"],
              "dynamic_axes": {"image": {0: "batch"}, "logits": {0: "batch"}}}
    try:
        # Newer torch defaults to the dynamo exporter; the classic one is smaller and runs everywhere.
        torch.onnx.export(model, dummy, str(out_path), dynamo=False, **kwargs)
    except TypeError:  # older torch has no `dynamo` argument
        torch.onnx.export(model, dummy, str(out_path), **kwargs)
    return out_path


def check_onnx(model_path: Path, onnx_path: Path, image_path: Path, atol: float = 1e-3) -> float:
    """Largest absolute difference between torch and onnxruntime logits for one image."""
    import onnxruntime as ort
    from PIL import Image
    torch, _ = _torch()
    model, _classes = load_cnn(model_path)
    with Image.open(image_path) as img:
        x = transforms(train=False)(img.convert("RGB")).unsqueeze(0)
    with torch.no_grad():
        ref = model(x).numpy()
    sess = ort.InferenceSession(str(onnx_path), providers=["CPUExecutionProvider"])
    got = sess.run(["logits"], {"image": x.numpy()})[0]
    diff = float(np.abs(ref - got).max())
    if diff > atol:
        raise RuntimeError(f"ONNX output differs from torch by {diff:.5f} (> {atol})")
    return diff
