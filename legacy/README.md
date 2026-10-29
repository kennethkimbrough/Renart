# Legacy code

Earlier iterations of Renart, kept for reference. None of this is used by the
current pipeline, and none of it was ever run end to end: the R and JavaScript
versions were two parallel attempts at the same training loop, each stopping
before producing a trained model.

| Path | What it was |
|------|-------------|
| `r/main.r` | Keras-in-R training script (transfer learning on a `data/renaissance` folder). Never produced a saved model. |
| `r/coloranalysis.r`, `r/paintstroke.r` | Hand-written color-palette and stroke-dynamics feature ideas. The current `renart/features.py` ports the useful parts: dominant-color clustering, hue statistics, and gradient-based stroke orientation / curvature measures. |
| `r/model.r`, `r/data.r`, `r/function.r`, `r/get.r`, `r/accuracy.r`, `r/image_data_generator.r` | Helpers for the R pipeline, including a synthetic-image generator used for smoke testing. |
| `js/model.js`, `js/train.js`, `js/predict.js` | TensorFlow.js version of the same CNN. |
| `js/renaissanceArt.js` | A hand-maintained metadata list of paintings and artists. |
| `js/gallery.jsx` | A React gallery component with unresolved imports. |
| `renart_dataset.py` | First Python dataset script (WikiArt via Hugging Face plus the National Gallery of Art open data). Replaced by `renart/download.py`, which fixes the artist-matching bug: the Hugging Face `artist` column is an integer class label, so comparing it with artist-name strings matched nothing. |
