import cv2
import numpy as np
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the car classifier model.
car_classifier = cv2.CascadeClassifier('cars.xml')

def identify_car(image):
  """
  Identify a car in an image.

  Args:
    image: A numpy array representing the image.

  Returns:
    A list of bounding boxes around the cars in the image.
  """

  # Convert the image to grayscale.
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Detect cars in the image.
  cars = car_classifier.detectMultiScale(gray_image, 1.1, 3)

  # Return a list of bounding boxes around the cars.
  return cars

def give_traffic_insights(cars):
  """
  Give traffic insights based on a list of car bounding boxes.

  Args:
    cars: A list of bounding boxes around the cars in an image.

  Returns:
    A dictionary containing traffic insights.
  """

  # Calculate the number of cars in the image.
  num_cars = len(cars)

  # Calculate the average speed of the cars.
  avg_speed = 0.0
  for car in cars:
    avg_speed += car[4]
  avg_speed /= num_cars

  # Calculate the traffic density.
  traffic_density = num_cars / (image.shape[0] * image.shape[1])

  # Return a dictionary containing traffic insights.
  return {
    "numCars": num_cars,
    "avgSpeed": avg_speed,
    "trafficDensity": traffic_density
  }

@app.route("/identify-car", methods=["POST"])
def identify_car_api():
  """
  Identify cars in an image.

  Args:
    None.

  Returns:
    A JSON object containing the bounding boxes around the cars in the image.
  """

  # Get the uploaded image file.
  image_file = request.files["image"]

  # Read the image into a numpy array.
  image = np.array(Image.open(image_file))

  # Identify cars in the image.
  cars = identify_car(image)

  # Convert the bounding boxes to JSON.
  json_boxes = []
  for car in cars:
    json_boxes.append({
      "x": car[0],
      "y": car[1],
      "width": car[2],
      "height": car[3]
    })

  # Return the JSON object.
  return jsonify(json_boxes)

@app.route("/give-traffic-insights", methods=["POST"])
def give_traffic_insights_api():
  """
  Give traffic insights based on a list of car bounding boxes.

  Args:
    None.

  Returns:
    A JSON object containing the traffic insights.
  """

  # Get the car bounding boxes from the request body.
  cars = request.json["cars"]

  # Give traffic insights based on the car bounding boxes.
  traffic_insights = give_traffic_insights(cars)

  # Return the JSON object.
  return jsonify(traffic_insights)

if __name__ == "__main__":
  app.run(debug=True)
