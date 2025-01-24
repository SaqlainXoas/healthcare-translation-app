# util.py

import asyncio
from googletrans import Translator
from elevenlabs.client import ElevenLabs
import streamlit as st

# Initialize Google Translator
translator = Translator()

# Initialize ElevenLabs client
api_key = st.secrets["ELEVENLABS_API_KEY"] 
client = ElevenLabs(api_key=api_key)

async def translate_text(text, input_language, output_language):
    """
    Translate text asynchronously using Google Translator.
    """
    return await translator.translate(text, src=input_language, dest=output_language)

def elevenlabs_tts(text, voice_model="21m00Tcm4TlvDq8ikWAM"):
    """
    Generate speech from text using ElevenLabs API.
    """
    try:
        audio_generator = client.generate(
            text=text,
            voice=voice_model,
            model="eleven_multilingual_v1"
        )
        audio_data = b''.join([chunk for chunk in audio_generator])
        return audio_data
    except Exception as e:
        st.error(f"Error generating speech: {e}")
        return None
