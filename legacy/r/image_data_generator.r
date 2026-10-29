train_data <- image_data_generator(
  rescale = 1/255,
  rotation_range = 40,
  width_shift_range = 0.2,
  height_shift_range = 0.2,
  shear_range = 0.2,
  zoom_range = 0.2,
  horizontal_flip = TRUE,
  fill_mode = 'nearest'
) %>%
flow_images_from_directory(
  train_data_dir,
  target_size = c(150, 150),
  batch_size = 32,
  class_mode = "categorical"
)
