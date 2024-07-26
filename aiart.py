import streamlit as st
import requests
import os

# Path to static assets
css_path = os.path.join(os.path.dirname(__file__), 'static', 'css', 'style.css')
js_path = os.path.join(os.path.dirname(__file__), 'static', 'js', 'main.js')

# Load CSS
with open(css_path) as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load JS
with open(js_path) as f:
    st.markdown(f'<script>{f.read()}</script>', unsafe_allow_html=True)

# Streamlit app configuration
st.set_page_config(page_title="AI Art Maker", layout="wide")

# Title and description
st.title("AI Art Maker")
st.write("Enter a prompt to generate AI art. This app uses the RapidAPI for generating art based on your prompt.")

# Input prompt from the user
prompt = st.text_input("Enter your art prompt:", "A beautiful sunset over the mountains")

# API details
api_url = "https://yt-api.p.rapidapi.com/dl"
headers = {
    "X-Rapidapi-Key": "10b8ea539emsh303325ea16a546ep175db6jsn340dbef4f66a",
    "X-Rapidapi-Host": "yt-api.p.rapidapi.com"
}

# Function to call the API and generate art
def generate_art(prompt):
    response = requests.get(api_url, headers=headers, params={"id": prompt})
    if response.status_code == 200:
        return response.content
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
        return None

# Generate art button
if st.button("Generate Art"):
    with st.spinner("Generating art..."):
        art = generate_art(prompt)
        if art:
            st.image(art, caption="Generated Art", use_column_width=True)
        else:
            st.error("Failed to generate art. Please try again.")

# Footer
st.write("Powered by [RapidAPI](https://rapidapi.com/).")
