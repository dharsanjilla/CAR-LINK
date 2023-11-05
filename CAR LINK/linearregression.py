import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


# Load the traffic data.
traffic_data = pd.read_csv("traffic_data.csv")

# Split the data into features and target.
features = traffic_data[["speed", "traffic_density"]]
target = traffic_data["travel_time"]

# Create the linear regression model.
model = LinearRegression()

# Train the model on the training data.
model.fit(features, target)

# Make predictions on the training data.
predictions = model.predict(features)

# Calculate the mean squared error (MSE).
mse = (predictions - target)**2.mean()

# Print the MSE.
print("MSE:", mse)

# Make predictions on new data.
new_features = [[60, 0.5]]
new_predictions = model.predict(new_features)

# Print the predictions.
print("Predicted travel time:", new_predictions)

def predict_travel_time(speed, traffic_density):
  """
  Predict travel time based on speed and traffic density.

  Args:
    speed: The speed of the car in mph.
    traffic_density: The traffic density in vehicles per square mile.

  Returns:
    The predicted travel time in minutes.
  """

  # Create the model input.
  input_features = [[speed, traffic_density]]

  # Make a prediction.
  prediction = model.predict(input_features)

  # Return the prediction.
  return prediction[0]

# Example usage:

speed = 60
traffic_density = 0.5

# Predict the travel time.
travel_time = predict_travel_time(speed, traffic_density)

# Print the predicted travel time.
print("Predicted travel time:", travel_time)
