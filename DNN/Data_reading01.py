import os
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Directory containing the data files
data_dir = 'c:/Users/User/OneDrive/Desktop/Labeling_system_Cliff/txtFiles/'

# Function to parse a single file
def parse_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Extracting data blocks
    trick_name = lines[2].split('=')[1].strip().strip('"')
    right_leg_gyro = np.array(eval(lines[5].split('=')[1].strip()))
    right_leg_accel = np.array(eval(lines[10].split('=')[1].strip()))
    
    # Extracting output blocks
    left_leg_gyro = np.array(eval(lines[15].split('=')[1].strip()))
    left_leg_accel = np.array(eval(lines[20].split('=')[1].strip()))
    # Add other blocks similarly...

    # Flatten the input and output arrays
    input_data = np.concatenate([right_leg_gyro.flatten(), right_leg_accel.flatten()])
    output_data = np.concatenate([left_leg_gyro.flatten(), left_leg_accel.flatten()])
    # Append other blocks to output_data...

    return trick_name, input_data, output_data

# Function to load all data
def load_data():
    input_data_list = []
    output_data_list = []
    trick_names = []

    for filename in os.listdir(data_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(data_dir, filename)
            trick_name, input_data, output_data = parse_file(file_path)
            trick_names.append(trick_name)
            input_data_list.append(input_data)
            output_data_list.append(output_data)

    # One-hot encode trick names
    encoder = OneHotEncoder(sparse=False)
    trick_names_encoded = encoder.fit_transform(np.array(trick_names).reshape(-1, 1))

    # Combine trick names with input data
    inputs = np.hstack([trick_names_encoded, input_data_list])
    outputs = np.array(output_data_list)

    return inputs, outputs

# Function to load training data
def load_training_data():
    input_data_list = []
    output_data_list = []
    trick_names = []

    for filename in os.listdir(data_dir):
        if filename.endswith('.txt'):
            file_path = os.path.join(data_dir, filename)
            trick_name, input_data, output_data = parse_file(file_path)
            trick_names.append(trick_name)
            input_data_list.append(input_data)
            output_data_list.append(output_data)

    # One-hot encode trick names
    encoder = OneHotEncoder(sparse=False)
    trick_names_encoded = encoder.fit_transform(np.array(trick_names).reshape(-1, 1))

    # Combine trick names with input data
    inputs = np.hstack([trick_names_encoded, input_data_list])
    outputs = np.array(output_data_list)

    return inputs, outputs

# Load the data
inputs, outputs = load_data()

# Print shapes to verify
print("Inputs shape:", inputs.shape)
print("Outputs shape:", outputs.shape)