import streamlit as st
import requests

# Prepare API key and API url
api_key = "5NkWNgF1iHqRT1qv4ekt7bvKmY0Zvg0NZ6vdgbUE"
url = "https://api.nasa.gov/planetary/apod?" \
      f"api_key={api_key}"

# Get the request data as dictionary
response_url = requests.get(url)
content = response_url.json()

# Extract the image, title, url and explanation
title = content["title"]
image_url = content["url"]
explanation = content["explanation"]

# Download the image
image_to_download = "img.png"
response_image = requests.get(image_url)
with open(image_to_download, "wb") as file:
    file.write(response_image.content)

st.title(title)
st.image(image_url)
st.write(explanation)
