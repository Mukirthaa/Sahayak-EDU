import os
from dotenv import load_dotenv  # loads .env
load_dotenv()  # reads GEMINI_API_KEY from .env [web:368][web:95]

import streamlit as st  # must import before using st.error [web:370]

# Read API key (do not print it)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # note the closing parenthesis [web:368]
if not GEMINI_API_KEY:
    st.error("GEMINI_API_KEY not set in .env")  # guardrail if key missing [web:361]

# Google GenAI SDK
from google import genai
client = genai.Client()  # uses the key from environment automatically [web:94][web:372]

st.title("Sahayak EDU - MVP")
st.write("AI Teaching Companion for Multi-Grade Classrooms")

# Grade selection
grade = st.selectbox(
    "Select Grade:",
    ["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8"]
)

# Language selection
language = st.selectbox(
    "Select Language:",
    ["English", "Tamil", "Hindi"]
)

# Teacher's request
prompt = st.text_input("Enter your teaching request (e.g., 'Explain water cycle')")

# Single button block (no nesting)
if st.button("Generate Content"):
    if prompt:
        st.write(f"**Grade:** {grade}")
        st.write(f"**Language:** {language}")
        st.write(f"**Your Request:** {prompt}")

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[f"Language: {language}. Grade: {grade}. Task: {prompt}"]
            )  # minimal text-generation call [web:94][web:369]
            st.write(response.text)  # print model output [web:94]
        except Exception as e:
            st.error(f"Error generating content: {e}")  # basic error surface [web:370]
    else:
        st.warning("Please enter a teaching request")  # input validation [web:370]
