const tf = require('@tensorflow/tfjs-node');
const fs = require('fs');
const path = require('path');
const artData = require('./renaissanceart.js');

// Get unique artists from the dataset
const uniqueArtists = [...new Set(artData.map(item => item.artist))];
const numClasses = uniqueArtists.length;

// Model configuration
const IMAGE_WIDTH = 224;
const IMAGE_HEIGHT = 224;
const CHANNELS = 3;

// Create the model architecture
function createModel() {
    const model = tf.sequential();

    // First Convolutional Layer
    model.add(tf.layers.conv2d({
        inputShape: [IMAGE_HEIGHT, IMAGE_WIDTH, CHANNELS],
        filters: 32,
        kernelSize: 3,
        activation: 'relu',
        padding: 'same'
    }));
    model.add(tf.layers.maxPooling2d({ poolSize: [2, 2] }));

    // Second Convolutional Layer
    model.add(tf.layers.conv2d({
        filters: 64,
        kernelSize: 3,
        activation: 'relu',
        padding: 'same'
    }));
    model.add(tf.layers.maxPooling2d({ poolSize: [2, 2] }));

    // Third Convolutional Layer
    model.add(tf.layers.conv2d({
        filters: 128,
        kernelSize: 3,
        activation: 'relu',
        padding: 'same'
    }));
    model.add(tf.layers.maxPooling2d({ poolSize: [2, 2] }));

    // Flatten the output
    model.add(tf.layers.flatten());

    // Dense layers
    model.add(tf.layers.dense({ units: 512, activation: 'relu' }));
    model.add(tf.layers.dropout({ rate: 0.5 }));
    model.add(tf.layers.dense({ units: numClasses, activation: 'softmax' }));

    return model;
}

// Image preprocessing function
async function loadAndPreprocessImage(imagePath) {
    try {
        const imageBuffer = fs.readFileSync(imagePath);
        const tfImage = tf.node.decodeImage(imageBuffer);
        
        // Resize image
        const resized = tf.image.resizeBilinear(tfImage, [IMAGE_HEIGHT, IMAGE_WIDTH]);
        
        // Normalize pixel values
        const normalized = resized.div(255.0);
        
        return normalized;
    } catch (error) {
        console.error(`Error loading image ${imagePath}:`, error);
        return null;
    }
}

// Prepare dataset
async function prepareDataset() {
    const images = [];
    const labels = [];

    for (const artwork of artData) {
        try {
            const image = await loadAndPreprocessImage(artwork.imagePath);
            if (image !== null) {
                images.push(image);
                
                // Convert artist name to index
                const artistIndex = uniqueArtists.indexOf(artwork.artist);
                labels.push(artistIndex);
            }
        } catch (error) {
            console.error(`Error processing artwork:`, error);
        }
    }

    // Convert to tensors
    const xs = tf.stack(images);
    const ys = tf.oneHot(labels, numClasses);

    return {
        xs,
        ys,
        numExamples: images.length
    };
}

// Train the model
async function trainModel() {
    try {
        // Prepare data
        const data = await prepareDataset();
        console.log('Dataset prepared:', data.numExamples, 'examples');

        // Create and compile model
        const model = createModel();
        model.compile({
            optimizer: tf.train.adam(0.0001),
            loss: 'categoricalCrossentropy',
            metrics: ['accuracy']
        });

        // Split data into training and validation sets
        const splitIndex = Math.floor(data.numExamples * 0.8);
        const trainXs = data.xs.slice([0], [splitIndex]);
        const trainYs = data.ys.slice([0], [splitIndex]);
        const valXs = data.xs.slice([splitIndex]);
        const valYs = data.ys.slice([splitIndex]);

        // Train the model
        await model.fit(trainXs, trainYs, {
            epochs: 50,
            batchSize: 32,
            validationData: [valXs, valYs],
            callbacks: {
                onEpochEnd: (epoch, logs) => {
                    console.log(
                        `Epoch ${epoch + 1}: ` +
                        `loss = ${logs.loss.toFixed(4)}, ` +
                        `accuracy = ${logs.acc.toFixed(4)}, ` +
                        `val_loss = ${logs.val_loss.toFixed(4)}, ` +
                        `val_acc = ${logs.val_acc.toFixed(4)}`
                    );
                }
            }
        });

        // Save the model
        await model.save('file://./renaissance-art-model');
        console.log('Model saved successfully');

        return model;
    } catch (error) {
        console.error('Error training model:', error);
        throw error;
    }
}

// Prediction function
async function predictArtwork(model, imagePath) {
    try {
        const image = await loadAndPreprocessImage(imagePath);
        const prediction = model.predict(image.expandDims(0));
        const artistIndex = prediction.argMax(-1).dataSync()[0];
        return uniqueArtists[artistIndex];
    } catch (error) {
        console.error('Error making prediction:', error);
        throw error;
    }
}

// Export functions
module.exports = {
    trainModel,
    predictArtwork,
    uniqueArtists
};
