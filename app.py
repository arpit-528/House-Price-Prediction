from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("xgb_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route("/")
def home():
    return "House Price Prediction API is running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()  # Get JSON data
        features = np.array([list(data.values())]).reshape(1, -1)
        scaled_features = scaler.transform(features)  # Standardize input

        # model.predict(...) returns an array, so [0] is a single float
        prediction = model.predict(scaled_features)[0]

        # Convert float32 → standard Python float
        predicted_price = float(prediction)

        # Return JSON with a nicely rounded float
        return jsonify({"predicted_price": round(predicted_price, 2)})

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
