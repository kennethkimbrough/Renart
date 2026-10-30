"""The results site: intervals, school errors, the Markdown subset, and a build from synthetic results."""

from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

import pytest

from renart.cli import main
from renart.site import build_site, render_markdown, school_errors, site_data, wilson

ROOT = Path(__file__).resolve().parents[1]
PAINTERS = ["titian", "hans-memling", "raphael"]  # the order the metrics files use


def _metrics(matrix: list[list[int]], top3: float = 1.0) -> dict:
    n = sum(map(sum, matrix))
    return {
        "classes": PAINTERS,
        "confusion_matrix": matrix,
        "n_eval": n,
        "accuracy": sum(matrix[i][i] for i in range(len(matrix))) / n,
        "top3_accuracy": top3,
        "macro_f1": 0.5,
        "chance_accuracy": 1 / len(PAINTERS),
    }


def _write(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj), encoding="utf-8")


def make_run(run: Path, cnn_matrix: list[list[int]] | None = None) -> None:
    counts = {"titian": {"train": 8, "val": 4}, "hans-memling": {"train": 8, "val": 3},
              "raphael": {"train": 8, "val": 3}}
    _write(run / "dataset_stats.json", {"artists": PAINTERS, "total_images": 34, "counts": counts,
                                        "source": "synthetic", "image_size": [224, 224]})
    cnn = _metrics(cnn_matrix or [[3, 0, 1], [0, 3, 0], [1, 0, 2]], top3=1.0)
    cnn.update({"epochs": 2, "unfreeze_stages": 2, "train_seconds": 12.5})
    _write(run / "metrics_cnn_resnet18.json", cnn)
    _write(run / "metrics_baseline_logreg.json", _metrics([[2, 1, 1], [1, 2, 0], [1, 1, 1]], top3=0.8))
    history = [{"epoch": 1, "train_loss": 1.2, "train_acc": 0.5, "val_acc": 0.6, "seconds": 6.1},
               {"epoch": 2, "train_loss": 0.8, "train_acc": 0.7, "val_acc": 0.8, "seconds": 6.4}]
    _write(run / "cnn_history.json", history)


@pytest.fixture
def project(tmp_path: Path) -> Path:
    make_run(tmp_path / "results/runs/a")
    (tmp_path / "results/runs/a/notes.md").write_text(
        "### Limitations\n\n- Small <b>set</b>, see [the data](https://example.org) and [here](local.md).\n"
        "  Continued line.\n\nA paragraph with `code` and </script> in it.\n", encoding="utf-8")
    (tmp_path / "site.toml").write_text(
        'run = "results/runs/a"\nnotes = "results/runs/a/notes.md"\n'
        '[[schools]]\nname = "North"\npainters = ["hans-memling"]\n'
        '[[schools]]\nname = "Italy"\npainters = ["raphael", "titian"]\n', encoding="utf-8")
    return tmp_path


def test_wilson_interval():
    assert wilson(0, 0) is None
    half = wilson(5, 10)
    assert half["v"] == 0.5 and half["lo"] == pytest.approx(0.2366, abs=1e-4)
    assert half["hi"] == pytest.approx(0.7634, abs=1e-4)
    none, every = wilson(0, 10), wilson(10, 10)
    assert none["lo"] == 0.0 and none["hi"] == pytest.approx(0.2775, abs=1e-4)
    assert every["hi"] == 1.0 and every["lo"] == pytest.approx(0.7225, abs=1e-4)


def test_school_errors_against_random_mistakes():
    order = ["a", "b", "c"]
    matrix = [[5, 2, 1], [0, 4, 3], [1, 1, 6]]
    result = school_errors(matrix, order, {"a": "X", "b": "X", "c": "Y"})
    # 8 mistakes, 2 of them a->b inside school X; random mistakes would land in-school 3 times in 8.
    assert result == {"errors": 8, "within": 2, "expected_share": 0.375}
    assert school_errors([[1, 0], [0, 1]], ["a", "b"], {})["expected_share"] is None


