# 🤖 Balamma AI Companion

A web-based AI companion powered by Python, Flask, and the Google Gemini API. This project demonstrates an agentic workflow where the AI is equipped with a distinct persona (Balamma from Nalgonda) and real-time internet search capabilities.

## ✨ Features
* **Conversational AI:** Powered by the `gemini-1.5-flash` model for fast, natural interactions.
* **Agentic Tool Calling:** Integrated with Google Search to fetch real-time news and ground responses in factual data.
* **Custom Persona:** Prompt-engineered to have the personality of Balamma, a warm and witty 25-year-old from Nalgonda, Telangana.
* **Dynamic UI:** Features custom-generated visual avatars with lip-sync states when responding.
* **Resiliency:** Configured with API rate-limit handling and automatic retries.

## 🛠️ Tech Stack
* **Backend:** Python, Flask
* **AI & LLM:** Google Gemini API, Google ADK (Agent Development Kit)
* **Tools:** Antigravity CLI, Google Cloud Platform

## 🚀 How to Run Locally
1. Clone this repository: `git clone https://github.com/RITHISH-REDDY/ai-companion-balamma.git`
2. Navigate to the directory: `cd ai-companion-balamma`
3. Install dependencies: `pip install -r requirements.txt`
4. Set your Gemini API Key: `export GEMINI_API_KEY="your_api_key_here"`
5. Run the server: `python app.py`
6. Open your browser and navigate to `http://127.0.0.1:5000`
