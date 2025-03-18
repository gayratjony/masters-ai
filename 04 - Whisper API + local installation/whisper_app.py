import streamlit as st
import whisper
import torch
import tempfile
import os

# Load Whisper model (small model for better performance)
@st.cache_resource
def load_model():
    return whisper.load_model("small")

model = load_model()

# Streamlit UI
st.title("🎙 Whisper AI - Speech-to-Text Transcription")
st.write("Upload an audio file and get instant transcription using OpenAI's Whisper model.")

# File uploader
uploaded_file = st.file_uploader("Upload an audio file (MP3, WAV, etc.)", type=["mp3", "wav", "m4a", "ogg"])

if uploaded_file is not None:
    st.audio(uploaded_file, format="audio")
    
    # Save uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[-1]) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_filepath = temp_file.name
    
    # Transcription
    st.write("Transcribing... Please wait ⏳")
    result = model.transcribe(temp_filepath)
    
    # Display transcription
    st.subheader("📝 Transcription:")
    st.text_area("", result["text"], height=200)
    
    # Clean up temporary file
    os.remove(temp_filepath)

st.write("---")
st.write("📜 This project is open-source. Feel free to contribute and enhance it! 🚀")
