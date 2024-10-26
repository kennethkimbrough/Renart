const { trainModel } = require('./model');

async function main() {
    try {
        console.log('Starting model training...');
        const model = await trainModel();
        console.log('Training completed successfully!');
    } catch (error) {
        console.error('Training failed:', error);
    }
}

main();
