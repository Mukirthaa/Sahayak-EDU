import streamlit as st

st.title("Sahayak EDU - MVP")
st.write("AI Teaching Companion for Multi-Grade Classrooms")

# Add grade selection
grade = st.selectbox(
    "Select Grade:", 
    ["Grade 1", "Grade 2", "Grade 3", "Grade 4", "Grade 5", "Grade 6", "Grade 7", "Grade 8"]
)

# Add language selection  
language = st.selectbox(
    "Select Language:",
    ["English", "Tamil", "Hindi"]
)

# Teacher's request
prompt = st.text_input("Enter your teaching request (e.g., 'Explain water cycle')")

if st.button("Generate Content"):
    if prompt:
        st.write(f"**Grade:** {grade}")
        st.write(f"**Language:** {language}")
        st.write(f"**Your Request:** {prompt}")
        st.write("*AI content generation coming soon...*")
    else:
        st.warning("Please enter a teaching request")