def test_markdown_subset_escapes_and_drops_relative_links():
    out = render_markdown("### Title\n\n- one <b>\n  two\n- [x](https://a.b) [y](notes.md)\n\n**bold** *it*")
    assert "<h3>Title</h3>" in out
    assert "<li>one &lt;b&gt; two</li>" in out
    assert '<a href="https://a.b">x</a> y' in out
    assert "<p><strong>bold</strong> <em>it</em></p>" in out


def test_site_data_orders_painters_by_school(project: Path):
    data = site_data(project / "site.toml")
    assert [p["slug"] for p in data["painters"]] == ["hans-memling", "raphael", "titian"]
    assert [m["key"] for m in data["models"]] == ["cnn_resnet18", "baseline_logreg"]
    cnn = data["models"][0]
    # Rows and columns follow the school order: memling, raphael, titian.
    assert cnn["matrix"] == [[3, 0, 0], [0, 2, 1], [0, 1, 3]]
    assert cnn["accuracy"]["k"] == 8 and cnn["accuracy"]["n"] == 10
    assert [p["k"] for p in cnn["painters"]] == [3, 2, 3]
    assert cnn["school_errors"] == {"errors": 2, "within": 2, "expected_share": 0.5}
    assert data["best_epoch"] == 2 and "seconds" not in data["history"][0]
    assert data["run"]["train"] == 24 and data["run"]["val"] == 10
    assert data["gradcam"] is None and "repeat" not in data


def test_build_writes_one_page_with_escaped_data(project: Path, tmp_path: Path):
    (project / "results/runs/a/gradcam.png").write_bytes(b"\x89PNG fake")
    page = build_site(project / "site.toml", tmp_path / "out")
    html = page.read_text(encoding="utf-8")
    assert "/*__DATA__*/null" not in html
    payload = re.search(r'<script id="data" type="application/json">(.*?)</script>', html, re.DOTALL).group(1)
    assert "</" not in payload  # a literal "</script>" in the notes would end the element early
    data = json.loads(payload)
    assert "&lt;/script&gt;" in data["notes_html"] and "<h3>Limitations</h3>" in data["notes_html"]
    assert (tmp_path / "out/.nojekyll").exists()
    assert (tmp_path / "out/gradcam.png").read_bytes() == b"\x89PNG fake"


def test_site_reports_the_test_split_and_the_out_of_set_check(project: Path, tmp_path: Path):
    run = project / "results/runs/a"
    cnn = json.loads((run / "metrics_cnn_resnet18.json").read_text())
    cnn.update({"eval_split": "test", "val_accuracy": 0.9,
                "calibration": {"temperature": 1.3, "ece_before": 0.12, "ece": 0.04}})
    _write(run / "metrics_cnn_resnet18.json", cnn)
    stats = json.loads((run / "dataset_stats.json").read_text())
    for c in stats["counts"].values():
        c["test"] = 2
    stats.update({"excluded_genres": ["sketch_and_study"], "excluded_counts": {"titian": 3, "raphael": 1}})
    _write(run / "dataset_stats.json", stats)
    _write(run / "metrics_ood.json", {"auroc": 0.91, "threshold": 0.55, "in_set_kept": 0.95, "out_of_set_rejected": 0.7,
                                      "n_in": 10, "n_out": 20, "in_split": "test",
                                      "per_painter": {"claude-monet": {"n": 20, "auroc": 0.91, "rejected_at_threshold": 0.7,
                                                                       "mean_confidence": 0.4}}})
    _write(run / "renart_model.json", {"classes": PAINTERS, "input_size": 224, "mean": [0.5] * 3, "std": [0.25] * 3,
                                       "temperature": 1.3, "abstain_below": 0.55, "accuracy": 0.8,
                                       "top3_accuracy": 1.0, "n_eval": 10, "eval_split": "test"})
    (run / "ood_confidence.png").write_bytes(b"\x89PNG fake")
    cfg = project / "site.toml"
    cfg.write_text('model_release = "model-run7"\n' + cfg.read_text())

    data = site_data(cfg)
    assert data["run"]["eval_split"] == "test" and data["run"]["split_word"] == "test"
    assert data["run"]["test"] == 6 and data["run"]["excluded_images"] == 4
    assert data["ood"]["auroc"] == 0.91 and data["ood"]["painters"][0]["label"] == "Claude Monet"
    assert data["ood"]["plot"] == "ood_confidence.png"
    assert data["model"]["release"] == "model-run7" and data["model"]["url"] == "model/renart.onnx"
    assert data["model"]["labels"] == ["Titian", "Hans Memling", "Raphael"]
    assert data["calibration"]["temperature"] == 1.3

    build_site(cfg, tmp_path / "out")
    demo = (tmp_path / "out/demo.html").read_text(encoding="utf-8")
    assert "/*__DATA__*/null" not in demo and "onnxruntime-web" in demo
    payload = json.loads(re.search(r'<script id="data" type="application/json">(.*?)</script>', demo, re.DOTALL).group(1))
    assert payload["model"]["abstain_below"] == 0.55 and payload["ood"]["n_out"] == 20
    assert (tmp_path / "out/ood_confidence.png").exists()


