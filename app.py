import streamlit as st
import joblib
import re
import string

# Load the saved pipeline (not separate model and vectorizer)
model_pipeline = joblib.load("spam_model.pkl")  # Make sure you save the pipeline as 'spam_pipeline.pkl'

# Preprocessing function (optional if pipeline includes preprocessing)
def clean_text(text):
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Streamlit UI
st.title("📧 Email Spam Classifier")
st.write("Enter the content of your email and find out if it's spam or not!")

input_email = st.text_area("✉️ Email Content")

if st.button("Predict"):
    # No need for manual cleaning if the pipeline handles it
    # cleaned = clean_text(input_email)
    prediction = model_pipeline.predict([input_email])[0]
    
    if prediction == 1:
        st.error("🚨 It's a SPAM email!")
    else:
        st.success("✅ It's a HAM (Not Spam) email!")
