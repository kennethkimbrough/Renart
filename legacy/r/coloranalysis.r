#' Extract dominant colors from an image
#' @param img Image file path or matrix
#' @param n_colors Number of colors to extract
#' @return Vector of hex colors
extract_dominant_colors <- function(img, n_colors = 5) {
  require(imager)
  require(stats)
  
  # Load image if path provided
  if(is.character(img)) {
    img <- load.image(img)
  }
  
  # Convert to data frame
  img_df <- as.data.frame(img)
  
  # Perform k-means clustering
  kmeans_result <- kmeans(img_df[,c("value", "cc")], centers = n_colors)
  
  # Convert cluster centers to hex colors
  colors <- rgb(kmeans_result$centers[,1],
               kmeans_result$centers[,2],
               kmeans_result$centers[,3])
  
  return(colors)
}

#' Calculate color harmony score
#' @param colors Vector of hex colors
#' @return Numeric harmony score
calculate_color_harmony <- function(colors) {
  require(colorspace)
  
  # Convert to HSV
  hsv_colors <- t(sapply(colors, hex2HSV))
  
  # Calculate hue differences
  hue_diffs <- outer(hsv_colors[,1], hsv_colors[,1], `-`)
  hue_diffs <- abs(hue_diffs)
  hue_diffs[hue_diffs > 180] <- 360 - hue_diffs[hue_diffs > 180]
  
  # Calculate harmony score based on h
