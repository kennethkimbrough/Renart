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


def build_model(n_classes: int, pretrained: bool = True, arch: str = "resnet18"):
    torch, _torchvision = _torch()
    from torchvision import models
    if arch == "resnet18":
        weights = models.ResNet18_Weights.IMAGENET1K_V1 if pretrained else None
        model = models.resnet18(weights=weights)
        for name, p in model.named_parameters():
            p.requires_grad = name.startswith(("layer4", "fc"))
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


def predict_probs(model, folder: ImageFolder, batch_size: int = 64, workers: int = 2) -> np.ndarray:
    torch, _ = _torch()
    ds = _FolderDataset(folder, transforms(train=False))
    loader = torch.utils.data.DataLoader(ds, batch_size=batch_size, shuffle=False, num_workers=workers)
    model.eval()
    out = []
    with torch.no_grad():
        for x, _ in loader:
            out.append(torch.softmax(model(x), dim=1).cpu().numpy())
    return np.concatenate(out) if out else np.zeros((0, 0))


def train_cnn(train: ImageFolder, val: ImageFolder, out_dir: Path, epochs: int = 8,
              batch_size: int = 32, lr: float = 3e-4, arch: str = "resnet18",
              pretrained: bool = True, workers: int = 2, seed: int = 0) -> dict:
    """Fine-tune, keep the best validation epoch, return history + val probs."""
    torch, _ = _torch()
    torch.manual_seed(seed)
    np.random.seed(seed)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    model = build_model(len(train.classes), pretrained=pretrained, arch=arch)
    params = [p for p in model.parameters() if p.requires_grad]
    opt = torch.optim.AdamW(params, lr=lr, weight_decay=1e-4)
    sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=max(epochs, 1))
    loss_fn = torch.nn.CrossEntropyLoss(label_smoothing=0.05)

    train_loader = torch.utils.data.DataLoader(
        _FolderDataset(train, transforms(train=True)), batch_size=batch_size,
        shuffle=True, num_workers=workers, drop_last=False)

    history = []
    best_acc, best_state, best_probs = -1.0, None, None
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
        probs = predict_probs(model, val, batch_size=max(batch_size, 64), workers=workers)
        val_acc = float((probs.argmax(1) == val.labels).mean()) if len(val) else float("nan")
        row = {"epoch": epoch + 1, "train_loss": loss_sum / max(total, 1),
               "train_acc": correct / max(total, 1), "val_acc": val_acc,
               "seconds": round(time.time() - t0, 1)}
        history.append(row)
        print(json.dumps(row), flush=True)
        if val_acc > best_acc:
            best_acc, best_probs = val_acc, probs
            best_state = {k: v.detach().clone() for k, v in model.state_dict().items()}

    if best_state is not None:
        model.load_state_dict(best_state)
    torch.save({"state_dict": model.state_dict(), "classes": train.classes, "arch": arch},
               out_dir / "cnn.pt")
    (out_dir / "cnn_history.json").write_text(json.dumps(history, indent=2))
    return {"history": history, "best_val_acc": best_acc, "val_probs": best_probs,
            "model_path": str(out_dir / "cnn.pt")}


def load_cnn(path: Path):
    torch, _ = _torch()
    blob = torch.load(path, map_location="cpu", weights_only=False)
    model = build_model(len(blob["classes"]), pretrained=False, arch=blob.get("arch", "resnet18"))
    model.load_state_dict(blob["state_dict"])
    model.eval()
    return model, blob["classes"]


def predict_image(model, classes: list[str], image_path: Path, top_k: int = 3) -> list[tuple[str, float]]:
    torch, _ = _torch()
    from PIL import Image
    with Image.open(image_path) as img:
        x = transforms(train=False)(img.convert("RGB")).unsqueeze(0)
    with torch.no_grad():
        probs = torch.softmax(model(x), dim=1)[0].numpy()
    order = np.argsort(-probs)[:top_k]
    return [(classes[i], float(probs[i])) for i in order]
