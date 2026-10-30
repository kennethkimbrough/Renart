"""Evaluation helpers shared by the baseline and the CNN."""

from __future__ import annotations

import json
from itertools import pairwise
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


def softmax(logits: np.ndarray, temperature: float = 1.0) -> np.ndarray:
    z = np.asarray(logits, dtype=np.float64) / float(temperature)
    z = z - z.max(axis=1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=1, keepdims=True)


def nll(logits: np.ndarray, y_true: np.ndarray, temperature: float = 1.0) -> float:
    p = softmax(logits, temperature)
    return float(-np.log(np.clip(p[np.arange(len(y_true)), y_true], 1e-12, None)).mean())


def fit_temperature(logits: np.ndarray, y_true: np.ndarray) -> float:
    """Temperature scaling (Guo et al. 2017): one scalar that minimises validation NLL.

    It does not change the ranking, only how confident the probabilities are,
    so accuracy is untouched while the confidence becomes meaningful. Fitted
    on the validation split, applied to the test split and the browser demo.
    """
    from scipy.optimize import minimize_scalar
    y_true = np.asarray(y_true)
    if len(y_true) == 0:
        return 1.0
    res = minimize_scalar(lambda t: nll(logits, y_true, t), bounds=(0.05, 20.0), method="bounded")
    return float(res.x)


def expected_calibration_error(probs: np.ndarray, y_true: np.ndarray, bins: int = 15) -> dict:
    """ECE over equal-width confidence bins, plus the bins for a reliability diagram."""
    probs = np.asarray(probs)
    y_true = np.asarray(y_true)
    conf = probs.max(axis=1)
    correct = (probs.argmax(axis=1) == y_true).astype(float)
    edges = np.linspace(0.0, 1.0, bins + 1)
    ece = 0.0
    rows = []
    for lo, hi in pairwise(edges):
        mask = (conf > lo) & (conf <= hi) if lo > 0 else (conf >= lo) & (conf <= hi)
        n = int(mask.sum())
        if n == 0:
            continue
        acc, avg_conf = float(correct[mask].mean()), float(conf[mask].mean())
        ece += n / len(conf) * abs(acc - avg_conf)
        rows.append({"lo": round(float(lo), 4), "hi": round(float(hi), 4), "n": n,
                     "accuracy": round(acc, 4), "confidence": round(avg_conf, 4)})
    return {"ece": round(float(ece), 4), "bins": rows, "mean_confidence": round(float(conf.mean()), 4),
            "accuracy": round(float(correct.mean()), 4)}


def ood_report(in_scores: np.ndarray, out_scores: dict[str, np.ndarray], keep_rate: float = 0.95) -> dict:
    """How well a confidence score separates the ten painters' paintings from everyone else's.

    `in_scores` are the maximum calibrated probabilities on the test split;
    `out_scores` the same for each out-of-set painter. The threshold is set so
    `keep_rate` of in-set test paintings are kept, then the report says what
    share of each outsider's paintings would be turned away at that threshold.
    """
    from sklearn.metrics import roc_auc_score
    in_scores = np.asarray(in_scores, dtype=np.float64)
    all_out = np.concatenate([np.asarray(v, dtype=np.float64) for v in out_scores.values()]) \
        if out_scores else np.zeros(0)
    threshold = float(np.quantile(in_scores, 1.0 - keep_rate)) if len(in_scores) else 0.0
    per = {}
    for name, s in out_scores.items():
        s = np.asarray(s, dtype=np.float64)
        y = np.concatenate([np.ones(len(in_scores)), np.zeros(len(s))])
        x = np.concatenate([in_scores, s])
        per[name] = {"n": len(s), "auroc": round(float(roc_auc_score(y, x)), 4) if len(s) else None,
                     "rejected_at_threshold": round(float((s < threshold).mean()), 4) if len(s) else None,
                     "mean_confidence": round(float(s.mean()), 4) if len(s) else None}
    overall = None
    if len(all_out):
        y = np.concatenate([np.ones(len(in_scores)), np.zeros(len(all_out))])
        overall = round(float(roc_auc_score(y, np.concatenate([in_scores, all_out]))), 4)
    return {
        "score": "max calibrated softmax probability",
        "n_in": len(in_scores), "n_out": len(all_out),
        "threshold": round(threshold, 4), "in_set_kept": round(float((in_scores >= threshold).mean()), 4)
        if len(in_scores) else None,
        "in_set_mean_confidence": round(float(in_scores.mean()), 4) if len(in_scores) else None,
        "out_of_set_rejected": round(float((all_out < threshold).mean()), 4) if len(all_out) else None,
        "auroc": overall,
        "per_painter": per,
    }


def save_confidence_histogram(in_scores: np.ndarray, out_scores: dict[str, np.ndarray], threshold: float,
                              path: Path, pretty=lambda s: s) -> Path:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(8, 4))
    bins = np.linspace(0, 1, 21)
    ax.hist(in_scores, bins=bins, density=True, alpha=0.75, color="#b7862f", label="the ten painters (test)")
    all_out = np.concatenate([np.asarray(v) for v in out_scores.values()]) if out_scores else np.zeros(0)
    if len(all_out):
        ax.hist(all_out, bins=bins, density=True, alpha=0.55, color="#6b7a8f",
                label="painters outside the set (" + ", ".join(pretty(k) for k in out_scores) + ")")
    ax.axvline(threshold, color="#b04830", linestyle="--", label=f"abstain below {threshold:.2f}")
    ax.set_xlabel("model confidence (max calibrated probability)")
    ax.set_ylabel("density")
    ax.set_title("Does the model know when a painting is by none of the ten?")
    ax.legend(fontsize=8)
    fig.tight_layout()
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=150)
    plt.close(fig)
    return path


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
