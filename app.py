import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("spam_model.pkl")

# Page Configuration
st.set_page_config(
    page_title="Email Spam Detection",
    page_icon="📧",
    layout="centered"
)

# Title
st.title("📧 Email Spam Detection")
st.write("Enter the email details below and click **Predict**.")

st.divider()

# Input Fields
email_length = st.number_input(
    "Email Length",
    min_value=0,
    value=100
)

num_links = st.number_input(
    "Number of Links",
    min_value=0,
    value=0
)

num_special_chars = st.number_input(
    "Number of Special Characters",
    min_value=0,
    value=0
)

capital_words = st.number_input(
    "Capital Words",
    min_value=0,
    value=0
)

has_attachment = st.selectbox(
    "Has Attachment?",
    ["No", "Yes"]
)

attachment = 1 if has_attachment == "Yes" else 0

st.divider()

# Prediction Button
if st.button("Predict"):

    input_data = np.array([
        [
            email_length,
            num_links,
            num_special_chars,
            capital_words,
            attachment
        ]
    ])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("🚨 This Email is SPAM")
    else:
        st.success("✅ This Email is NOT SPAM")