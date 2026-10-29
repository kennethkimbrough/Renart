"""Command-line entry point: `python -m renart <command>`.

    download        build the WikiArt subset (needs network + huggingface_hub)
    train-baseline  hand-crafted features + logistic regression / random forest
    train-cnn       fine-tune ResNet-18 (needs torch)
    predict         top-3 artists for an image with a saved model
    report          merge metrics JSON files into a Markdown table
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np

from .config import DataConfig, smoke_config
from .data import load_dataset


def _cfg_from_args(args) -> DataConfig:
    cfg = smoke_config(args.data) if args.smoke else DataConfig(root=Path(args.data))
    if args.artists:
        cfg.artists = args.artists
    if args.per_artist:
        cfg.images_per_artist = args.per_artist
    if args.max_artists:
        cfg.max_artists = args.max_artists
    return cfg


def cmd_download(args) -> int:
    from .download import download_wikiart
    cfg = _cfg_from_args(args)
    stats = download_wikiart(cfg, max_shards=args.max_shards)
    print(json.dumps(stats["counts"], indent=2))
    return 0


def cmd_train_baseline(args) -> int:
    from .baseline import featurise, save_model, train_baseline
    from .metrics import evaluate_predictions, save_confusion_matrix, write_json
    train, val = load_dataset(Path(args.data))
    print(f"train={len(train)} val={len(val)} classes={train.classes}")
    t0 = time.time()
    size = (224, 224)
    x_train = featurise(train, size)
    x_val = featurise(val, size)
    feat_seconds = time.time() - t0
    model = train_baseline(x_train, train.labels, kind=args.classifier)
    probs = model.predict_proba(x_val)
    result = evaluate_predictions(val.labels, probs, val.classes, f"baseline-{args.classifier}")
    result["feature_dim"] = int(x_train.shape[1])
    result["n_train"] = len(train)
    result["feature_seconds"] = round(feat_seconds, 1)
    out = Path(args.out)
    write_json(result, out / f"metrics_baseline_{args.classifier}.json")
    save_confusion_matrix(result["confusion_matrix"], val.classes,
                          out / f"confusion_baseline_{args.classifier}.png",
                          f"Baseline ({args.classifier}) acc={result['accuracy']:.2f}")
    save_model(model, val.classes, out / f"baseline_{args.classifier}.pkl")
    print(f"accuracy={result['accuracy']:.3f} macro_f1={result['macro_f1']:.3f} "
          f"(chance {result['chance_accuracy']:.3f})")
    return 0


def cmd_train_cnn(args) -> int:
    from .cnn import train_cnn
    from .metrics import evaluate_predictions, save_confusion_matrix, write_json
    train, val = load_dataset(Path(args.data))
    print(f"train={len(train)} val={len(val)} classes={train.classes}")
    out = Path(args.out)
    res = train_cnn(train, val, out, epochs=args.epochs, batch_size=args.batch_size,
                    lr=args.lr, arch=args.arch, workers=args.workers, unfreeze=args.unfreeze)
    result = evaluate_predictions(val.labels, res["val_probs"], val.classes, f"cnn-{args.arch}")
    result["epochs"] = args.epochs
    result["unfreeze_stages"] = args.unfreeze
    result["n_train"] = len(train)
    result["history"] = res["history"]
    result["train_seconds"] = round(sum(h["seconds"] for h in res["history"]), 1)
    write_json(result, out / f"metrics_cnn_{args.arch}.json")
    save_confusion_matrix(result["confusion_matrix"], val.classes, out / f"confusion_cnn_{args.arch}.png",
                          f"CNN ({args.arch}) acc={result['accuracy']:.2f}")
    print(f"accuracy={result['accuracy']:.3f} macro_f1={result['macro_f1']:.3f}")
    return 0


def cmd_predict(args) -> int:
    path = Path(args.model)
    if path.suffix == ".pt":
        from .cnn import load_cnn, predict_image
        model, classes = load_cnn(path)
        ranked = predict_image(model, classes, Path(args.image), top_k=3)
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


def cmd_report(args) -> int:
    from .metrics import markdown_table
    results = [json.loads(Path(p).read_text()) for p in args.metrics]
    print(markdown_table(results))
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
    d.set_defaults(func=cmd_download)

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

    pr = sub.add_parser("predict", help="rank artists for one image")
    pr.add_argument("--model", required=True, help="results/cnn.pt or results/baseline_logreg.pkl")
    pr.add_argument("image")
    pr.set_defaults(func=cmd_predict)

    r = sub.add_parser("report", help="print a Markdown comparison table")
    r.add_argument("metrics", nargs="+")
    r.set_defaults(func=cmd_report)
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
