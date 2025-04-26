import streamlit as st
import joblib

# Load the saved full pipeline
model_pipeline = joblib.load("spam_model.pkl")

# Custom CSS Styling (correct way for Streamlit)
st.markdown("""
    <style>
    /* Background color for the whole app */
    .stApp {
        background-color: #f0f2f6;
    }

    /* Title style */
    h1 {
        color: #2F4F4F;
        text-align: center;
        font-family: 'Arial';
    }

    /* Text input (textarea) style */
    textarea {
        border: 2px solid #6c63ff !important;
        border-radius: 10px !important;
    }

    /* Button style */
    div.stButton > button:first-child {
        background-color: #6c63ff;
        color: white;
        font-size: 16px;
        border-radius: 10px;
        height: 50px;
        width: 200px;
        margin-top: 10px;
    }
    
    div.stButton > button:hover {
        background-color: #5548c8;
        color: white;
    }

    /* Result message box styling */
    .stAlert {
        border-radius: 12px;
    }

    /* Add some padding to the page */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit App
st.title("📧 Email Spam Classifier")
st.markdown("---")
st.write("## Enter your email content below 👇")

input_email = st.text_area("✉️ Email Content", height=200)

if st.button("Predict"):
    prediction = model_pipeline.predict([input_email])[0]
    
    if prediction == 1:
        st.error("🚨 It's a SPAM email!")
    else:
        st.success("✅ It's a HAM (Not Spam) email!")
