
---

# 🌍 Real-Time Healthcare Translation App  

**Breaking language barriers in healthcare with Generative AI.**  


## 📖 Overview  

The **Real-Time Healthcare Translation App** enhances communication between patients and healthcare providers by providing real-time transcription, translation, and voice synthesis. This app ensures smooth multilingual interactions, enabling better care and accessibility in diverse healthcare environments.  

Built using **OpenAI Whisper**, **Google Translate**, **ElevenLabs**, and **Streamlit**, it combines cutting-edge technologies to deliver accurate and natural language processing features.  

---

## 🚀 Features  

- **Speech-to-Text**:  
  Converts spoken language into text using **OpenAI Whisper**.  
- **Real-Time Translation**:  
  Translates text into multiple languages with **Google Translate**.  
- **Text-to-Speech**:  
  Generates realistic voice responses with **ElevenLabs**.  
- **Multilingual Support**:  
  Supports English, Urdu, Hindi, Spanish, French, and more.  
- **Interactive UI**:  
  User-friendly interface built with **Streamlit** for seamless operation.  

---

## 📦 Technology Stack  

<div align="center">
  <img src="https://streamlit.io/images/brand/streamlit-mark-color.svg" alt="Streamlit Logo" height="60" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/d/d4/Google_Translate_logo.png" alt="Google Translate Logo" height="60" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/a/a0/OpenAI_Logo.svg" alt="OpenAI Logo" height="60" />
  <img src="https://github.com/elevenlabs/elevenlabs-python/raw/main/logo.png" alt="ElevenLabs Logo" height="60" />
</div>  

---

## 🗂️ Project Structure  

```plaintext
|-- app.py                # Main Streamlit app for UI and core logic.
|-- util.py               # Utility functions for translation and text-to-speech.
|-- requirements.txt      # Python dependencies.
|-- README.md             # Project documentation.
```

---

## ⚙️ Installation  

Follow the steps below to set up the project locally:  

### 1. Clone the Repository  

```bash
git clone https://github.com/yourusername/healthcare-translation-app.git
cd healthcare-translation-app
```  

### 2. Install Dependencies  

Install the required Python packages using:  

```bash
pip install -r requirements.txt
```  

### 3. Add API Keys  

Create a `.env` file in the root directory and add the required API keys:  

```plaintext
OPENAI_API_KEY=your_openai_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
```  

### 4. Run the App  

Run the application using Streamlit:  

```bash
streamlit run app.py
```  

The app will launch in your default web browser.  

---

## 💡 How It Works  

1. **Input Speech**: Record your voice   
2. **Transcription**: The app converts your speech to text using **OpenAI Whisper**.  
3. **Translation**: The text is translated into the desired language with **Google Translate**.  
4. **Voice Output**: The translated text is converted into speech using **ElevenLabs**.  
5. **Interactive UI**: The results are displayed and managed through the **Streamlit** interface.  

---

## 🌟 Advantages  

- **Improved Communication**: Enhances understanding between patients and healthcare providers.  
- **Secure**: Ensures sensitive data is handled securely.  
- **Cost-Effective**: Leverages affordable APIs for maximum efficiency.  
- **Scalable**: Easily extendable for new features or additional languages.  

---

