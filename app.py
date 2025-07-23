import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Birthday Message Creator (Streamlit)")

# Read the content of your index.html file
# Make sure index.html is in the same directory as app.py
try:
    with open(r"C:\Users\mvign\OneDrive\Desktop\Birthday_message_generator\index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
except FileNotFoundError:
    st.error("Error: index.html not found. Please make sure 'index.html' is in the same directory as 'app.py'.")
    st.stop()

st.title("🎂 Birthday Message Creator")
st.write("This Streamlit app embeds your interactive HTML birthday card creator.")


# Embed the HTML content using Streamlit Components
# You might need to adjust the height to fit your content
# The 'scrolling=True' might be helpful if the content is taller than the height
components.html(
    html_content,
    height=1200,  # Adjust this height as needed to show your full app
    scrolling=True
)

st.markdown("---")
st.write("Built with Streamlit and your custom HTML/React template.")