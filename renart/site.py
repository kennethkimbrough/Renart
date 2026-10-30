"""Build the static results site from committed results.

    python -m renart site [--config site.toml] [--out site]

The output is one self-contained ``index.html`` (the template in
``site_template.html`` with the data embedded as JSON) plus the run's Grad-CAM
image. Every number is computed here from the committed metrics files, so the
site cannot disagree with them, and nothing is downloaded or trained.
"""

from __future__ import annotations

import html
import json
import math
import re
import shutil
from importlib import resources
from pathlib import Path

REPO_URL = "https://github.com/kennethkimbrough/Renart"

PAINTER_LABELS = {
    "albrecht-durer": "Albrecht Dürer",
    "fra-angelico": "Fra Angelico",
    "hans-memling": "Hans Memling",
    "hieronymus-bosch": "Hieronymus Bosch",
    "leonardo-da-vinci": "Leonardo da Vinci",
    "michelangelo": "Michelangelo",
    "paolo-veronese": "Paolo Veronese",
    "raphael": "Raphael",
    "tintoretto": "Tintoretto",
    "titian": "Titian",
}

MODEL_FILES = [
    ("cnn_resnet18", "metrics_cnn_resnet18.json", "ResNet-18, fine-tuned",
     "ImageNet-pretrained network with its last two stages retrained on the paintings."),
    ("baseline_logreg", "metrics_baseline_logreg.json", "Logistic regression",
     "102 hand-crafted colour and brush-stroke features per image."),
    ("baseline_forest", "metrics_baseline_forest.json", "Random forest",
     "The same 102 hand-crafted features, with a random forest."),
]


def label(slug: str) -> str:
    return PAINTER_LABELS.get(slug, slug.replace("-", " ").title())


def wilson(successes: int, n: int, z: float = 1.96) -> dict | None:
    """Wilson score interval for a proportion: better behaved than the normal one near 0% and 100%."""
    if n <= 0:
        return None
    p = successes / n
    denom = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / denom
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / denom
    lo, hi = max(0.0, centre - half), min(1.0, centre + half)
    return {"v": round(p, 4), "lo": round(lo, 4), "hi": round(hi, 4), "k": successes, "n": n}


def render_markdown(text: str) -> str:
    """A small Markdown subset: ### headings, - bullets, paragraphs, **bold**, *italic*, `code`, links."""

    def inline(s: str) -> str:
        s = html.escape(s, quote=False)
        s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
        s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
        s = re.sub(r"(?<![*\w])\*([^*]+)\*(?![*\w])", r"<em>\1</em>", s)

        def link(m: re.Match) -> str:
            if not re.match(r"^(https?://|#)", m.group(2)):
                return m.group(1)
            return f'<a href="{html.escape(m.group(2))}">{m.group(1)}</a>'

        return re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, s)

    out: list[str] = []
    paragraph: list[str] = []
    items: list[str] = []

    def flush() -> None:
        if paragraph:
            out.append(f"<p>{inline(' '.join(paragraph))}</p>")
            paragraph.clear()
        if items:
            out.append("<ul>" + "".join(f"<li>{inline(i)}</li>" for i in items) + "</ul>")
            items.clear()

    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush()
        elif line.startswith("### "):
            flush()
            out.append(f"<h3>{inline(line[4:].strip())}</h3>")
        elif line.startswith("- "):
            if paragraph:
                flush()
            items.append(line[2:].strip())
        elif items and raw.startswith("  "):
            items[-1] += " " + line.strip()
        else:
            if items:
                flush()
            paragraph.append(line.strip())
    flush()
    return "\n".join(out)


def load_config(path: Path) -> dict:
    try:
        import tomllib
    except ModuleNotFoundError as e:  # Python 3.10
        raise RuntimeError("building the site needs Python 3.11 or newer (tomllib)") from e
    with Path(path).open("rb") as f:
        return tomllib.load(f)


def _read(run_dir: Path, name: str) -> dict | list | None:
    p = run_dir / name
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def _model(metrics: dict, order: list[str]) -> dict:
    """Accuracy and top-3 with Wilson intervals, the confusion matrix reordered, and per-painter results."""
    classes = metrics["classes"]
    idx = [classes.index(p) for p in order]
    cm = metrics["confusion_matrix"]
    matrix = [[int(cm[i][j]) for j in idx] for i in idx]
    n = sum(sum(row) for row in matrix)
    correct = sum(matrix[i][i] for i in range(len(order)))
    if n != metrics["n_eval"]:
        raise ValueError(f"confusion matrix sums to {n} but n_eval is {metrics['n_eval']}")
    if abs(correct / n - metrics["accuracy"]) > 1e-9:
        raise ValueError("confusion matrix diagonal does not match the reported accuracy")
    painters = [wilson(matrix[i][i], sum(matrix[i])) for i in range(len(order))]
    top3_k = round(metrics["top3_accuracy"] * n)
    return {
        "accuracy": wilson(correct, n),
        "top3": wilson(top3_k, n),
        "macro_f1": round(metrics["macro_f1"], 4),
        "chance": metrics.get("chance_accuracy"),
        "matrix": matrix,
        "painters": painters,
    }


