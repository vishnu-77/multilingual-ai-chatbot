# 🌍 Multilingual AI Chatbot

Build your own ChatGPT-like chatbot in 15 minutes! Supports 8+ languages and runs completely FREE.

## ✨ Features

- 🌐 8 Languages (English, Spanish, French, German, Hindi, Japanese, Chinese, Arabic)
- 💬 Multiple Chat Histories
- ⚡ Lightning Fast (Groq API)
- 💰 100% FREE

## 🚀 Quick Start

### 1. Install

```bash
git clone https://github.com/yourusername/multilingual-chatbot.git
cd multilingual-chatbot
pip install groq streamlit
```

### 2. Get API Key

- Go to [console.groq.com](https://console.groq.com)
- Sign up (FREE, no credit card)
- Create API key
- Copy it

### 3. Add Your Key

This project reads the Groq API key from the `GROQ_API_KEY` environment
variable. Do not hard-code your key into source files. Instead set the
environment variable before running the app.

Locally (PowerShell):
```powershell
$env:GROQ_API_KEY = "paste_your_key_here"
streamlit run ui.py
```

On Streamlit Cloud (or other hosting) set a secret / environment variable
named `GROQ_API_KEY` in the app settings or deployment environment.
In Streamlit Cloud: App Settings → Secrets → Add `GROQ_API_KEY` = "your_key"

The app will show a friendly error if `GROQ_API_KEY` is not set.

Local `.streamlit/secrets.toml` example
--------------------------------------
You can also store secrets locally during development by creating a
`.streamlit/secrets.toml` file in the project root (don't commit this file).

Example `./.streamlit/secrets.toml`:
```toml
# .streamlit/secrets.toml
GROQ_API_KEY = "paste_your_key_here"
```

Streamlit will load the secrets into `st.secrets` at runtime, and the
application will read from `st.secrets["GROQ_API_KEY"]` if the environment
variable is not present.

### 4. Run

```bash
streamlit run ui.py
```

That's it! Open `http://localhost:8501` in your browser.

## 📁 Files

```
backend.py  → AI logic
ui.py       → User interface
```

## 🎨 Customize

**Add languages:** Edit the language list in `ui.py`

**Change AI personality:** Modify system message in `backend.py`

**Different model:** Change model name to `llama-3.1-8b-instant` for faster responses

## 🐛 Common Issues

**"Module not found"** → Run: `pip install groq streamlit`

**"Invalid API key"** → Get new key from console.groq.com

**"Model error"** → Use: `llama-3.3-70b-versatile`
