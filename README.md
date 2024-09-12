Placement Prediction App
This project is a Flask-based web application that predicts placement outcomes using a pre-trained Random Forest machine learning model. The app takes user input from an HTML form, processes the data, and returns a prediction indicating whether a candidate is "Placed" or "Not Placed."

Features:
Flask Framework: Backend built with Flask to handle requests and render HTML templates.
Random Forest Model: Utilizes a pre-trained Random Forest model (stored in model.pkl) for predictions.
User Input: Accepts form inputs for prediction.
Web Interface: Displays results on a user-friendly HTML page.
How it works:
Load the pre-trained Random Forest model using pickle.
Accept input data via a form.
Process the input and make predictions using the model.
Display the prediction result on the webpage.
