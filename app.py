import streamlit as st
import pickle
import numpy as np

st.set_page_config(layout="centered") # Set layout for better display
st.title("Linear Regression App")

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

x = st.number_input("Enter x value", value=0.0)

if st.button("Predict"):
    y = model.predict(np.array([[x]]))
    st.success(f"Predicted y = {y[0]:.2f}")

# Save the streamlit app to a file
