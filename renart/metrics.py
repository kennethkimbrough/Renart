"""Evaluation helpers shared by the baseline and the CNN."""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score, top_k_accuracy_score


def evaluate_predictions(y_true: np.ndarray, probs: np.ndarray, classes: list[str],
                         model_name: str) -> dict:
    """Accuracy, macro-F1, top-3 accuracy, per-class accuracy and the confusion matrix."""
    y_true = np.asarray(y_true)
    probs = np.asarray(probs)
    y_pred = probs.argmax(axis=1)
    cm = confusion_matrix(y_true, y_pred, labels=list(range(len(classes))))
    per_class = {}
    for i, cls in enumerate(classes):
        n = int(cm[i].sum())
        per_class[cls] = {"support": n, "accuracy": float(cm[i, i] / n) if n else None}
    result = {
        "model": model_name,
        "n_eval": len(y_true),
        "n_classes": len(classes),
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "macro_f1": float(f1_score(y_true, y_pred, average="macro", labels=list(range(len(classes))),
                                   zero_division=0)),
        "chance_accuracy": float(1.0 / len(classes)),
        "per_class": per_class,
        "confusion_matrix": cm.tolist(),
        "classes": list(classes),
    }
    if len(classes) > 3:
        result["top3_accuracy"] = float(
            top_k_accuracy_score(y_true, probs, k=3, labels=list(range(len(classes)))))
    return result


def save_confusion_matrix(cm: list[list[int]] | np.ndarray, classes: list[str], path: Path,
                          title: str) -> Path:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    cm = np.asarray(cm)
    row_sums = cm.sum(axis=1, keepdims=True)
    norm = np.divide(cm, np.maximum(row_sums, 1))
    fig, ax = plt.subplots(figsize=(1.0 + 0.7 * len(classes), 0.8 + 0.6 * len(classes)))
    ax.imshow(norm, cmap="Blues", vmin=0, vmax=1)
    ax.set_xticks(range(len(classes)))
    ax.set_yticks(range(len(classes)))
    ax.set_xticklabels(classes, rotation=45, ha="right", fontsize=8)
    ax.set_yticklabels(classes, fontsize=8)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("True")
    ax.set_title(title)
    for i in range(len(classes)):
        for j in range(len(classes)):
            if cm[i, j]:
                ax.text(j, i, str(cm[i, j]), ha="center", va="center", fontsize=7,
                        color="white" if norm[i, j] > 0.5 else "black")
    fig.tight_layout()
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


def write_json(data: dict, path: Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2))
    return path


def markdown_table(results: list[dict]) -> str:
    """A README-ready comparison table."""
    lines = ["| Model | Accuracy | Macro F1 | Top-3 | Chance |", "|---|---|---|---|---|"]
    for r in results:
        top3 = f"{r['top3_accuracy']:.3f}" if "top3_accuracy" in r else "n/a"
        lines.append(f"| {r['model']} | {r['accuracy']:.3f} | {r['macro_f1']:.3f} | {top3} | "
                     f"{r['chance_accuracy']:.3f} |")
    return "\n".join(lines)
