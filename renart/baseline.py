"""Classical baseline: hand-crafted features -> scaler -> logistic regression.

A random forest can be swapped in with `--classifier forest`. This runs on a
laptop CPU in seconds for ~1,500 images and gives the CNN a floor to beat.
"""

from __future__ import annotations

import pickle
from pathlib import Path

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from .data import ImageFolder, load_image
from .features import extract_features


def featurise(folder: ImageFolder, size: tuple[int, int], log_every: int = 200) -> np.ndarray:
    rows = []
    for i, p in enumerate(folder.paths):
        rows.append(extract_features(load_image(p, size)))
        if log_every and (i + 1) % log_every == 0:
            print(f"  features: {i + 1}/{len(folder.paths)}", flush=True)
    return np.vstack(rows) if rows else np.zeros((0, 0), dtype=np.float32)


def make_classifier(kind: str = "logreg", seed: int = 0) -> Pipeline:
    if kind == "logreg":
        clf = LogisticRegression(max_iter=3000, C=0.5, random_state=seed)
    elif kind == "forest":
        clf = RandomForestClassifier(n_estimators=400, random_state=seed, n_jobs=-1)
    else:
        raise ValueError(f"unknown classifier: {kind}")
    return Pipeline([("scale", StandardScaler()), ("clf", clf)])


def train_baseline(x_train: np.ndarray, y_train: np.ndarray, kind: str = "logreg",
                   seed: int = 0) -> Pipeline:
    model = make_classifier(kind, seed)
    model.fit(x_train, y_train)
    return model


def save_model(model: Pipeline, classes: list[str], path: Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "wb") as f:
        pickle.dump({"model": model, "classes": classes}, f)
    return path


def load_model(path: Path) -> tuple[Pipeline, list[str]]:
    with open(path, "rb") as f:
        blob = pickle.load(f)
    return blob["model"], blob["classes"]
