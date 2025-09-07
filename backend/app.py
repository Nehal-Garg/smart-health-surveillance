from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

app = Flask(__name__)
CORS(app)  # allow cross-origin requests (useful for frontend)

# Load trained model
model = joblib.load("ml/model.joblib")

@app.route("/")
def home():
    return {"message": "Smart Health Surveillance API is running 🚀"}

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        turbidity = data.get("turbidity")
        ph = data.get("ph")
        bacteria_count = data.get("bacteria_count")

        # Convert to dataframe for sklearn
        df = pd.DataFrame([[turbidity, ph, bacteria_count]],
                          columns=["turbidity", "ph", "bacteria_count"])

        prediction = model.predict(df)[0]

        return jsonify({
            "outbreak_risk": int(prediction)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
