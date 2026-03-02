# 🤖 Simple Groq Chatbot API

A beginner-friendly chatbot backend built with **FastAPI** and **Groq AI**.  
You send a message, the AI replies. That's it!

---

## 📁 Project Structure

```
FASTAPI_SIMPLE_CHAT/
│
├── app/
│   ├── config.py        # Loads settings from the .env file
│   ├── logger.py        # Sets up logging
│   ├── llm_service.py   # Talks to the Groq AI and gets a reply
│   └── main.py          # The web server
│
├── .env                 # API keys
├── requirements.txt     # List of packages to install
└── README.md            # This file
```

---

## ⚙️ Setup Instructions

### 1. Clone or download the project

```bash
git clone https://github.com/Anirudhan-Valsan/FASTAPI_SIMPLE_CHAT.git
cd FASTAPI_SIMPLE_CHAT
```

### 2. Create a virtual environment (recommended)

A virtual environment keeps your project's packages separate from the rest of your system.

```bash
python -m venv venv
```

Activate it:

- **Windows:** `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Create your `.env` file

Create a file called `.env` in the root of your project and add the following:

```
GROQ_API_KEY=your_groq_api_key_here
MODEL_NAME=llama-3.1-8b-instant
SYSTEM_PROMPT=You are a helpful assistant.
```

> 🔑 Get your free Groq API key at [https://console.groq.com](https://console.groq.com)

---

## ▶️ Running the App

```bash
uvicorn app.main:app --reload
```

- `--reload` means the server automatically restarts when you change your code 
- The server runs on `http://localhost:8000` by default

---

## 🧪 Testing the API

### Option 1 — Browser (Interactive Docs)

Open your browser and go to:

```
http://localhost:8000/docs
```

FastAPI gives you a free interactive UI where you can test your endpoints without any extra tools.

### Option 2 — curl (Terminal)

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello! What can you do?"}'
```

### Option 3 — Python script

```python
import requests

response = requests.post("http://localhost:8000/chat", json={
    "message": "Tell me a fun fact!",
    "temperature": 0.7
})

print(response.json())
```

---

## 📬 API Reference

### `POST /chat`

Send a message and get an AI reply.

**Request body:**

| Field         | Type    | Required | Default | Description                        |
|---------------|---------|----------|---------|------------------------------------|
| `message`     | string  | ✅ Yes   | —       | The message you want to send       |
| `temperature` | float   | ❌ No    | `0.7`   | Creativity level (0.0 = safe, 1.0 = creative) |

**Example request:**

```json
{
  "message": "What is Python?",
  "temperature": 0.7
}
```

**Example response:**

```json
{
  "response": "Python is a beginner-friendly programming language known for its simple, readable syntax..."
}
```

---

## 📦 requirements.txt

```
fastapi
uvicorn
groq
python-dotenv
pydantic
```