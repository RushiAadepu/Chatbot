import streamlit as st
from langchain.llms import GooglePalm

# Set your Google API key
api_key = "AIzaSyBS8sGmcNxPNJKV_kYOnmACi-uFe_wSkEA"

# Initialize the model
llm = GooglePalm(google_api_key=api_key, temperature=0.7)

# Create the Streamlit app
st.title("AI-Powered Text Generation")

# Get user input
user_input = st.text_input("Enter your prompt:")

# Generate output when the button is pressed
if st.button("Generate Response"):
    response = llm(user_input)
    st.write("Response:")
    st.write(response)