def test_site_without_a_model_has_no_demo_page(project: Path, tmp_path: Path):
    data = site_data(project / "site.toml")
    assert data["model"] is None and data["ood"] is None and data["run"]["split_word"] == "validation"
    build_site(project / "site.toml", tmp_path / "out")
    assert not (tmp_path / "out/demo.html").exists()


def test_repeat_run_comparison_ignores_timing(project: Path):
    shutil.copytree(project / "results/runs/a", project / "results/runs/b")
    history = json.loads((project / "results/runs/b/cnn_history.json").read_text())
    history[0]["seconds"] = 99.0
    _write(project / "results/runs/b/cnn_history.json", history)
    cfg = project / "site.toml"
    cfg.write_text('repeat = "results/runs/b"\n' + cfg.read_text())  # top-level keys go before [[schools]]
    repeat = site_data(project / "site.toml")["repeat"]
    assert repeat["history_identical"] and repeat["cnn_resnet18"] and repeat["baseline_logreg"]

    make_run(project / "results/runs/b", cnn_matrix=[[4, 0, 0], [0, 3, 0], [1, 0, 2]])
    repeat = site_data(project / "site.toml")["repeat"]
    assert not repeat["cnn_resnet18"] and repeat["baseline_logreg"]


def test_schools_must_cover_every_painter(project: Path):
    cfg = project / "site.toml"
    cfg.write_text(cfg.read_text().replace('["raphael", "titian"]', '["raphael"]'))
    with pytest.raises(ValueError, match="exactly once"):
        site_data(cfg)


def test_inconsistent_metrics_are_rejected(project: Path):
    path = project / "results/runs/a/metrics_cnn_resnet18.json"
    metrics = json.loads(path.read_text())
    metrics["n_eval"] += 1
    _write(path, metrics)
    with pytest.raises(ValueError, match="sums to"):
        site_data(project / "site.toml")


def test_cli_site_command(project: Path, tmp_path: Path, capsys):
    assert main(["site", "--config", str(project / "site.toml"), "--out", str(tmp_path / "s")]) == 0
    assert "index.html" in capsys.readouterr().out


def test_committed_site_config_builds():
    """The published site is built from site.toml; it must agree with the committed run 5 metrics."""
    data = site_data(ROOT / "site.toml")
    cnn = data["models"][0]
    assert cnn["key"] == "cnn_resnet18"
    assert (cnn["accuracy"]["k"], cnn["accuracy"]["n"]) == (254, 327)
    assert len(data["painters"]) == 10 and sum(s["size"] for s in data["schools"]) == 10
    assert data["repeat"]["history_identical"] and data["repeat"]["cnn_resnet18"]
