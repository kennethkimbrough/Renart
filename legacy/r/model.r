# Load necessary libraries
library(keras)

# Set the main path to your dataset
main_path <- "path/to/your/art_dataset"

# Load training and validation data (as previously defined)
train_data_dir <- file.path(main_path, "train")
validation_data_dir <- file.path(main_path, "validation")

# Data generators
train_data <- image_data_generator(rescale = 1/255) %>%
  flow_images_from_directory(
    train_data_dir,
    target_size = c(150, 150),  # Resize images
    batch_size = 32,
    class_mode = "categorical"   # Use categorical labels
  )

validation_data <- image_data_generator(rescale = 1/255) %>%
  flow_images_from_directory(
    validation_data_dir,
    target_size = c(150, 150),
    batch_size = 32,
    class_mode = "categorical"
  )

# Define the CNN model
model <- keras_model_sequential() %>%
  layer_conv_2d(filters = 32, kernel_size = c(3, 3), activation = 'relu', input_shape = c(150, 150, 3)) %>%
  layer_max_pooling_2d(pool_size = c(2, 2)) %>%
  
  layer_conv_2d(filters = 64, kernel_size = c(3, 3), activation = 'relu') %>%
  layer_max_pooling_2d(pool_size = c(2, 2)) %>%
  
  layer_conv_2d(filters = 128, kernel_size = c(3, 3), activation = 'relu') %>%
  layer_max_pooling_2d(pool_size = c(2, 2)) %>%
  
  layer_flatten() %>%
  layer_dense(units = 128, activation = 'relu') %>%
  layer_dropout(rate = 0.5) %>%
  layer_dense(units = length(unique(train_data$class_indices)), activation = 'softmax')  # Output layer

# Compile the model
model %>% compile(
  loss = 'categorical_crossentropy',
  optimizer = optimizer_adam(),
  metrics = c('accuracy')
)

# Print the model summary
summary(model)

# Train the model
history <- model %>% fit(
  train_data,
  validation_data = validation_data,
  epochs = 20,
  steps_per_epoch = train_data$n %/% train_data$batch_size,
  validation_steps = validation_data$n %/% validation_data$batch_size
)

# Evaluate the model on validation data
eval_results <- model %>% evaluate(validation_data)
cat("Validation Loss:", eval_results$loss, "\n")
cat("Validation Accuracy:", eval_results$accuracy, "\n")
