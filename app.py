import streamlit as st
import pickle
import numpy as np

# Page configuration
st.set_page_config(layout="centered")

# App title
st.title("Linear Regression App")

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# User input
x = st.number_input("Enter x value", value=0.0)

# Prediction
if st.button("Predict"):
    y = model.predict(np.array([[x]]))
    st.success(f"Predicted y = {y[0]:.2f}")
