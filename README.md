# Renart - Renaissance Art Classifier

Renart is a sophisticated machine learning model designed to authenticate and analyze Renaissance artwork. By analyzing image characteristics, it can identify artists, authenticate pieces, and provide detailed analysis of artistic elements such as brush strokes, creation period, and distinctive features. This tool aims to assist galleries, museums, and art experts in verifying artwork authenticity and discovering forgeries.

## 🎨 Features

- **Artist Identification**: Accurately identifies the artist based on their unique style and techniques
- **Artwork Authentication**: Helps detect potential forgeries by analyzing artistic elements
- **Detailed Analysis**: Provides comprehensive information about:
  - Brush stroke patterns
  - Creation period estimation
  - Material composition
  - Artistic techniques used
  - Historical context
- **High-Resolution Image Processing**: Supports detailed examination of high-resolution artwork images
- **Multi-Period Recognition**: Covers various Renaissance periods and artistic schools

## 🚀 Installation

### Prerequisites
- Node.js (v14 or higher)
- npm (v6 or higher)
- TensorFlow.js

## 📊 Model Architecture

Our model utilizes a deep convolutional neural network (CNN) architecture specifically trained on Renaissance artwork:

- Input Layer: 224x224x3 (RGB images)
- Multiple Convolutional Layers
- Dense Layers for Feature Extraction
- Softmax Output Layer for Artist Classification

## 🎯 Accuracy Metrics

- Artist Identification: 92% accuracy
- Period Classification: 89% accuracy
- Style Analysis: 87% accuracy

## 📚 Dataset

The model is trained on a comprehensive dataset including:
- Over 1000 Renaissance paintings
- Works from 50+ master artists
- Multiple artistic periods
- Various artistic techniques and styles

## 🛠️ Technical Requirements

- Node.js v14+
- RAM: 8GB minimum
- GPU: Recommended for faster processing
- Storage: 2GB minimum for model files

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## 🙏 Acknowledgments

- Wikicommons

## 📈 Future Developments

- Integration with AR/VR technologies
- Real-time analysis capabilities


