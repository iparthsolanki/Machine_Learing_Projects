import streamlit as st
import numpy as np
import pickle

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Diabetes Prediction System",
    page_icon="🩺",
    layout="wide"
)

# ----------------------------
# Load Model
# ----------------------------
model = pickle.load(open("best_rf.pkl", "rb"))

# ----------------------------
# Title
# ----------------------------
st.title("🩺 Diabetes Prediction System")
st.write("Enter the patient's medical details to predict diabetes.")

st.sidebar.header("Patient Details")

# ----------------------------
# Inputs
# ----------------------------

age = st.sidebar.number_input("Age", 18, 100, 35)

physical_activity = st.sidebar.number_input(
    "Physical Activity (minutes/week)",
    0,
    1000,
    150
)

diet_score = st.sidebar.slider(
    "Diet Score",
    1.0,
    10.0,
    5.0
)

sleep = st.sidebar.number_input(
    "Sleep Hours",
    1.0,
    15.0,
    7.0
)

family_history = st.sidebar.selectbox(
    "Family History of Diabetes",
    [0,1]
)

hypertension = st.sidebar.selectbox(
    "Hypertension History",
    [0,1]
)

cardiovascular = st.sidebar.selectbox(
    "Cardiovascular History",
    [0,1]
)

bmi = st.sidebar.number_input(
    "BMI",
    10.0,
    60.0,
    25.0
)

waist = st.sidebar.number_input(
    "Waist to Hip Ratio",
    0.50,
    1.20,
    0.85
)

systolic = st.sidebar.number_input(
    "Systolic BP",
    80,
    220,
    120
)

diastolic = st.sidebar.number_input(
    "Diastolic BP",
    40,
    140,
    80
)

cholesterol = st.sidebar.number_input(
    "Total Cholesterol",
    100,
    400,
    180
)

hdl = st.sidebar.number_input(
    "HDL Cholesterol",
    20,
    120,
    55
)

ldl = st.sidebar.number_input(
    "LDL Cholesterol",
    50,
    300,
    100
)

triglycerides = st.sidebar.number_input(
    "Triglycerides",
    50,
    500,
    150
)

fasting = st.sidebar.number_input(
    "Fasting Glucose",
    50,
    300,
    95
)

post = st.sidebar.number_input(
    "Postprandial Glucose",
    70,
    400,
    140
)

insulin = st.sidebar.number_input(
    "Insulin Level",
    0.0,
    100.0,
    15.0
)

hba1c = st.sidebar.number_input(
    "HbA1c",
    3.0,
    15.0,
    5.5
)

# ----------------------------
# Prediction
# ----------------------------

if st.sidebar.button("Predict Diabetes"):

    data = np.array([[
        age,
        physical_activity,
        diet_score,
        sleep,
        family_history,
        hypertension,
        cardiovascular,
        bmi,
        waist,
        systolic,
        diastolic,
        cholesterol,
        hdl,
        ldl,
        triglycerides,
        fasting,
        post,
        insulin,
        hba1c
    ]])

    prediction = model.predict(data)[0]

    probability = model.predict_proba(data)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.error("⚠️ Diabetic Patient")
    else:
        st.success("✅ Non-Diabetic Patient")

    st.metric(
        "Diabetes Probability",
        f"{probability*100:.2f}%"
    )

    st.subheader("Risk Level")

    if probability < 0.30:
        st.success("🟢 Low Risk")

    elif probability < 0.70:
        st.warning("🟡 Medium Risk")

    else:
        st.error("🔴 High Risk")