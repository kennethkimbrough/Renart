### Limitations

- **Ten painters, WikiArt images.** The model only chooses among the ten painters it saw. WikiArt images vary in resolution, colour balance and framing, and some are details rather than whole paintings.
- **Weak out-of-set detection.** Confidence separates paintings by other painters from the ten only modestly (AUROC 0.67). At a threshold that keeps 95% of the ten painters' test paintings, just 7% of outsiders are turned away, and Rembrandt not at all. An answer about a painting by someone outside the ten should be read as meaningless.
- **Style is not authorship.** Workshop pieces, pupils and later copies share a master's style by design. Renart says nothing about materials, age or provenance, and it cannot tell a painting from a good copy of it.
- **Small test set.** 213 paintings, as few as 6 for Leonardo once his drawings were removed. One painting moves a painter's figure by several points; the intervals on this page show how wide that is.
- **CPU budget.** ResNet-18 at 224 pixels for 12 epochs on a GitHub Actions runner. A larger backbone, higher resolution and more images per painter would all help.
