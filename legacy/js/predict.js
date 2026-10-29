const tf = require('@tensorflow/tfjs-node');
const { predictArtwork } = require('./model');

async function main() {
    try {
        // Load the saved model
        const model = await tf.loadLayersModel('file://./renaissance-art-model/model.json');
        
        // Make prediction on a test image
        const testImagePath = 'path/to/test/image.jpg';
        const prediction = await predictArtwork(model, testImagePath);
        console.log(`Predicted artist: ${prediction}`);
    } catch (error) {
        console.error('Prediction failed:', error);
    }
}

main();
