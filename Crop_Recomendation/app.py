import streamlit as st
import numpy as np
import pickle

# Load model and scaler
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# Title
st.title("🌱 Crop Recommendation System")

st.write("Enter the soil and weather details")

# Inputs
N = st.number_input("Nitrogen")
P = st.number_input("Phosphorus")
K = st.number_input("Potassium")
temperature = st.number_input("Temperature")
humidity = st.number_input("Humidity")
ph = st.number_input("pH")
rainfall = st.number_input("Rainfall")

# Prediction
if st.button("Predict Crop"):

    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    scaled_features = scaler.transform(features)

    prediction = model.predict(scaled_features)

    st.success(f"Recommended Crop: {prediction[0]}")
    
reverse_crop_dict = {
    1: "rice",
    2: "maize",
    3: "jute",
    4: "cotton",
    5: "coconut",
    6: "papaya",
    7: "orange",
    8: "apple",
    9: "muskmelon",
    10: "watermelon",
    11: "grapes",
    12: "mango",
    13: "banana",
    14: "pomegranate",
    15: "lentil",
    16: "blackgram",
    17: "mungbean",
    18: "mothbeans",
    19: "pigeonpeas",
    20: "kidneybeans",
    21: "chickpea",
    22: "coffee"
}

st.success(f"Recommended Crop: {reverse_crop_dict[prediction[0]]}")