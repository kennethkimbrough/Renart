import json

from renart.baseline import featurise, load_model, save_model, train_baseline
from renart.cli import main
from renart.data import load_dataset
from renart.metrics import evaluate_predictions, markdown_table


def test_baseline_learns_synthetic_styles(synthetic_dataset, tmp_path):
    train, val = load_dataset(synthetic_dataset)
    x_train = featurise(train, (224, 224), log_every=0)
    x_val = featurise(val, (224, 224), log_every=0)
    model = train_baseline(x_train, train.labels)
    result = evaluate_predictions(val.labels, model.predict_proba(x_val), val.classes, "test")
    assert result["accuracy"] == 1.0
    assert result["confusion_matrix"] == [[4, 0], [0, 4]]
    assert "| test |" in markdown_table([result])

    path = save_model(model, val.classes, tmp_path / "m.pkl")
    loaded, classes = load_model(path)
    assert classes == val.classes
    assert loaded.predict(x_val[:1]).shape == (1,)


def test_cli_train_baseline_and_predict(synthetic_dataset, tmp_path, capsys):
    out = tmp_path / "results"
    assert main(["train-baseline", "--data", str(synthetic_dataset), "--out", str(out)]) == 0
    metrics = json.loads((out / "metrics_baseline_logreg.json").read_text())
    assert metrics["n_eval"] == 8 and metrics["feature_dim"] > 50
    assert (out / "confusion_baseline_logreg.png").exists()

    _, val = load_dataset(synthetic_dataset)
    assert main(["predict", "--model", str(out / "baseline_logreg.pkl"), str(val.paths[0])]) == 0
    lines = capsys.readouterr().out.strip().splitlines()[-2:]  # two classes -> two ranked lines
    assert lines[0].startswith("artist-cool")
    assert float(lines[0].split()[-1]) >= float(lines[1].split()[-1])
