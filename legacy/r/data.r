# Load necessary library
library(magick)

# Set the main path for your project
main_path <- "path/to/your/Renart/data"

# Create directories for training data
dir.create(file.path(main_path, "train", "Renaissance"), recursive = TRUE)
dir.create(file.path(main_path, "train", "Baroque"), recursive = TRUE)
dir.create(file.path(main_path, "train", "Impressionism"), recursive = TRUE)

# Create directories for validation data
dir.create(file.path(main_path, "validation", "Renaissance"), recursive = TRUE)
dir.create(file.path(main_path, "validation", "Baroque"), recursive = TRUE)
dir.create(file.path(main_path, "validation", "Impressionism"), recursive = TRUE)

# Function to create synthetic images
create_synthetic_image <- function(class_name, index) {
  img <- image_blank(width = 150, height = 150, color = "white") %>%
    image_annotate(text = class_name, size = 20, location = "+10+10", color = "black")
  image_write(img, path = file.path(main_path, "train", class_name, paste0("image", index, ".jpg")), format = "jpg")
}

# Generate synthetic images for training data
for (class in c("Renaissance", "Baroque", "Impressionism")) {
  for (i in 1:10) {  # Generate 10 images for each class
    create_synthetic_image(class, i)
  }
}

# Generate synthetic images for validation data
for (class in c("Renaissance", "Baroque", "Impressionism")) {
  for (i in 1:5) {  # Generate 5 images for each class
    create_synthetic_image(class, i)
  }
}

cat("Synthetic dataset created successfully!\n")
