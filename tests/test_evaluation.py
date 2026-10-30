"""Splits, the genre filter, calibration and the out-of-set report (no network, no torch)."""

from __future__ import annotations

import json
from collections import Counter

import numpy as np
import pytest

from renart.cli import main
from renart.config import DEFAULT_ARTISTS, OOD_ARTISTS, split_for
from renart.data import load_ood, load_splits
from renart.download import keep_row
from renart.metrics import expected_calibration_error, fit_temperature, nll, ood_report, softmax


def test_split_rule_is_deterministic_and_balanced():
    counts = Counter(split_for(n) for n in range(2000))
    assert counts["train"] == 1400 and counts["val"] == 300 and counts["test"] == 300
    # Each split is spread through the sequence rather than taken from one end.
    assert {split_for(n) for n in range(20)} == {"train", "val", "test"}
    assert [split_for(n) for n in range(10)] == [split_for(n) for n in range(10)]


def test_out_of_set_painters_are_outside_the_set():
    assert not set(OOD_ARTISTS) & set(DEFAULT_ARTISTS)


def test_genre_filter_keeps_unlabelled_rows():
    assert keep_row(None, {3})
    assert keep_row(1, {3})
    assert not keep_row(3, {3})
    assert keep_row(3, set())


def test_load_splits_without_a_test_split_scores_val(synthetic_dataset):
    without = load_splits(synthetic_dataset)
    assert without.test is None and without.eval_name == "val" and len(without.eval) == 8
    assert load_ood(synthetic_dataset) == {}


def test_load_splits_reports_which_split_is_scored(synthetic_dataset_with_test):
    with_test = load_splits(synthetic_dataset_with_test)
    assert with_test.eval_name == "test" and len(with_test.test) == 6
    assert with_test.test.classes == with_test.train.classes
    ood = load_ood(synthetic_dataset_with_test)
    assert list(ood) == ["artist-grey"] and len(ood["artist-grey"]) == 3


def test_baseline_is_scored_on_test_when_present(synthetic_dataset_with_test, tmp_path):
    out = tmp_path / "results"
    assert main(["train-baseline", "--data", str(synthetic_dataset_with_test), "--out", str(out)]) == 0
    metrics = json.loads((out / "metrics_baseline_logreg.json").read_text())
    assert metrics["eval_split"] == "test" and metrics["n_eval"] == 6
    assert metrics["val_accuracy"] == 1.0 and metrics["accuracy"] == 1.0


def test_temperature_scaling_fixes_overconfidence():
    rng = np.random.RandomState(0)
    y = rng.randint(0, 4, size=400)
    # Logits that point the right way 70% of the time but are scaled up five-fold: overconfident.
    z = rng.normal(0, 1, size=(400, 4))
    hit = rng.rand(400) < 0.7
    z[np.arange(400)[hit], y[hit]] += 3.0
    z *= 5.0
    t = fit_temperature(z, y)
    assert t > 2.0
    assert nll(z, y, t) < nll(z, y, 1.0)
    before = expected_calibration_error(softmax(z), y)["ece"]
    after = expected_calibration_error(softmax(z, t), y)["ece"]
    assert after < before
    # Scaling never changes the ranking.
    assert np.array_equal(softmax(z).argmax(1), softmax(z, t).argmax(1))
    assert fit_temperature(z[:0], y[:0]) == 1.0


def test_ece_of_perfectly_calibrated_bins_is_zero():
    probs = np.array([[0.9, 0.1]] * 10)
    y = np.array([0] * 9 + [1])  # 90% right at 90% confidence
    assert expected_calibration_error(probs, y, bins=10)["ece"] == pytest.approx(0.0, abs=1e-9)


def test_ood_report_threshold_and_rejection():
    in_scores = np.linspace(0.5, 1.0, 100)
    out_scores = {"far": np.linspace(0.1, 0.4, 20), "near": np.linspace(0.3, 0.8, 20)}
    r = ood_report(in_scores, out_scores, keep_rate=0.95)
    assert r["n_in"] == 100 and r["n_out"] == 40
    assert r["in_set_kept"] >= 0.95
    assert r["per_painter"]["far"]["auroc"] == 1.0 and r["per_painter"]["far"]["rejected_at_threshold"] == 1.0
    assert 0.5 < r["per_painter"]["near"]["auroc"] < 1.0
    assert r["auroc"] > 0.9
    empty = ood_report(in_scores, {})
    assert empty["auroc"] is None and empty["n_out"] == 0
