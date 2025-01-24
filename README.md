
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


| **Technology**            | **Description**                                      |  
|---------------------------|------------------------------------------------------|  
| ![OpenAI Logo](https://en.m.wikipedia.org/wiki/File:OpenAI_Logo.svg) **OpenAI Whisper**         | Speech-to-text transcription.                       |  
| ![Google Translate Logo](https://en.m.wikipedia.org/wiki/File:Google_Translate_logo.svg) **Google Translate**       | Multilingual text translation.                      |  
| ![ElevenLabs Logo](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMwAAADACAMAAAB/Pny7AAAAUVBMVEX///8AAADe3t7n5+fT09M5OTm0tLSsrKwxMTF/f3/x8fHt7e1paWlAQEDOzs4kJCRJSUmampoSEhKioqL39/cZGRlkZGQICAhQUFApKSm9vb3IFuFuAAAB6UlEQVR4nO3dQW+qQBSG4TNgsYACgtre+/9/aEFjGtmYppOcj9P3WbiBxXkXZJhIMpYWdWub1ta3DFt+DqX3NL9VHh4xx857lt/rjveYy957khymyy3m2ngPkkNzXWL6ynuOPKp+jhm8p8hlmGNO3kPkcko2Ft5D5FKMNnrPkM9oYR6Z+aGx2nuEfGqbvEfIZ7Igq8yisgDvZQ+d7bxHyGdnYZaZeaGxzW9lvpUW4pX5ro0U09jZe4R8zrFiAAAAAAAAAAAAsGHnaf9kWn2V21TP1/fK/3WXaWX1lUHRr64rfx/yMuaNGB/EqCJGFTGqiFFFjCpiVBGjihhVxKgiRhUxqohRRYwqYlQRo4oYVcSoIkYVMaqIUUWMKmJUEaOKGFXEqCJGFTGqiFFFjCpiVBGjihhVxKgiRhUxqohRRYwqYlQRo4oYVX8r5n1TMe9PPtYxn/+er//3mRMAAAAAAAAAgD8h0Cm0wU4HDnUIdfv6pq1oYh3crnzMwA8Vtnt901bsrPMeIZ/OlP+8/qHKJu8R8pms9h4hn9oG7xHyGWz0HiGf0cYwC00xWjp5D5HLKVkK89AMc0wfZKWp+jkmXUPsApprWmIuIdbN/eUWk44B3s+6Y7rHpMPmNzXlIT1iUr3x/WZb3zK+ACvFGUzIcmBeAAAAAElFTkSuQmCC) **ElevenLabs**             | Realistic multilingual text-to-speech synthesis.    |  
| ![Streamlit Logo](https://upload.wikimedia.org/wikipedia/commons/3/30/Streamlit_logo.svg) **Streamlit**              | Interactive user interface for seamless operation.  |  
| ![Python Logo](https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg) **Python**                 | Backend logic for AI integration and API calls.     |  

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

