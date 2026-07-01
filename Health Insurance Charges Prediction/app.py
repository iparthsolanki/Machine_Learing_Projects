import streamlit as st
import pandas as pd
import numpy as np
import pickle

# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="Health Insurance Charges Prediction",
    page_icon="🏥",
    layout="wide"
)

# =====================================================
# Custom CSS
# =====================================================

st.markdown("""
<style>

.main{
    background-color:#f8f9fa;
}

h1{
    color:#0d6efd;
}

.stButton>button{

    background:#0d6efd;
    color:white;
    border-radius:12px;
    height:50px;
    width:100%;
    font-size:18px;
    font-weight:bold;
}

.stButton>button:hover{

    background:#084298;
    color:white;

}

div[data-testid="metric-container"]{

    border-radius:15px;
    padding:20px;
    background:#EEF5FF;
    border:2px solid #0d6efd;

}

</style>
""",unsafe_allow_html=True)

# =====================================================
# Load Model
# =====================================================

model = pickle.load(open("model.pkl","rb"))
scaler = pickle.load(open("scaler.pkl","rb"))
columns = pickle.load(open("columns.pkl","rb"))

# =====================================================
# Sidebar
# =====================================================

st.sidebar.title("🏥 Insurance ML Project")

st.sidebar.markdown("---")

st.sidebar.success("Machine Learning Project")

st.sidebar.write("Algorithm : Linear Regression")

st.sidebar.write("Accuracy : 98.97%")

st.sidebar.markdown("---")

st.sidebar.info("""
Developer

Parth Solanki
""")

st.sidebar.markdown("---")

st.sidebar.write("Made using")

st.sidebar.write("✅ Python")

st.sidebar.write("✅ Streamlit")

st.sidebar.write("✅ Scikit-Learn")

st.sidebar.write("✅ Pandas")

# =====================================================
# Title
# =====================================================

st.title("🏥 Health Insurance Charges Prediction")

st.write(
"""
Predict Health Insurance Charges using Machine Learning.
"""
)

st.markdown("---")

# =====================================================
# Input Columns
# =====================================================

left,right = st.columns(2)

# =====================================================
# Left Side
# =====================================================

with left:

    age = st.slider(
        "Age",
        18,
        65,
        25
    )

    gender = st.selectbox(
        "Gender",
        [
            "male",
            "female"
        ]
    )

    bmi = st.number_input(
        "BMI",
        min_value=15.0,
        max_value=35.0,
        value=24.5
    )

    children = st.slider(
        "Children",
        0,
        5,
        0
    )

    smoker = st.selectbox(
        "Smoker",
        [
            "yes",
            "no"
        ]
    )

    exercise_frequency = st.selectbox(

        "Exercise Frequency",

        [
            "Never",
            "Rarely",
            "Occasionally",
            "Frequently"
        ]

    )

# =====================================================
# Right Side
# =====================================================

with right:

    coverage_level = st.selectbox(

        "Coverage Level",

        [
            "Basic",
            "Standard",
            "Premium"
        ]

    )

    region = st.selectbox(

        "Region",

        [
            "northeast",
            "northwest",
            "southeast",
            "southwest"
        ]

    )

    medical_history = st.selectbox(

        "Medical History",

        [
            "Diabetes",
            "Heart disease",
            "High blood pressure",
            "Unknown"
        ]

    )

    family_medical_history = st.selectbox(

        "Family Medical History",

        [
            "Diabetes",
            "Heart disease",
            "High blood pressure",
            "Unknown"
        ]

    )

    occupation = st.selectbox(

        "Occupation",

        [
            "Blue collar",
            "White collar",
            "Student",
            "Unemployed"
        ]

    )

st.markdown("---")

predict = st.button("🚀 Predict Insurance Charges")


# =====================================================
# Prediction
# =====================================================

if predict:

    # Validation

    if bmi <= 0:

        st.error("BMI should be greater than 0.")

    elif age <= 0:

        st.error("Age should be greater than 0.")

    else:

        # ==========================
        # Label Encoding
        # ==========================

        gender = 1 if gender == "male" else 0

        smoker = 1 if smoker == "yes" else 0


        # ==========================
        # Mapping
        # ==========================

        exercise_map = {

            "Never":0,
            "Rarely":1,
            "Occasionally":2,
            "Frequently":3

        }

        coverage_map = {

            "Basic":0,
            "Standard":1,
            "Premium":2

        }

        exercise_frequency = exercise_map[exercise_frequency]

        coverage_level = coverage_map[coverage_level]


        # ==========================
        # Create Input DataFrame
        # ==========================

        input_df = pd.DataFrame({

            "age":[age],
            "gender":[gender],
            "bmi":[bmi],
            "children":[children],
            "smoker":[smoker],
            "exercise_frequency":[exercise_frequency],
            "coverage_level":[coverage_level],

            "region":[region],
            "medical_history":[medical_history],
            "family_medical_history":[family_medical_history],
            "occupation":[occupation]

        })


        # ==========================
        # One Hot Encoding
        # ==========================

        input_df = pd.get_dummies(

            input_df,

            columns=[

                "region",
                "medical_history",
                "family_medical_history",
                "occupation"

            ],

            drop_first=True

        )


        # ==========================
        # Add Missing Columns
        # ==========================

        for col in columns:

            if col not in input_df.columns:

                input_df[col] = 0


        # ==========================
        # Arrange Same Order
        # ==========================

        input_df = input_df[columns]


        # ==========================
        # Scaling
        # ==========================

        input_scaled = scaler.transform(input_df)


        # ==========================
        # Prediction
        # ==========================

        prediction = model.predict(input_scaled)

        predicted_charge = prediction[0]


        # ==========================
        # Output
        # ==========================

        st.markdown("---")

        st.success("Prediction Completed Successfully ✅")

        st.metric(

            label="💰 Estimated Insurance Charges",

            value=f"₹ {predicted_charge:,.2f}"

        )

        st.info(

            """
            📌 Prediction generated using Linear Regression Model.
            """

        )

        st.balloons()


# =====================================================
# Footer
# =====================================================

st.markdown("---")

st.markdown(
"""
<center>

Made with ❤️ using Python, Streamlit & Scikit-Learn

<br>

Developed by <b>Parth Solanki</b>

</center>
""",
unsafe_allow_html=True
)