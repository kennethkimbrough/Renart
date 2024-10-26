#' Convert RGB to HSL color space
#' @param r Red component (0-1)
#' @param g Green component (0-1)
#' @param b Blue component (0-1)
#' @return Vector of HSL values
rgb_to_hsl <- function(r, g, b) {
  cmax <- max(r, g, b)
  cmin <- min(r, g, b)
  delta <- cmax - cmin
  
  # Calculate hue
  h <- if(delta == 0) 0 else {
    if(cmax == r) {
      60 * (((g - b)/delta) %% 6)
    } else if(cmax == g) {
      60 * (((b - r)/delta) + 2)
    } else {
      60 * (((r - g)/delta) + 4)
    }
  }
  
  # Calculate lightness
  l <- (cmax + cmin)/2
  
  # Calculate saturation
  s <- if(delta == 0) 0 else {
    delta/(1 - abs(2 * l - 1))
  }
  
  return(c(h = h, s = s, l = l))
}

#' Save artwork with metadata
save_artwork <- function(artwork, filename, metadata = list()) {
  # Save the artwork
  save(artwork, file = filename)
  
  # Add metadata
  metadata$creation_date <- Sys.time()
  metadata$r_version <- R.version.string
  
  # Save metadata
  writeLines(
    jsonlite::toJSON(metadata, pretty = TRUE
