import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from Data_reading01 import load_training_data

# Load training data
X, y = load_training_data()

# Define the model
model = Sequential()

# Input layer
input_shape = X.shape[1]
model.add(Dense(units=64, activation='relu', input_shape=(input_shape,)))

# Hidden layers
model.add(Dense(units=64, activation='relu'))
model.add(Dense(units=64, activation='relu'))

# Output layer
output_shape = y.shape[1]
model.add(Dense(units=output_shape, activation='linear'))

# Compile the model
model.compile(optimizer=Adam(), loss='mean_squared_error')

# Print model summary
model.summary()

# Train the model
history = model.fit(X, y, epochs=30, batch_size=16, validation_split=0.1, shuffle=True)

# Print loss and val_loss after each epoch
for epoch in range(len(history.history['loss'])):
    print(f"Epoch {epoch+1}/{len(history.history['loss'])}")
    print(f" - loss: {history.history['loss'][epoch]:.4f} - val_loss: {history.history['val_loss'][epoch]:.4f}")

# Print model weights for each layer
for layer in model.layers:
    weights = layer.get_weights()
    print(f"Layer: {layer.name} Weights: {weights}")

# Save model weights
model.save_weights('dnn_body_model_weights.h5')

# Load model weights (for future use)
# model.load_weights('dnn_body_model_weights.h5')
