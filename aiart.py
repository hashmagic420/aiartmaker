import streamlit as st
import requests
import os

# Function to load CSS file
def load_css(file_name):
    if os.path.exists(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    else:
        st.error(f"CSS file '{file_name}' not found. Please ensure the file is in the correct directory.")

# Load CSS
css_path = 'style.css'  # Adjusted path based on provided structure
load_css(css_path)

# Function to create the AI Art Maker interface
def ai_art_maker():
    st.title("AI Art Maker")
    st.markdown("This app allows you to create AI-generated art. Enter a description and click 'Generate Art' to get started.")

    description = st.text_input("Enter a description for the AI art:")
    if st.button("Generate Art"):
        if description:
            st.write("Generating art...")
            # Call the API with the description
            response = requests.get(
                "https://yt-api.p.rapidapi.com/dl",
                headers={
                    "X-Rapidapi-Key": "10b8ea539emsh303325ea16a546ep175db6jsn340dbef4f66a",
                    "X-Rapidapi-Host": "yt-api.p.rapidapi.com",
                },
                params={"id": description}
            )

            if response.status_code == 200:
                st.image(response.json().get('url'))
            else:
                st.error("Error generating art. Please try again.")
        else:
            st.warning("Please enter a description.")

if __name__ == "__main__":
    ai_art_maker()
