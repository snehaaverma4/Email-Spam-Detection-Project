import streamlit as st
import joblib
import re
import string

# Load model and vectorizer
model = joblib.load("spam_model.pkl")

# No need to load vectorizer separately
cleaned = clean_text(input_email)
result = model.predict([cleaned])[0]


# Preprocessing function
def clean_text(text):
    text = text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    text = re.sub(r'\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Custom CSS styling
st.markdown("""
    <style>
    .stApp {
        background-color: #d2f5f9;
    }
    .block-container {
        background-color: #FEFAE0;
        padding-top: 4rem;
    }
    h1 {
        text-align: center;
        margin-top: 3rem;
        color: #2c3e50;
    }
    textarea {
        background-color: #f0f8ff !important;
        border: 1px solid #ccc !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }
    .stButton>button {
        background-color: #007BFF !important;
        color: white !important;
        border: none;
        border-radius: 8px;
        padding: 10px 24px;
    }
    </style>
""", unsafe_allow_html=True)

# Page config
st.set_page_config(page_title="Email Spam Classifier", layout="centered", page_icon="📧")

# Main heading
st.markdown("<h1>📧 Email Spam Classifier</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Paste your email below to check if it's spam.</p>", unsafe_allow_html=True)

# Input area
input_email = st.text_area("✉️ Email Content", height=200)

# Prediction button
if st.button("🚀 Predict"):
    cleaned = clean_text(input_email)
    vectorized = vectorizer.transform([cleaned])
    result = model.predict(vectorized)[0]
    
    st.markdown("---")
    if result == 1:
        st.markdown(
            "<div style='background-color:#ffdddd;padding:20px;border-radius:10px;'>"
            "<h3 style='color:#b30000;'>🚨 It's a SPAM email!</h3>"
            "</div>", unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<div style='background-color:#ddffdd;padding:20px;border-radius:10px;'>"
            "<h3 style='color:#006600;'>✅ It's a HAM (Not Spam) email!</h3>"
            "</div>", unsafe_allow_html=True
        )
