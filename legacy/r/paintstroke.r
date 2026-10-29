#' Paint Stroke Evaluator and Generator
#' @description A collection of functions to create, evaluate, and manipulate digital paint strokes

#' Define a brush stroke class
#' @export
Brush <- R6::R6Class("Brush",
  public = list(
    #' @field size Brush size
    size = 1,
    #' @field opacity Brush opacity
    opacity = 1,
    #' @field color Brush color
    color = "#000000",
    #' @field pressure_sensitivity Brush pressure sensitivity
    pressure_sensitivity = TRUE,
    #' @field texture Brush texture pattern
    texture = NULL,
    
    #' @description Initialize a new brush
    #' @param size Brush size
    #' @param opacity Brush opacity
    #' @param color Brush color
    initialize = function(size = 1, opacity = 1, color = "#000000") {
      self$size <- size
      self$opacity <- opacity
      self$color <- color
    },
    
    #' @description Set brush texture
    #' @param texture_pattern Matrix representing texture pattern
    set_texture = function(texture_pattern) {
      self$texture <- texture_pattern
    }
  )
)

#' Stroke class for representing paint strokes
#' @export
Stroke <- R6::R6Class("Stroke",
  public = list(
    #' @field points List of points in the stroke
    points = list(),
    #' @field pressure List of pressure values
    pressure = list(),
    #' @field brush Associated brush object
    brush = NULL,
    
    #' @description Initialize a new stroke
    #' @param brush Brush object to use
    initialize = function(brush) {
      self$brush <- brush
    },
    
    #' @description Add a point to the stroke
    #' @param x X coordinate
    #' @param y Y coordinate
    #' @param pressure Pressure value
    add_point = function(x, y, pressure = 1) {
      self$points[[length(self$points) + 1]] <- c(x, y)
      self$pressure[[length(self$pressure) + 1]] <- pressure
    }
  )
)

#' Evaluate stroke characteristics
#' @param stroke Stroke object to evaluate
#' @return List of stroke characteristics
#' @export
evaluate_stroke <- function(stroke) {
  # Convert points to matrix for easier calculation
  points_matrix <- do.call(rbind, stroke$points)
  
  # Calculate stroke length
  stroke_length <- sum(sqrt(
    diff(points_matrix[,1])^2 + 
    diff(points_matrix[,2])^2
  ))
  
  # Calculate average pressure
  avg_pressure <- mean(unlist(stroke$pressure))
  
  # Calculate stroke curvature
  curvature <- calculate_curvature(points_matrix)
  
  # Calculate stroke speed (based on point spacing)
  point_spacing <- sqrt(
    diff(points_matrix[,1])^2 + 
    diff(points_matrix[,2])^2
  )
  stroke_speed <- mean(point_spacing)
  
  # Calculate stroke smoothness
  smoothness <- calculate_smoothness(points_matrix)
  
  return(list(
    length = stroke_length,
    avg_pressure = avg_pressure,
    curvature = curvature,
    speed = stroke_speed,
    smoothness = smoothness
  ))
}

#' Calculate curvature of a stroke
#' @param points Matrix of points
#' @return Average curvature value
calculate_curvature <- function(points) {
  if(nrow(points) < 3) return(0)
  
  # Calculate angles between consecutive segments
  angles <- sapply(2:(nrow(points)-1), function(i) {
    v1 <- points[i,] - points[i-1,]
    v2 <- points[i+1,] - points[i,]
    
    # Calculate angle between vectors
    dot_product <- sum(v1 * v2)
    norms <- sqrt(sum(v1^2)) * sqrt(sum(v2^2))
    
    acos(dot_product/norms)
  })
  
  return(mean(angles))
}

#' Calculate smoothness of a stroke
#' @param points Matrix of points
#' @return Smoothness score
calculate_smoothness <- function(points) {
  if(nrow(points) < 3) return(1)
  
  # Calculate second derivatives
  second_derivatives <- sapply(2:(nrow(points)-1), function(i) {
    (points[i+1,] - 2*points[i,] + points[i-1,])
  })
  
  # Smoothness is inverse of average second derivative magnitude
  smoothness <- 1 / (mean(sqrt(colSums(second_derivatives^2))) + 1e-6)
  
  return(smoothness)
}

