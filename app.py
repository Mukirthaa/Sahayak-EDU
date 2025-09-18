import streamlit as st
st.title("Sahayak EDU-MVP")
st.write("Hello, teacher! This is a test page")
prompt=st.text_input("Enter a teaching request")
st.write("You entered:", prompt)
if st.button("Generate"):
    st.write("Coming soon...")