def school_errors(matrix: list[list[int]], order: list[str], school_of: dict[str, str]) -> dict:
    """How many mistakes land on a painter from the same school, against what random mistakes would give."""
    errors = within = 0
    expected = 0.0
    k = len(order)
    for i, t in enumerate(order):
        row_errors = sum(matrix[i]) - matrix[i][i]
        same = sum(1 for p in order if p != t and school_of.get(p) == school_of.get(t))
        expected += row_errors * same / (k - 1)
        for j, p in enumerate(order):
            if i != j:
                errors += matrix[i][j]
                within += matrix[i][j] if school_of.get(p) == school_of.get(t) else 0
    share = round(expected / errors, 4) if errors else None
    return {"errors": errors, "within": within, "expected_share": share}


def _same_results(a: Path, b: Path) -> dict:
    """Compare two runs' outputs, ignoring timing fields."""
    def strip(h):
        return [{k: v for k, v in e.items() if k != "seconds"} for e in (h or [])]

    out = {"history_identical": strip(_read(a, "cnn_history.json")) == strip(_read(b, "cnn_history.json"))}
    for key, fname, *_ in MODEL_FILES:
        ma, mb = _read(a, fname), _read(b, fname)
        out[key] = bool(ma and mb and ma["confusion_matrix"] == mb["confusion_matrix"]
                        and ma["accuracy"] == mb["accuracy"] and ma["top3_accuracy"] == mb["top3_accuracy"])
    ca, cb = _read(a, "metrics_cnn_resnet18.json") or {}, _read(b, "metrics_cnn_resnet18.json") or {}
    out["train_seconds"] = [ca.get("train_seconds"), cb.get("train_seconds")]
    return out


def _ood_summary(report: dict | None, has_plot: bool) -> dict | None:
    """The out-of-set check, reduced to what the page shows."""
    if not report or not report.get("per_painter"):
        return None
    return {
        "auroc": report.get("auroc"),
        "threshold": report.get("threshold"),
        "in_set_kept": report.get("in_set_kept"),
        "out_of_set_rejected": report.get("out_of_set_rejected"),
        "n_in": report.get("n_in"),
        "n_out": report.get("n_out"),
        "in_split": report.get("in_split", "test"),
        "painters": [{"slug": k, "label": label(k), **v} for k, v in report["per_painter"].items()],
        "plot": "ood_confidence.png" if has_plot else None,
    }


def _demo_model(meta: dict | None, release: str | None) -> dict | None:
    """What the browser demo needs; None when the run has no exported model description."""
    if not meta:
        return None
    return {
        "classes": meta["classes"],
        "labels": [label(c) for c in meta["classes"]],
        "input_size": meta.get("input_size", 224),
        "mean": meta["mean"],
        "std": meta["std"],
        "temperature": meta.get("temperature", 1.0),
        "abstain_below": meta.get("abstain_below"),
        "accuracy": meta.get("accuracy"),
        "top3_accuracy": meta.get("top3_accuracy"),
        "n_eval": meta.get("n_eval"),
        "eval_split": meta.get("eval_split", "val"),
        "release": release,
        "url": "model/renart.onnx",
    }