#' Generate a synthetic brush stroke
#' @param brush Brush object to use
#' @param start_point Starting point coordinates
#' @param end_point Ending point coordinates
#' @param control_points Optional control points for curve
#' @return Stroke object
#' @export
generate_stroke <- function(brush, start_point, end_point, control_points = NULL) {
  stroke <- Stroke$new(brush)
  
  if(is.null(control_points)) {
    # Generate simple linear stroke
    t <- seq(0, 1, length.out = 50)
    points <- t(sapply(t, function(t) {
      start_point * (1-t) + end_point * t
    }))
  } else {
    # Generate Bezier curve stroke
    points <- generate_bezier_curve(start_point, end_point, control_points)
  }
  
  # Add points to stroke with varying pressure
  for(i in 1:nrow(points)) {
    # Simulate pressure variation
    pressure <- 0.5 + 0.5 * sin(pi * i/nrow(points))
    stroke$add_point(points[i,1], points[i,2], pressure)
  }
  
  return(stroke)
}

#' Generate points along a Bezier curve
#' @param start_point Starting point
#' @param end_point Ending point
#' @param control_points Control points
#' @return Matrix of points along the curve
generate_bezier_curve <- function(start_point, end_point, control_points) {
  t <- seq(0, 1, length.out = 50)
  
  points <- t(sapply(t, function(t) {
    # De Casteljau's algorithm
    points <- rbind(start_point, control_points, end_point)
    n <- nrow(points)
    
    while(n > 1) {
      for(i in 1:(n-1)) {
        points[i,] <- (1-t) * points[i,] + t * points[i+1,]
      }
      n <- n - 1
    }
    
    points[1,]
  }))
  
  return(points)
}

