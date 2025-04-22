import streamlit as st
import joblib
import re
import string

# Load the model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Preprocessing function
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
    cleaned = clean_text(input_email)
    vectorized = vectorizer.transform([cleaned])
    result = model.predict(vectorized)[0]
    
    if result == 1:
        st.error("🚨 It's a SPAM email!")
    else:
        st.success("✅ It's a HAM (Not Spam) email!")
