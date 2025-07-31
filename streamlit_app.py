
import streamlit as st
import numpy as np
import pickle

with open('rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title("💰 Medical Insurance Cost Predictor")
st.write("Enter patient details to predict insurance charges.")

# User input
age = st.slider("Age", 18, 100, 30)
sex = st.selectbox("Sex", ['Male', 'Female'])
bmi = st.number_input("BMI", value=25.0)
children = st.number_input("Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", ['Yes', 'No'])
region = st.selectbox("Region", ['northeast', 'northwest', 'southeast', 'southwest'])

# Encode inputs
sex_val = 1 if sex == 'Male' else 0
smoker_val = 1 if smoker == 'Yes' else 0
region_val = {'northeast': 0, 'northwest': 1, 'southeast': 2, 'southwest': 3}[region]

input_data = np.array([age, sex_val, bmi, children, smoker_val, region_val]).reshape(1, -1)

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Insurance Cost: **${prediction[0]:,.2f}**")
