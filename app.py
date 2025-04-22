import streamlit as st
import joblib
import re
import string
import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Construct file paths
model_path = os.path.join(script_dir, "spam_model.pkl")
vectorizer_path = os.path.join(script_dir, "tfidf_vectorizer.pkl")

# Load the model and vectorizer with error handling
try:
    model = joblib.load(model_path)
    vectorizer = joblib.load(vectorizer_path)
except FileNotFoundError:
    st.error("Error: Model or vectorizer files not found!")
    st.stop()
except Exception as e:
    st.error(f"An error occurred: {e}")
    st.stop()

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
