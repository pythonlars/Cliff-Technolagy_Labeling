# AI Motion Reconstruction Cliff-Technology

This project aims to reconstruct full-body motion using IMU sensor data from a mobile device. The application predicts the movement of the entire body based on sensor data from the right leg and a selected trick name.

## Components
- **Data Reading**: Parses and prepares sensor data for training.
- **Neural Network Model**: A deep neural network that predicts full-body motion.
- **Model Testing**: Tests the trained model using new input data.

## Usage
1. **Data Preparation**: Ensure all data files are in the `txtFiles` directory.
2. **Training**: Run `neural_network_model.py` to train the model.
3. **Testing**: Use `test_model.py` to test the predictions.

## Requirements
See `requirements.txt` for necessary libraries.

## Future Work
- Implement 3D visualization using the `export_to_3d` function.
