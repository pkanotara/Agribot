# 🌱 Agribot - AI Farming Assistant

Agribot is an AI-powered farming assistant built using **Streamlit** and **Google Generative AI**.
It helps farmers with crop analysis, disease detection, and smart suggestions in **English, Hindi, and Gujarati**.

---

## 🚀 Features

* 🌍 Multi-language support (English / हिंदी / ગુજરાતી)
* 🖼️ Crop disease analysis using images
* 🤖 AI-powered smart suggestions
* 📝 Report generation and history tracking
* 🎨 Easy-to-use Streamlit interface

---

## 🛠️ Tech Stack

* **Frontend/UI**: Streamlit
* **Backend/Logic**: Python
* **AI Integration**: Google Generative AI (`google-generativeai`)
* **Image Processing**: PIL
* **Data Storage**: JSON / Local reports folder

---

## 📂 Project Structure

```
Agribot/
│── main.py                  # Alternative entry point
│── streamlit_app.py         # Main Streamlit entry point
│── requirements.txt         # Python dependencies
│── conversations.json       # Stores chat/conversation history
│── structure.txt            # Notes on project structure
│
├───.streamlit/              # Streamlit configuration
│   └── secrets.toml         # API keys / secrets
│
├───agribot/
│   ├── components/          # UI Components (sidebar, navbar, etc.)
│   ├── pages/               # Streamlit multi-page setup (about, analyze, login, history)
│   ├── utils/               # Helpers (db, constants, translator, session, model)
│   └── __init__.py
│
├───reports/                 # Auto-generated reports
└───__pycache__/             # Compiled cache files

```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/pkanotara/Agribot.git
cd Agribot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Google API Key

Agribot uses Google Generative AI.
Set your API key as an environment variable:

```bash
export GOOGLE_API_KEY="your_api_key_here"   # Mac/Linux
set GOOGLE_API_KEY="your_api_key_here"      # Windows (cmd)
$env:GOOGLE_API_KEY="your_api_key_here"     # Windows (PowerShell)
```

### 4. Run the Application

```bash
streamlit run streamlit_app.py
```

The app will open in your browser at **[http://localhost:8501](http://localhost:8501)**

---

## 📸 Screenshots

*(Add your app screenshots here for better presentation)*

---

## 📚 References

* [Streamlit Documentation](https://streamlit.io)
* [Google Generative AI](https://ai.google.dev)
* [Python Pillow (PIL)](https://pillow.readthedocs.io/en/stable/)
* Government Agricultural Portals (India)
* Relevant IEEE papers on AI in Agriculture

---

## 👨‍💻 Author

**Pravin Kanotara**
GitHub: [pkanotara](https://github.com/pkanotara)

---
