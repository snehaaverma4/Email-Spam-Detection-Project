import streamlit as st
import joblib

# Load the saved full pipeline
model_pipeline = joblib.load("spam_model.pkl")

# Custom CSS Styling
st.markdown("""
    <style>
    /* 🔵 Overall App Background */
    .stApp {
        background-color: #ebf8ff;
    }

    /* 🟣 Title (h1) Styling */
    h1 {
        color: #000000; /* Black */
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 36px; /* Title size */
    }

    # /* 🟣 Subheading (h2) Styling */
    # h3 {
    #     color: #333333;
    #     text-align: left;
    #     font-family: 'Arial', sans-serif;
    #     font-size: 14px; /* Smaller size for second heading */
    }

    /* 🟢 Textarea (Input Box) Styling */
    textarea {
        border: 2px solid #004669 !important; /* margenta border */
        border-radius: 8px !important; /* Slightly round corners */
        padding: 10px;
        font-size: 16px;
        height: 100px !important; /* Make input box smaller */
    }

    /* 🟠 Button Styling */
    div.stButton > button:first-child {
        background-color: #005a87; /* pink background */
        color: white;
        font-size: 14px; /* Make text slightly smaller */
        border-radius: 8px;
        height: 40px;
        width: 130px;
        margin-top: 10px;
        border: none;
    }

    /* 🟠 Button Hover Styling */
    div.stButton > button:first-child:hover {
        background-color: #45a049; /* Slightly darker green on hover */
        color: white;
    }

    /* 🟡 Result message (error/success) box */
    .stAlert {
        border-radius: 10px;
        padding: 20px;
    }

    /* 🔵 Padding around whole page */
    .block-container {
        padding-top: 4rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit App UI
st.title("📧 Email Spam Classifier")
st.markdown("     ")

# Smaller second heading
st.markdown("""
    <h2 style='text-align: centre; font-size: 21px, color: #333333;'>Enter your email content below👇🏻</h2>
""", unsafe_allow_html=True)


# Textarea
input_email = st.text_area("✉️ Email Content")

# Button
if st.button("Predict"):
    # 🛡️ PROPER EMPTY CHECK
    if not input_email.strip():
        st.warning("⚠️ Please enter some text before predicting.")
    else:
        prediction = model_pipeline.predict([input_email])[0]
        
        if prediction == 1:
            st.error("🚨 It's a SPAM email!")
        else:
            st.success("✅ It's a HAM (Not Spam) email!")