def site_data(config_path: Path) -> dict:
    config_path = Path(config_path)
    root = config_path.parent
    cfg = load_config(config_path)
    run = root / cfg["run"]
    stats = _read(run, "dataset_stats.json")
    schools = cfg.get("schools") or [{"name": "", "painters": stats["artists"]}]
    order = [p for s in schools for p in s["painters"]]
    if sorted(order) != sorted(stats["artists"]):
        raise ValueError(f"the schools in {config_path.name} must list each of the run's painters "
                         "exactly once")
    school_of = {p: s["name"] for s in schools for p in s["painters"]}

    models = []
    for key, fname, title, desc in MODEL_FILES:
        metrics = _read(run, fname)
        if metrics is None:
            continue
        m = _model(metrics, order)
        m.update({"key": key, "label": title, "description": desc,
                  "school_errors": school_errors(m["matrix"], order, school_of)})
        models.append(m)

    cnn = _read(run, "metrics_cnn_resnet18.json") or {}
    history = _read(run, "cnn_history.json") or cnn.get("history") or []
    best = max(history, key=lambda e: e["val_acc"])["epoch"] if history else None
    eval_split = cnn.get("eval_split", "val")
    counts = stats["counts"]

    data = {
        "repo": REPO_URL,
        "run": {
            "path": cfg["run"],
            "name": run.name,
            "source": stats.get("source"),
            "images": stats["total_images"],
            "train": sum(c["train"] for c in counts.values()),
            "val": sum(c["val"] for c in counts.values()),
            "test": sum(c.get("test", 0) for c in counts.values()),
            "eval_split": eval_split,
            "split_word": "test" if eval_split == "test" else "validation",
            "excluded_genres": stats.get("excluded_genres") or [],
            "excluded_images": sum((stats.get("excluded_counts") or {}).values()),
            "image_size": stats.get("image_size"),
            "epochs": cnn.get("epochs"),
            "unfreeze": cnn.get("unfreeze_stages"),
            "train_seconds": cnn.get("train_seconds"),
            "val_accuracy": cnn.get("val_accuracy"),
        },
        "painters": [{"slug": p, "label": label(p), "school": school_of[p], "test": 0, **counts[p]}
                     for p in order],
        "schools": [{"name": s["name"], "size": len(s["painters"])} for s in schools],
        "models": models,
        "history": [{k: e[k] for k in ("epoch", "train_loss", "train_acc", "val_acc")} for e in history],
        "best_epoch": best,
        "calibration": cnn.get("calibration"),
        "gradcam": "gradcam.png" if (run / "gradcam.png").exists() else None,
        "gradcam_caption": cfg.get("gradcam_caption"),
        "ood": _ood_summary(_read(run, "metrics_ood.json"), (run / "ood_confidence.png").exists()),
        "model": _demo_model(_read(run, "renart_model.json"), cfg.get("model_release")),
        "notes_html": "",
    }
    if cfg.get("notes"):
        data["notes_html"] = render_markdown((root / cfg["notes"]).read_text(encoding="utf-8"))

    if cfg.get("repeat"):
        data["repeat"] = {"path": cfg["repeat"], "name": Path(cfg["repeat"]).name,
                          **_same_results(run, root / cfg["repeat"])}
    if cfg.get("previous"):
        prev_dir = root / cfg["previous"]
        prev = _read(prev_dir, "metrics_cnn_resnet18.json")
        prev_stats = _read(prev_dir, "dataset_stats.json")
        if prev and prev_stats:
            k = round(prev["accuracy"] * prev["n_eval"])
            data["previous"] = {
                "path": cfg["previous"], "name": prev_dir.name, "accuracy": wilson(k, prev["n_eval"]),
                "top3": round(prev["top3_accuracy"], 4), "images": prev_stats["total_images"],
                "epochs": prev.get("epochs"), "unfreeze": prev.get("unfreeze_stages", 1),
            }
    return data


def _render(template_name: str, data: dict) -> str:
    # "</" must not appear inside a <script> element; "<\\/" is the same string to JSON.
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    payload = payload.replace("</", "<\\/")
    template = resources.files("renart").joinpath(template_name).read_text(encoding="utf-8")
    page = template.replace("/*__DATA__*/null", payload)
    if page == template:
        raise RuntimeError(f"{template_name} has no data placeholder")
    return page


def build_site(config_path: Path, out_dir: Path) -> Path:
    """Write index.html (the results), demo.html (try the model in the browser) and their images.

    The ONNX model itself is not in the repository: the Pages workflow downloads
    it from the release named by `model_release` in site.toml into `model/`.
    """
    config_path = Path(config_path)
    data = site_data(config_path)
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "index.html").write_text(_render("site_template.html", data), encoding="utf-8")
    (out_dir / ".nojekyll").write_text("", encoding="utf-8")
    run_dir = config_path.parent / load_config(config_path)["run"]
    if data["gradcam"]:
        shutil.copyfile(run_dir / "gradcam.png", out_dir / "gradcam.png")
    if data["ood"] and data["ood"]["plot"]:
        shutil.copyfile(run_dir / "ood_confidence.png", out_dir / "ood_confidence.png")
    if data["model"]:
        demo = {"repo": REPO_URL, "model": data["model"], "ood": data["ood"], "run": data["run"]}
        (out_dir / "demo.html").write_text(_render("demo_template.html", demo), encoding="utf-8")
    return out_dir / "index.html"
