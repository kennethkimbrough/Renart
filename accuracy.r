# Plot training & validation accuracy values
plot(history) + 
  ggtitle("Model Accuracy") + 
  xlab("Epochs") + 
  ylab("Accuracy") + 
  theme_minimal()

# Plot training & validation loss values
plot(history) + 
  ggtitle("Model Loss") + 
  xlab("Epochs") + 
  ylab("Loss") + 
  theme_minimal()
