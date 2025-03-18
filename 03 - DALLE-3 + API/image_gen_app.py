import streamlit as st
import openai
import os

# Set up OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define available artistic styles
ART_STYLES = [
    "Realistic",
    "Cartoon",
    "Cyberpunk",
    "Watercolor",
    "Sketch",
    "Pixel Art",
    "Fantasy",
    "Minimalist",
    "Oil Painting"
]

# Streamlit UI
st.title("🎨 AI Image Generator - Multiple Artistic Styles")
st.write("Generate AI-powered images in various styles using OpenAI's DALL·E.")

# User input prompt
prompt = st.text_input("Enter your text prompt:", placeholder="A cyberpunk city at night")

# Button to generate images
if st.button("Generate Images"):
    if prompt:
        st.write("Generating images... Please wait ⏳")
        
        # Generate images for each style
        for style in ART_STYLES:
            styled_prompt = f"{prompt} in {style} style"
            
            try:
                response = openai.Image.create(
                    prompt=styled_prompt,
                    n=1,
                    size="1024x1024"
                )
                image_url = response["data"][0]["url"]
                
                # Display image
                st.subheader(f"{style} Style")
                st.image(image_url, caption=f"{style} Style", use_column_width=True)
            
            except Exception as e:
                st.error(f"Error generating {style} image: {e}")
    else:
        st.warning("Please enter a text prompt.")

# Footer
st.write("---")
st.write("📜 This project is open-source. Feel free to modify and enhance it! 🚀")
