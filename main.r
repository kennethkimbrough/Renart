# Load necessary libraries
library(keras)
library(magrittr)

# Function to load images from a directory
load_images <- function(data_dir) {
  image_data_generator(rescale = 1/255) %>%
    flow_images_from_directory(
      data_dir,
      target_size = c(150, 150),  # Resize images
      batch_size = 32,
      class_mode = "categorical"   # Use categorical labels
    )
}

# Function to build the CNN model
build_model <- function(num_classes) {
  model <- keras_model_sequential() %>%
    layer_conv_2d(filters = 32, kernel_size = c(3, 3), activation = 'relu', input_shape = c(150, 150, 3)) %>%
    layer_max_pooling_2d(pool_size = c(2, 2)) %>%
    
    layer_conv_2d(filters = 64, kernel_size = c(3, 3), activation = 'relu') %>%
    layer_max_pooling_2d(pool_size = c(2, 2)) %>%
    
    layer_conv_2d(filters = 128, kernel_size = c(3, 3), activation = 'relu') %>%
    layer_max_pooling_2d(pool_size = c(2, 2)) %>%
    
    layer_flatten() %>%
    layer_dense(units = 128, activation = 'relu') %>%
    layer_dense(units = num_classes, activation = 'softmax')  # Adjust for number of classes

  model %>% compile(
    loss = 'categorical_crossentropy',
    optimizer = 'adam',
    metrics = c('accuracy')
  )
  
  return(model)
}

# Main function
main <- function() {
  # Set the path to your dataset
  train_data_dir <- "path/to/your/train_data"
  validation_data_dir <- "path/to/your/validation_data"

  # Load training and validation data
  train_data <- load_images(train_data_dir)
  validation_data <- load_images(validation_data_dir)

  # Build the model
  num_classes <- length(unique(train_data$classes))  # Get the number of classes
  model <- build_model(num_classes)

  # Train the model
  history <- model %>% fit(
    train_data,
    epochs = 10,  # Adjust the number of epochs as needed
    validation_data = validation_data,
    steps_per_epoch = train_data$n / train_data$batch_size
  )

  # Save the model
  model %>% save_model_hdf5("art_recognition_model.h5")

  # Load a new image for prediction (example)
  new_image_path <- "path/to/new/image.jpg"
  new_image <- image_load(new_image_path, target_size = c(150, 150))
  new_image <- image_to_array(new_image)
  new_image <- array_reshape(new_image, c(1, dim(new_image))) / 255

  # Make a prediction
  predictions <- model %>% predict(new_image)
  predicted_class <- which.max(predictions)
  
  # Print the predicted class
  print(paste("Predicted class:", predicted_class))
}

# Run the main function
main()
