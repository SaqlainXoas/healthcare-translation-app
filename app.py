# app.py

import io
import openai
import streamlit as st
from io import BytesIO
from util import translate_text, elevenlabs_tts  
import asyncio  

# Set page configuration
st.set_page_config(
    page_title='Real Time Translation Healthcare',
    page_icon='🌎',
    layout='centered',
    initial_sidebar_state='auto'
)

# Hide Streamlit footer
st.markdown(
    """
    <style>
        footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True,
)

def main():
    st.header('Real Time Translation Healthcare')
    st.caption('Enabling real-time, multilingual communication in healthcare.')

    # Set OpenAI API key
    openai.api_key = st.secrets["OPENAI_API_KEY"]

    # Language selection
    st.markdown("### Language Selection")
    input_language = st.selectbox("Select Input Language", ["en", "ur", "hi", "es", "fr"], index=0)
    output_language = st.selectbox("Select Output Language", ["en", "ur", "hi", "es", "fr"], index=1)

    # Real-time audio input using Streamlit
    st.markdown("### Record Your Message")
    audio_bytes = st.experimental_audio_input("Record a voice message")
    
    if audio_bytes:
        st.audio(audio_bytes)
        st.session_state.audio_bytes = audio_bytes

    with st.form('input_form'):
        submit_button = st.form_submit_button(label='Translate', type='primary')
        
        if submit_button and 'audio_bytes' in st.session_state:
            try:
                audio_file = io.BytesIO(st.session_state.audio_bytes.getvalue())
                audio_file.seek(0)
                audio_file.name = "temp_audio.wav"

                # Transcribe audio using OpenAI Whisper
                transcript_response = openai.Audio.translate("whisper-1", audio_file)
                original_text = transcript_response['text']

                st.markdown("#### Original Transcript")
                st.text_area("Original Transcript", value=original_text, label_visibility='collapsed')

                # Translate text
                try:
                    translated_text = asyncio.run(translate_text(original_text, 'en', output_language))
                except Exception as e:
                    st.error(f"Error during translation: {e}")
                    return

                st.markdown(f"#### Translated Transcript ({output_language})")
                st.text_area("Translated Transcript", value=translated_text.text, label_visibility='collapsed')

                # Convert translated text to speech
                if translated_text.text:
                    audio_data = elevenlabs_tts(translated_text.text)
                    if audio_data:
                        st.session_state.audio_data = audio_data
                else:
                    st.warning("No text available to convert to speech.")
            except Exception as e:
                st.error(f"An error occurred: {e}")

    if 'audio_data' in st.session_state:
        st.markdown("#### Synthesized Speech Translation")
        st.audio(st.session_state.audio_data)

if __name__ == "__main__":
    main()
