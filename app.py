import streamlit as st
import joblib

# Load the saved full pipeline
model_pipeline = joblib.load("spam_model.pkl")

# Streamlit UI
st.title("📧 Email Spam Classifier")
st.write("Enter the content of your email and find out if it's spam or not!")

input_email = st.text_area("✉️ Email Content")

if st.button("Predict"):
    prediction = model_pipeline.predict([input_email])[0]
    
    if prediction == 1:
        st.error("🚨 It's a SPAM email!")
    else:
        st.success("✅ It's a HAM (Not Spam) email!")

