# Run 6: an independent repeat of run 5

Run 6 is the training workflow run that started when the pipeline was merged
into `main`. It used exactly the same request as run 5 (ten painters, up to
200 images each, ResNet-18, two stages unfrozen, 12 epochs) and ran as a
separate job on a separate GitHub Actions runner: its training took 493
seconds against run 5's 798.

Every number it produced matches run 5: the loss and accuracy at every
epoch, the confusion matrices of all three models, and the Grad-CAM image
byte for byte. The pipeline is deterministic from its seeds, so a result
here can be reproduced by rerunning the workflow, not just by trusting the
committed files.

Only the JSON and Markdown outputs are kept here; the images are identical
to run 5's.
