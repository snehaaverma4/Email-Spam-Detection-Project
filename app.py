import streamlit as st
import joblib
import re
import string

# Load the model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

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

# Change background color using HTML and CSS
st.markdown(
    """
    <style>
    body {
        background-color: #C5EFF3; /* Light gray background */
    }
    .stApp {
        background-color: #ffffff; /* White container background */
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1); /* Optional shadow */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

input_email = st.text_area("✉️ Email Content")

if st.button("Predict"):
    cleaned = clean_text(input_email)
    vectorized = vectorizer.transform([cleaned])
    result = model.predict(vectorized)[0]

    if result == 1:
        st.error("🚨 It's a SPAM email!")
    else:
        st.success("✅ It's a HAM (Not Spam) email!")
