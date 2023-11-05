function uploadImage() {
  // Get the uploaded image file.
  const file = document.querySelector('#image').files[0];

  // Create a FormData object.
  const formData = new FormData();

  // Append the image file to the FormData object.
  formData.append('image', file);

  // Make a POST request to the server.
  fetch('/', {
    method: 'POST',
    body: formData
  })
    .then(response => response.json())
    .then(trafficInsights => {
      // Display the traffic insights on the page.
      const trafficInsightsElement = document.querySelector('#traffic-insights');
      trafficInsightsElement.innerHTML = `
        <p>Number of cars: ${trafficInsights.numCars}</p>
        <p>Average speed: ${trafficInsights.avgSpeed} mph</p>
        <p>Traffic density: ${trafficInsights.trafficDensity} vehicles per square mile</p>
      `;
    });
}

// Attach the uploadImage() function to the "submit" event of the form.
document.querySelector('form').addEventListener('submit', uploadImage);

// Get the speed and traffic density from the user.
const speed = document.querySelector('#speed').value;
const trafficDensity = document.querySelector('#trafficDensity').value;

// Make a prediction using the linear regression model.
const travelTime = await predictTravelTime(speed, trafficDensity);

// Display the predicted travel time to the user.
document.querySelector('#travelTime').innerHTML = `Predicted travel time: ${travelTime} minutes`;
