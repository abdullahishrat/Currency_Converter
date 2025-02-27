import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key securely
API_KEY = os.getenv("API_KEY")

# Page title and styling
st.set_page_config(page_title="Currency Converter", page_icon="💱", layout="centered")

# Custom styling
st.markdown(
    """
    <style>
        .main { text-align: center; }
        h1 { color: #1E88E5; font-size: 36px; }
        .stButton>button { background-color: #1E88E5; color: white; font-size: 16px; padding: 10px 20px; }
        .stSuccess { font-size: 20px; font-weight: bold; }
    </style>
    """,
    unsafe_allow_html=True
)

# Header with animation
st.markdown("<h1>💱 Currency Converter</h1>", unsafe_allow_html=True)
st.markdown('<iframe src="https://lottie.host/embed/d6bfb407-179b-43aa-831e-cc6dde35023b/aa8mZOqaE0.lottie" width="300" height="200"></iframe>', unsafe_allow_html=True)

# Currency selection
st.write("### Select Currencies:")
col1, col2 = st.columns(2)

with col1:
    curr1 = st.selectbox('From Currency:', ['EUR', 'USD', 'GBP'])

with col2:
    curr2 = st.selectbox('To Currency:', ['USD', 'EUR', 'GBP'])

# Currency Animation
st.markdown("<h3>💰 Selected Currency Animation:</h3>", unsafe_allow_html=True)
if curr1 == 'EUR':
    st.markdown('<iframe src="https://lottie.host/embed/606317bb-e13e-46e8-8f79-e96f8e91005c/h9YUpsYaPZ.lottie" width="250" height="200"></iframe>', unsafe_allow_html=True)
elif curr1 == 'USD':
    st.markdown('<iframe src="https://lottie.host/embed/201ecfed-235e-4e6a-9c4d-ff6ce1a90d5c/TjaCRmO875.lottie" width="250" height="200"></iframe>', unsafe_allow_html=True)
else:
    st.markdown('<iframe src="https://lottie.host/embed/f0a8aa69-b9d0-40fe-a83d-e20c60193dcc/0bMCIa8NqH.lottie" width="250" height="200"></iframe>', unsafe_allow_html=True)

# Convert Button
if st.button("🔄 Convert"):
    # Construct API URL
    url = f"https://api.exchangerate-api.com/v4/latest/{curr1}?apikey={API_KEY}"

    # Fetch exchange rate
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # Get exchange rate for selected currency
        if curr2 in data["rates"]:
            one_two = data["rates"][curr2]
            two_one = 1 / one_two  # Reverse rate

            st.markdown("<h3>💹 Conversion Rates:</h3>", unsafe_allow_html=True)
            col1, col2 = st.columns(2)
            with col1:
                st.success(f"1 {curr1} = {one_two:.2f} {curr2}")
            with col2:
                st.success(f"1 {curr2} = {two_one:.2f} {curr1}")
        else:
            st.error("❌ Exchange rate not available for selected currencies.")
    else:
        st.error("❌ Failed to retrieve exchange rate data. Please try again later.")
