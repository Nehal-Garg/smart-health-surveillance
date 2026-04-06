# Smart Health Surveillance

A machine learning system that predicts disease outbreak risk based on water quality data. It consists of a trained Random Forest model, a Flask REST API backend, and a Streamlit dashboard for real-time predictions.

## Project Structure

```
├── backend/
│   └── app.py          # Flask API server
├── dashboard/
│   └── dashboard.py    # Streamlit frontend
├── ml/
│   ├── train_model.py  # Model training script
│   ├── model.joblib    # Trained model (generated)
│   └── reports.csv     # Training dataset
└── requirements.txt
```

## How It Works

The model takes three water quality inputs and predicts whether there is a disease outbreak risk:

- Turbidity
- pH level
- Bacteria count

## Setup

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Train the model (skip if `ml/model.joblib` already exists):

```bash
python ml/train_model.py
```

3. Start the Flask backend:

```bash
python backend/app.py
```

4. In a separate terminal, launch the dashboard:

```bash
streamlit run dashboard/dashboard.py
```

Then open the Streamlit URL shown in your terminal (usually `http://localhost:8501`).

## API

`POST /predict`

Request body:
```json
{
  "turbidity": 3.5,
  "ph": 7.2,
  "bacteria_count": 150
}
```

Response:
```json
{
  "outbreak_risk": 0
}
```

`outbreak_risk` is `1` (high risk) or `0` (safe).

## Tech Stack

- Python, scikit-learn (Random Forest)
- Flask + Flask-CORS
- Streamlit
- pandas, joblib
