from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables

import streamlit as st
import os
import google.generativeai as genai

# Configure GenAI Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Google Gemini Model and provide summarization
def summarize_text(description, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], description])
    return response.text.strip()

# Custom CSS for styling
st.markdown(
    """
    <style>
        /* Page Background */
        body {
            background-color: #1E1E1E;
            color: #E0E0E0;
            font-family: 'Roboto', sans-serif;
        }

        /* Header Styling */
        .main-header {
            font-size: 3rem;
            color: #BB86FC;
            text-align: center;
            margin-bottom: 1.5rem;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }

        /* Subheader Styling */
        .sub-header {
            font-size: 1.2rem;
            color: #03DAC6;
            margin-top: 1rem;
            text-align: center;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }

        /* Text Input Area */
        .stTextArea > div > div > textarea {
            background-color: #2C2C2C;
            color: #E0E0E0;
            border: 2px solid #BB86FC;
            border-radius: 10px;
            padding: 10px;
            font-size: 1rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        .stTextArea > div > div > textarea:focus {
            border-color: #03DAC6;
            box-shadow: 0 7px 14px rgba(0, 0, 0, 0.1);
        }

        /* Buttons */
        .stButton > button {
            background-color: #BB86FC;
            color: #1E1E1E;
            border-radius: 25px;
            padding: 0.75rem 2rem;
            font-size: 1rem;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
            transition: all 0.3s ease;
            border: none;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        .stButton > button:hover {
            background-color: #03DAC6;
            transform: translateY(-2px);
            box-shadow: 0 7px 14px rgba(0, 0, 0, 0.1);
        }

        /* Checkbox and Radio Buttons */
        .stRadio > label, .stCheckbox > label {
            font-size: 1rem;
            color: #E0E0E0;
        }
        .stRadio > div, .stCheckbox > div {
            margin-top: 0.5rem;
        }

        /* Summary Output */
        .summary-output {
            background-color: #2C2C2C;
            color: #E0E0E0;
            border-radius: 10px;
            padding: 1.5rem;
            margin-top: 2rem;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit App Header
st.markdown('<h1 class="main-header">🌟 Gemini Text Simplification Tool</h1>', unsafe_allow_html=True)

# Description Section
st.markdown('<p class="sub-header">Enter a detailed description, and we\'ll summarize it in simple terms based on your preferences.</p>', unsafe_allow_html=True)

description = st.text_area("Enter the description:", key="description", height=200)

# Simplicity level radio buttons
simplicity_levels = {
    "Very simple": "Use very basic and clear language, as if explaining to a child.",
    "Simple": "Use simple and clear language, avoiding technical terms.",
    "Moderate": "Use moderately simple language, suitable for a general audience."
}
simplicity_choice = st.radio("Choose the level of simplicity:", list(simplicity_levels.keys()))

# Additional options checkboxes
col1, col2 = st.columns(2)
with col1:
    include_examples = st.checkbox("Include examples in the summary")
with col2:
    focus_on_key_points = st.checkbox("Focus strictly on key points")

# Generate the prompt based on user choices
if description.strip():
    selected_simplicity = simplicity_levels[simplicity_choice]
    prompt = [
        f"""
        You are an expert in summarizing complex text. Your task is to summarize 
        the provided description. {selected_simplicity}
        """
    ]
    if include_examples:
        prompt[0] += " Include examples to clarify the summary where appropriate."
    if focus_on_key_points:
        prompt[0] += " Focus strictly on the key points and avoid unnecessary details."
else:
    prompt = []

# Submit Button
st.markdown("<div style='text-align: center;'>", unsafe_allow_html=True)
submit = st.button("✨ Summarize ✨")
st.markdown("</div>", unsafe_allow_html=True)

# Summary Output
if submit:
    if description.strip():
        summary = summarize_text(description, prompt)
        st.markdown("<div class='summary-output'>", unsafe_allow_html=True)
        st.subheader("Summary:")
        st.write(summary)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.error("Please enter a valid description to summarize.")