import streamlit as st
import joblib
import re
import string
import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Construct file path to the pipeline
model_path = os.path.join(script_dir, "spam_model.pkl")

# Load the entire pipeline (model + vectorizer)
try:
    pipeline = joblib.load(model_path)  # Load the pipeline
except FileNotFoundError:
    st.error("Error: Model file not found!")
    st.stop()
except Exception as e:
    st.error(f"An error occurred: {e}")
    st.stop()


# Preprocessing function (same as in training)
def clean_text(text):
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


# Streamlit UI
st.title("📧 Email Spam Classifier")
st.write("Enter the content of your email and find out if it's spam or not!")

input_email = st.text_area("✉️ Email Content")

if st.button("Predict"):
    cleaned_text = clean_text(input_email)
    prediction = pipeline.predict([cleaned_text])[0]  # Pipeline does vectorizing

    if prediction == 1:  # Assuming 1 represents spam
        st.error("🚨 It's a SPAM email!")
    else:
        st.success("✅ It's a HAM (Not Spam) email!")