#' Render a stroke to a canvas
#' @param stroke Stroke object
#' @param canvas Existing canvas or dimensions
#' @return Updated canvas
#' @export
render_stroke <- function(stroke, canvas) {
  if(is.numeric(canvas)) {
    # Create new canvas with specified dimensions
    canvas <- matrix(1, nrow = canvas[1], ncol = canvas[2])
  }
  
  # Convert points to pixel coordinates
  points <- do.call(rbind, stroke$points)
  points <- round(points)
  
  # Apply brush to each point
  for(i in 1:nrow(points)) {
    x <- points[i,1]
    y <- points[i,2]
    pressure <- stroke$pressure[[i]]
    
    # Calculate brush size based on pressure
    if(stroke$brush$pressure_sensitivity) {
      current_size <- stroke$brush$size * pressure
    } else {
      current_size <- stroke$brush$size

    # Apply brush texture if available
    if(!is.null(stroke$brush$texture)) {
      brush_mask <- scale_texture(stroke$brush$texture, current_size)
    } else {
      brush_mask <- create_circular_brush(current_size)
    }
    
    # Apply brush to canvas
    x_range <- (x - floor(current_size/2)):(x + floor(current_size/2))
    y_range <- (y - floor(current_size/2)):(y + floor(current_size/2))
    
    # Clip to canvas boundaries
    x_range <- x_range[x_range > 0 & x_range <= ncol(canvas)]
    y_range <- y_range[y_range > 0 & y_range <= nrow(canvas)]
    
    if(length(x_range) > 0 && length(y_range) > 0) {
      canvas[y_range, x_range] <- blend_colors(
        canvas[y_range, x_range],
        stroke$brush$color,
        brush_mask * stroke$brush$opacity * pressure
      )
    }
  }
  
  return(canvas)
}

#' Create a circular brush mask
#' @param size Brush size
#' @return Matrix representing brush mask
create_circular_brush <- function(size) {
  grid <- expand.grid(
    x = seq(-1, 1, length.out = size),
    y = seq(-1, 1, length.out = size)
  )
  
  distances <- sqrt(grid$x^2 + grid$y^2)
  mask <- matrix(1 - distances, size, size)
  mask[mask < 0] <- 0
  
  return(mask)
}

#' Scale texture to desired size
#' @param texture Original texture matrix
#' @param size Desired size
#' @return Scaled texture matrix
scale_texture <- function(texture, size) {
  require(imager)
  
  # Convert to cimg object
  texture_img <- as.cimg(texture)
  
  # Resize
  scaled <- resize(texture_img, size, size)
  
  # Convert back to matrix
  return(as.matrix(scaled))
}

#' Blend colors using alpha compositing
#' @param bottom Bottom color(s)
#' @param top Top color
#' @param alpha Alpha values
#' @return Blended colors
blend_colors <- function(bottom, top, alpha) {
  # Convert colors to RGB
  bottom_rgb <- col2rgb(bottom)/255
  top_rgb <- col2rgb(top)/255
  
  # Blend
  blended <- bottom_rgb * (1 - alpha) + top_rgb * alpha
  
  # Convert back to color strings
  rgb(blended[1,], blended[2,], blended[3,])
}

#' Stroke Analysis Tools
#' @description Functions for analyzing stroke characteristics and patterns

#' Analyze stroke dynamics
#' @param stroke Stroke object
#' @return List of dynamic characteristics
#' @export
analyze_stroke_dynamics <- function(stroke) {
  points <- do.call(rbind, stroke$points)
  pressures <- unlist(stroke$pressure)
  
  # Calculate velocity
  velocities <- sqrt(
    diff(points[,1])^2 + 
    diff(points[,2])^2
  )
  
  # Calculate acceleration
  accelerations <- diff(velocities)
  
  # Calculate jerk (rate of change of acceleration)
  jerk <- diff(accelerations)
  
  # Analyze pressure patterns
  pressure_changes <- diff(pressures)
  
  return(list(
    mean_velocity = mean(velocities),
    max_velocity = max(velocities),
    mean_acceleration = mean(accelerations),
    mean_jerk = mean(jerk),
    pressure_variance = var(pressures),
    pressure_changes = pressure_changes
  ))
}

#' Calculate stroke complexity
#' @param stroke Stroke object
#' @return Complexity score
#' @export
calculate_stroke_complexity <- function(stroke) {
  points <- do.call(rbind, stroke$points)
  
  # Direction changes
  directions <- atan2(
    diff(points[,2]),
    diff(points[,1])
  )
  direction_changes <- abs(diff(directions))
  
  # Calculate complexity metrics
  complexity <- list(
    direction_changes = sum(direction_changes),
    point_density = nrow(points) / stroke_length(stroke),
    pressure_complexity = pressure_complexity(stroke$pressure)
  )
  
  # Combine metrics into single score
  score <- mean(c(
    normalize(complexity$direction_changes),
    normalize(complexity$point_density),
    normalize(complexity$pressure_complexity)
  ))
  
  return(score)
}

#' Helper function to calculate stroke length
#' @param stroke Stroke object
#' @return Stroke length
stroke_length <- function(stroke) {
  points <- do.call(rbind, stroke$points)
  sum(sqrt(
    diff(points[,1])^2 + 
    diff(points[,2])^2
  ))
}

#' Calculate pressure complexity
#' @param pressures List of pressure values
#' @return Pressure complexity score
pressure_complexity <- function(pressures) {
  pressures <- unlist(pressures)
  
  # Calculate entropy of pressure values
  breaks <- seq(min(pressures), max(pressures), length.out = 10)
  hist_data <- hist(pressures, breaks = breaks, plot = FALSE)
  probs <- hist_data$counts / sum(hist_data$counts)
  probs <- probs[probs > 0]
  
  entropy <- -sum(probs * log2(probs))
  return(entropy)
}

#' Normalize values to 0-1 range
#' @param x Numeric vector
#' @return Normalized vector
normalize <- function(x) {
  (x - min(x)) / (max(x) - min(x))
}

#' Compare two strokes for similarity
#' @param stroke1 First stroke object
#' @param stroke2 Second stroke object
#' @return Similarity score
#' @export
compare_strokes <- function(stroke1, stroke2) {
  # Get characteristics of both strokes
  char1 <- evaluate_stroke(stroke1)
  char2 <- evaluate_stroke(stroke2)
  
  # Calculate similarity metrics
  length_sim <- 1 - abs(char1$length - char2$length) / max(char1$length, char2$length)
  pressure_sim <- 1 - abs(char1$avg_pressure - char2$avg_pressure)
  curvature_sim <- 1 - abs(char1$curvature - char2$curvature) / max(char1$curvature, char2$curvature)
  speed_sim <- 1 - abs(char1$speed - char2$speed) / max(char1$speed, char2$speed)
  smoothness_sim <- 1 - abs(char1$smoothness - char2$smoothness)
  
  # Weighted average of similarities
  similarity <- mean(c(
    length_sim * 0.2,
    pressure_sim * 0.2,
    curvature_sim * 0.2,
    speed_sim * 0.2,
    smoothness_sim * 0.2
  ))
  
  return(similarity)
}
