import flask
from flask import request, render_template
from main import identify_car, give_traffic_insights

app = flask.Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
  if request.method == "POST":
    # Get the uploaded image.
    image_file = request.files["image"]

    # Read the image into a numpy array.
    image = np.array(Image.open(image_file))

    # Identify cars in the image.
    cars = identify_car(image)

    # Give traffic insights based on the car bounding boxes.
    traffic_insights = give_traffic_insights(cars)

    # Render the template with the traffic insights.
    return render_template("index.html", traffic_insights=traffic_insights)
  else:
    # Render the template without any traffic insights.
    return render_template("index.html", traffic_insights=None)

if __name__ == "__main__":
  app.run(debug=True)
