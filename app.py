import streamlit as st
import joblib

# Load the saved full pipeline
model_pipeline = joblib.load("spam_model.pkl")

# Apply custom CSS
st.markdown(
    <style>
    /* Set background color */
    body {
        background-color: eeffd3;
    }
    
    # /* Center everything and add padding */
    # .main {
    #     padding-top: 50px;
    #     padding-left: 10px;
    #     padding-right: 10px;
    # }
    
    /* Title Styling */
    h1 {
        color: #2F4F4F;
        text-align: center;
        font-family: 'Arial';
        # font-size: 3em;
    }

    /* Text area styling */
    textarea {
        border-radius: 10px;
        border: 2px solid #6c63ff;
        padding: 10px;
        # font-size: 1em;
    }

    /* Button styling */
    div.stButton > button {
        background-color: #6c63ff;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin-top: 10px;
        border-radius: 12px;
        transition-duration: 0.4s;
        cursor: pointer;
    }
    
    div.stButton > button:hover {
        background-color: #5a54d1;
        color: white;
    }

    /* Message box (error/success) styling */
    .stAlert {
        border-radius: 12px;
        padding: 20px;
    }
    </style>
, unsafe_allow_html=True)

# Streamlit App UI
st.title("📧 Email Spam Classifier")
st.write("---")
st.write("## Enter your email content below 👇")

input_email = st.text_area("✉️ Email Content", height=200)

if st.button("Predict"):
    prediction = model_pipeline.predict([input_email])[0]
    
    if prediction == 1:
        st.error("🚨 It's a SPAM email!")
    else:
        st.success("✅ It's a HAM (Not Spam) email!")

