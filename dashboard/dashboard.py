import streamlit as st
import requests

st.title("💧 Smart Health Surveillance Dashboard")
st.write("Enter water quality details to predict disease outbreak risk.")

# User inputs
turbidity = st.number_input("Turbidity", min_value=0.0, max_value=20.0, step=0.1)
ph = st.number_input("pH Level", min_value=0.0, max_value=14.0, step=0.1)
bacteria_count = st.number_input("Bacteria Count", min_value=0, max_value=10000, step=10)

if st.button("Predict"):
    # Send request to backend
    url = "http://127.0.0.1:5000/predict"
    payload = {
        "turbidity": turbidity,
        "ph": ph,
        "bacteria_count": bacteria_count
    }
    response = requests.post(url, json=payload)

    if response.status_code == 200:
        result = response.json()
        risk = result.get("outbreak_risk")

        if risk == 1:
            st.error("⚠️ High risk of disease outbreak detected!")
        else:
            st.success("✅ Water quality looks safe, no outbreak risk.")
    else:
        st.warning("Something went wrong with the backend.")
