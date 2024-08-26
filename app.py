import streamlit as st
import json
from model import probe_model_5l_profit  # Import the function from model.py

# Streamlit app
st.title("Financial Data Analysis")

# File upload
uploaded_file = st.file_uploader("Upload your data.json file", type="json")

if uploaded_file is not None:
    # Read the uploaded file
    data = json.load(uploaded_file)
    
    # Process the data using the imported function
    result = probe_model_5l_profit(data["data"])
    
    # Display the result
    st.write("Analysis Results:")
    st.json(result)
