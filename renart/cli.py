"""Command-line entry point: `python -m renart <command>`.

    download        build the WikiArt subset: train/val/test (needs network + huggingface_hub)
    download-ood    a few painters outside the set, for the out-of-set test
    train-baseline  hand-crafted features + logistic regression / random forest
    train-cnn       fine-tune ResNet-18, pick the epoch on val, report on test (needs torch)
    ood             does the CNN notice a painting is by none of the ten? (needs torch)
    export          export the CNN to ONNX for the browser demo (needs torch)
    predict         top-3 artists for an image with a saved model
    gradcam         heatmaps of what the CNN looked at (needs torch)
    report          merge metrics JSON files into a Markdown table
    site            build the static results site from committed results (see site.toml)
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

from .config import DataConfig, pretty_name, smoke_config
from .data import load_ood, load_splits

MODEL_META = "renart_model.json"


def _cfg_from_args(args) -> DataConfig:
    cfg = smoke_config(args.data) if args.smoke else DataConfig(root=Path(args.data))
    if getattr(args, "artists", None):
        cfg.artists = args.artists
    if getattr(args, "per_artist", None):
        cfg.images_per_artist = args.per_artist
    if getattr(args, "max_artists", None):
        cfg.max_artists = args.max_artists
    if getattr(args, "keep_sketches", False):
        cfg.exclude_genres = []
    return cfg


def cmd_download(args) -> int:
    from .download import download_wikiart
    cfg = _cfg_from_args(args)
    stats = download_wikiart(cfg, max_shards=args.max_shards)
    print(json.dumps(stats["counts"], indent=2))
    return 0


def cmd_download_ood(args) -> int:
    from .download import download_ood
    cfg = smoke_config(args.data) if args.smoke else DataConfig(root=Path(args.data))
    stats = download_ood(cfg, artists=args.artists or None, per_artist=args.per_artist, max_shards=args.max_shards)
    print(json.dumps(stats["counts"], indent=2))
    return 0


def _describe(splits) -> None:
    test = len(splits.test) if splits.test is not None else 0
    print(f"train={len(splits.train)} val={len(splits.val)} test={test} classes={splits.classes} "
          f"(reporting on {splits.eval_name})")


def cmd_train_baseline(args) -> int:
    from .baseline import featurise, save_model, train_baseline
    from .metrics import evaluate_predictions, save_confusion_matrix, write_json
    splits = load_splits(Path(args.data))
    _describe(splits)
    train, val, ev = splits.train, splits.val, splits.eval
    t0 = time.time()
    size = (224, 224)
    x_train = featurise(train, size)
    x_val = featurise(val, size)
    x_eval = x_val if splits.eval_name == "val" else featurise(ev, size)
    feat_seconds = time.time() - t0
    model = train_baseline(x_train, train.labels, kind=args.classifier)
    result = evaluate_predictions(ev.labels, model.predict_proba(x_eval), ev.classes, f"baseline-{args.classifier}")
    result["eval_split"] = splits.eval_name
    result["val_accuracy"] = float((model.predict(x_val) == val.labels).mean()) if len(val) else None
    result["feature_dim"] = int(x_train.shape[1])
    result["n_train"] = len(train)
    result["feature_seconds"] = round(feat_seconds, 1)
    out = Path(args.out)
    write_json(result, out / f"metrics_baseline_{args.classifier}.json")
    save_confusion_matrix(result["confusion_matrix"], ev.classes,
                          out / f"confusion_baseline_{args.classifier}.png",
                          f"Baseline ({args.classifier}) {splits.eval_name} acc={result['accuracy']:.2f}")
    save_model(model, ev.classes, out / f"baseline_{args.classifier}.pkl")
    print(f"{splits.eval_name} accuracy={result['accuracy']:.3f} macro_f1={result['macro_f1']:.3f} "
          f"(chance {result['chance_accuracy']:.3f})")
    return 0


def cmd_train_cnn(args) -> int:
    from .cnn import IMAGENET_MEAN, IMAGENET_STD, train_cnn
    from .metrics import (
        evaluate_predictions,
        expected_calibration_error,
        fit_temperature,
        save_confusion_matrix,
        softmax,
        write_json,
    )
    splits = load_splits(Path(args.data))
    _describe(splits)
    train, val = splits.train, splits.val
    out = Path(args.out)
    res = train_cnn(train, val, out, epochs=args.epochs, batch_size=args.batch_size, lr=args.lr,
                    arch=args.arch, workers=args.workers, unfreeze=args.unfreeze, test=splits.test)

    # Calibrate on val (where the epoch was also chosen), score on test.
    temperature = fit_temperature(res["val_logits"], val.labels)
    if res["test_logits"] is not None:
        eval_logits, ev = res["test_logits"], splits.test
    else:
        eval_logits, ev = res["val_logits"], val
    probs = softmax(eval_logits, temperature)
    result = evaluate_predictions(ev.labels, probs, ev.classes, f"cnn-{args.arch}")
    result["eval_split"] = splits.eval_name
    result["val_accuracy"] = float(res["best_val_acc"])
    result["calibration"] = {
        "temperature": round(temperature, 4),
        "ece_before": expected_calibration_error(softmax(eval_logits), ev.labels)["ece"],
        **expected_calibration_error(probs, ev.labels),
    }
    result["epochs"] = args.epochs
    result["unfreeze_stages"] = args.unfreeze
    result["n_train"] = len(train)
    result["history"] = res["history"]
    result["train_seconds"] = round(sum(h["seconds"] for h in res["history"]), 1)
    write_json(result, out / f"metrics_cnn_{args.arch}.json")
    save_confusion_matrix(result["confusion_matrix"], ev.classes, out / f"confusion_cnn_{args.arch}.png",
                          f"CNN ({args.arch}) {splits.eval_name} acc={result['accuracy']:.2f}")
    # What the demo and `predict` need to turn logits into calibrated probabilities.
    write_json({
        "classes": ev.classes, "labels": [pretty_name(c) for c in ev.classes], "arch": args.arch,
        "input_size": 224, "mean": IMAGENET_MEAN, "std": IMAGENET_STD, "temperature": round(temperature, 4),
        "abstain_below": None, "eval_split": splits.eval_name, "accuracy": result["accuracy"],
        "top3_accuracy": result.get("top3_accuracy"), "n_eval": result["n_eval"],
    }, out / MODEL_META)
    print(f"val accuracy={res['best_val_acc']:.3f} | {splits.eval_name} accuracy={result['accuracy']:.3f} "
          f"macro_f1={result['macro_f1']:.3f} | temperature={temperature:.2f} "
          f"ECE {result['calibration']['ece_before']:.3f} -> {result['calibration']['ece']:.3f}")
    return 0


def cmd_ood(args) -> int:
    from .cnn import load_cnn, predict_logits
    from .metrics import ood_report, save_confidence_histogram, softmax, write_json
    out = Path(args.out)
    meta_path = out / MODEL_META
    meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
    temperature = float(meta.get("temperature", 1.0))
    splits = load_splits(Path(args.data))
    ood = load_ood(Path(args.data))
    if not ood:
        print(f"no out-of-set images under {Path(args.data) / 'ood'}; run `renart download-ood` first")
        return 1
    model, classes = load_cnn(Path(args.model))
    if classes != splits.classes:
        raise RuntimeError(f"model classes {classes} do not match the data {splits.classes}")
    in_scores = softmax(predict_logits(model, splits.eval, workers=args.workers), temperature).max(axis=1)
    out_scores = {name: softmax(predict_logits(model, folder, workers=args.workers), temperature).max(axis=1)
                  for name, folder in ood.items()}
    report = ood_report(in_scores, out_scores, keep_rate=args.keep)
    report["in_split"] = splits.eval_name
    report["keep_rate"] = args.keep
    ood_stats = Path(args.data) / "ood" / "ood_stats.json"
    if ood_stats.exists():
        report["painters_missing_from_dataset"] = json.loads(ood_stats.read_text()).get("missing_from_dataset", [])
    write_json(report, out / "metrics_ood.json")
    save_confidence_histogram(in_scores, out_scores, report["threshold"], out / "ood_confidence.png",
                              pretty=pretty_name)
    if meta:
        meta["abstain_below"] = report["threshold"]
        meta["ood"] = {"auroc": report["auroc"], "out_of_set_rejected": report["out_of_set_rejected"],
                       "in_set_kept": report["in_set_kept"], "painters": sorted(ood)}
        write_json(meta, meta_path)
    print(f"AUROC={report['auroc']} threshold={report['threshold']:.3f} "
          f"keeps {report['in_set_kept']:.0%} of the ten, rejects {report['out_of_set_rejected']:.0%} of outsiders")
    for name, r in report["per_painter"].items():
        print(f"  {name:<22} n={r['n']:<3} auroc={r['auroc']} rejected={r['rejected_at_threshold']}")
    return 0


def cmd_export(args) -> int:
    from .cnn import check_onnx, export_onnx
    path = export_onnx(Path(args.model), Path(args.out))
    print(f"wrote {path} ({path.stat().st_size / 1e6:.1f} MB)")
    if args.check:
        diff = check_onnx(Path(args.model), path, Path(args.check))
        print(f"onnxruntime agrees with torch to {diff:.2e}")
    return 0


def cmd_predict(args) -> int:
    path = Path(args.model)
    if path.suffix == ".pt":
        from .cnn import load_cnn, predict_image
        meta_path = path.parent / MODEL_META
        meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
        model, classes = load_cnn(path)
        ranked = predict_image(model, classes, Path(args.image), top_k=3,
                               temperature=float(meta.get("temperature", 1.0)))
        threshold = meta.get("abstain_below")
        if threshold is not None and ranked[0][1] < threshold:
            print(f"probably none of these {len(classes)} painters (confidence {ranked[0][1]:.2f} "
                  f"< {threshold:.2f}); the nearest are:")
    else:
        from .baseline import load_model
        from .data import load_image
        from .features import extract_features
        model, classes = load_model(path)
        probs = model.predict_proba(extract_features(load_image(Path(args.image), (224, 224)))[None])[0]
        order = np.argsort(-probs)[:3]
        ranked = [(classes[i], float(probs[i])) for i in order]
    for name, p in ranked:
        print(f"{name:<28} {p:.3f}")
    return 0


def cmd_gradcam(args) -> int:
    from .gradcam import render_gradcam
    splits = load_splits(Path(args.data))
    out = render_gradcam(Path(args.model), splits.eval, Path(args.out), n=args.n)
    print(f"wrote {out}")
    return 0


def cmd_report(args) -> int:
    from .metrics import markdown_table
    results = [json.loads(Path(p).read_text()) for p in args.metrics]
    print(markdown_table(results))
    return 0


def cmd_site(args) -> int:
    from .site import build_site
    target = build_site(Path(args.config), Path(args.out))
    print(f"wrote {target}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="renart", description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="command", required=True)

    d = sub.add_parser("download", help="download a WikiArt subset")
    d.add_argument("--data", default="data/renaissance")
    d.add_argument("--smoke", action="store_true", help="2 artists, 20 images each")
    d.add_argument("--artists", nargs="*", help="override the artist slugs")
    d.add_argument("--per-artist", type=int, dest="per_artist")
    d.add_argument("--max-artists", type=int, dest="max_artists")
    d.add_argument("--max-shards", type=int, dest="max_shards", help="scan at most N parquet shards")
    d.add_argument("--keep-sketches", action="store_true", dest="keep_sketches",
                   help="do not filter out the sketch_and_study genre")
    d.set_defaults(func=cmd_download)

    o = sub.add_parser("download-ood", help="download a few painters outside the set (for `ood`)")
    o.add_argument("--data", default="data/renaissance")
    o.add_argument("--smoke", action="store_true")
    o.add_argument("--artists", nargs="*", help="override the out-of-set painter slugs")
    o.add_argument("--per-artist", type=int, dest="per_artist", default=25)
    o.add_argument("--max-shards", type=int, dest="max_shards")
    o.set_defaults(func=cmd_download_ood)

    b = sub.add_parser("train-baseline", help="train the classical baseline")
    b.add_argument("--data", default="data/renaissance")
    b.add_argument("--out", default="results")
    b.add_argument("--classifier", choices=["logreg", "forest"], default="logreg")
    b.set_defaults(func=cmd_train_baseline)

    c = sub.add_parser("train-cnn", help="fine-tune a pretrained CNN")
    c.add_argument("--data", default="data/renaissance")
    c.add_argument("--out", default="results")
    c.add_argument("--epochs", type=int, default=8)
    c.add_argument("--batch-size", type=int, dest="batch_size", default=32)
    c.add_argument("--lr", type=float, default=3e-4)
    c.add_argument("--arch", choices=["resnet18", "efficientnet_b0"], default="resnet18")
    c.add_argument("--workers", type=int, default=2)
    c.add_argument("--unfreeze", type=int, default=1, help="ResNet stages to fine-tune, counting from the end")
    c.set_defaults(func=cmd_train_cnn)

    od = sub.add_parser("ood", help="measure whether the CNN notices paintings by none of the ten")
    od.add_argument("--model", default="results/cnn.pt")
    od.add_argument("--data", default="data/renaissance")
    od.add_argument("--out", default="results")
    od.add_argument("--keep", type=float, default=0.95,
                    help="share of in-set test paintings the abstention threshold must keep")
    od.add_argument("--workers", type=int, default=2)
    od.set_defaults(func=cmd_ood)

    ex = sub.add_parser("export", help="export the CNN to ONNX")
    ex.add_argument("--model", default="results/cnn.pt")
    ex.add_argument("--out", default="results/renart.onnx")
    ex.add_argument("--check", help="an image to compare torch and onnxruntime on")
    ex.set_defaults(func=cmd_export)

    pr = sub.add_parser("predict", help="rank artists for one image")
    pr.add_argument("--model", required=True, help="results/cnn.pt or results/baseline_logreg.pkl")
    pr.add_argument("image")
    pr.set_defaults(func=cmd_predict)

    g = sub.add_parser("gradcam", help="Grad-CAM heatmaps for a few validation images")
    g.add_argument("--model", default="results/cnn.pt")
    g.add_argument("--data", default="data/renaissance")
    g.add_argument("--out", default="results/gradcam.png")
    g.add_argument("--n", type=int, default=6)
    g.set_defaults(func=cmd_gradcam)

    r = sub.add_parser("report", help="print a Markdown comparison table")
    r.add_argument("metrics", nargs="+")
    r.set_defaults(func=cmd_report)

    s = sub.add_parser("site", help="build the static results site from committed results")
    s.add_argument("--config", default="site.toml", help="site configuration (default site.toml)")
    s.add_argument("--out", default="site", help="output directory (default site/)")
    s.set_defaults(func=cmd_site)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
