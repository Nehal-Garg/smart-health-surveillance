# train_model.py
# train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset (reports.csv should already be in ml/ folder)
data = pd.read_csv("ml/reports.csv")

# Features (X) and Labels (y)
X = data[["turbidity", "ph", "bacteria_count"]]
y = data["disease_outbreak"]

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
joblib.dump(model, "ml/model.joblib")

print("✅ Model trained and saved as ml/model.joblib")
