### Limitations

- **Ten painters, WikiArt images.** The model only chooses among the ten painters it saw; anything else is forced into one of them. WikiArt images vary in resolution, colour balance and framing, and some are details or studies rather than finished paintings.
- **Style is not authorship.** Workshop pieces, pupils and later copies share a master's style by design. Renart says nothing about materials, age or provenance, and it cannot tell a painting from a good copy of it.
- **Small validation set.** With 25 to 40 images per painter, a single image moves a painter's accuracy by three or four points; the intervals on this page show how wide that uncertainty is.
- **No separate test set.** The reported epoch is the one with the best validation accuracy, chosen on the same images it is scored on, which biases the CNN's figure slightly upward. A held-out test split is the obvious next step.
- **CPU budget.** ResNet-18 at 224 pixels for 12 epochs on a GitHub Actions runner. A larger backbone, higher resolution and more images per painter would all help.
