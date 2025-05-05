import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from Data_reading01 import load_training_data

# Load the model structure
model = Sequential()

# Define the model structure to match the trained model
input_shape = 3 * N + number_of_trick_names  # Adjust this based on your data
model.add(Dense(units=64, activation='relu', input_shape=(input_shape,)))
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=64, activation='relu'))
output_shape = 8 * 3 * N  # Adjust this based on your data
model.add(Dense(units=output_shape, activation='linear'))

# Load model weights
model.load_weights('dnn_body_model_weights.h5')

# Prepare input example (dummy data for illustration)
right_leg_gyro = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 0.0, 0.0, 0.0])  # Flattened
right_leg_accel = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 0.0, 0.0, 0.0])  # Flattened
trick_name_encoded = np.array([1, 0, 0])  # Example one-hot encoding

# Combine inputs
input_example = np.concatenate([trick_name_encoded, right_leg_gyro, right_leg_accel])
input_example = input_example.reshape(1, -1)  # Reshape for model input

# Predict full-body motion
predicted_output = model.predict(input_example)

# Reshape the flat output vector back into sensor blocks
predicted_blocks = predicted_output.reshape(8, 3, N)  # Adjust N based on your data

# Print predicted values
body_parts = ["left_leg_gyro", "left_leg_accel", "right_arm_gyro", "right_arm_accel",
              "left_arm_gyro", "left_arm_accel", "upper_body_gyro", "upper_body_accel"]

for i, part in enumerate(body_parts):
    print(f"{part}:")
    print(predicted_blocks[i])

# Placeholder for exporting to 3D
# def export_to_3d(predicted_blocks):
#     pass  # Implement 3D export logic here
