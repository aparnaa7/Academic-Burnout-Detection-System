from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# load trained model
model = pickle.load(open("burnout_model.pkl", "rb"))
encoder = pickle.load(open("label_encoder.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    study_hours = data["study_hours"]
    sleep_hours = data["sleep_hours"]
    stress_level = data["stress_level"]
    assignment_load = data["assignment_load"]
    attendance = data["attendance"]

    prediction = model.predict([[study_hours, sleep_hours, stress_level, assignment_load, attendance]])

    return jsonify({"burnout_level": prediction[0]})

@app.route("/")
def home():
    return "Burnout Prediction API is running"
if __name__ == "__main__":
    app.run(debug=True)
    