
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


## Technology Stack  

| **Technology** | **Description** |
|----------------|-----------------|
| ![OpenAI Logo](https://upload.wikimedia.org/wikipedia/commons/6/66/OpenAI_Logo.svg) **OpenAI Whisper** | Speech-to-text transcription. |
| ![Google Translate Logo](https://upload.wikimedia.org/wikipedia/commons/2/2d/Google_Translate_logo.svg) **Google Translate** | Multilingual text translation. |
| ![ElevenLabs Logo](https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Eleven_Labs_Logo.svg/1200px-Eleven_Labs_Logo.svg.png) **ElevenLabs** | Realistic multilingual text-to-speech synthesis. |
| ![Streamlit Logo](https://upload.wikimedia.org/wikipedia/commons/3/30/Streamlit_logo.svg) **Streamlit** | Interactive user interface for seamless operation. |
| ![Python Logo](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg) **Python** | Backend logic for AI integration and API calls. |

---


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

