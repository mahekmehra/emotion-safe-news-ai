# Backend – Emotion-Aware GenAI Media Guard 🧠⚙️

This backend provides the **core intelligence layer** of the Emotion-Aware GenAI Media Guard system.  
It exposes REST APIs for emotion detection, mental health risk assessment, GenAI-based explanation, and neutral content rewriting.

The backend is built using **FastAPI** and is designed to be **frontend-agnostic**, enabling integration with web apps, mobile apps, browser extensions, or other services.

---

## 🧠 Responsibilities

The backend handles:

- Emotion detection using NLP models
- Emotional manipulation risk scoring
- Mental health risk categorization
- Generative AI explanation of harmful content
- Neutral, educational, or reassuring content rewriting
- Clean API contracts for frontend consumption

---

## 🏗️ Architecture Overview

backend/
├── app/
│ ├── api/ # API routes
│ ├── core/ # Configuration & environment
│ ├── schemas/ # Request / response models
│ ├── services/ # NLP, GenAI, scoring logic
│ └── main.py # FastAPI entry point
│
├── requirements.txt
└── README.md


---

## 🚀 Tech Stack

- **Framework**: FastAPI
- **NLP**: HuggingFace Transformers, SpaCy
- **Emotion Model**: GoEmotions (RoBERTa)
- **GenAI**: Google Gemini
- **Validation**: Pydantic
- **Server**: Uvicorn

---

## 🔌 API Endpoints

### `POST /api/v1/analyze`

Analyze content for emotional manipulation and mental health impact.

#### Request Body
```json
{
  "text": "This shocking decision is creating fear and panic.",
  "tone": "reassuring"
}

#### Response Body
```json
{
  "emotions": { "fear": 0.78, "anger": 0.12 },
  "risk_score": 82.5,
  "risk_level": "High Emotional Risk",
  "explanation": "This content uses fear-inducing language...",
  "rewritten_text": "Officials announced a decision and experts advise..."
}

---

## 🧪 Running the Backend Locally

### 1️⃣ Activate virtual environment
- venv/Scripts/activate

### 2️⃣ Install dependencies
- pip install -r requirements.txt
- python -m spacy download en_core_web_sm

### 3️⃣ Set environment variables
- setx GEMINI_API_KEY "your_api_key_here"

Restart the terminal after this step.

### 4️⃣ Run the server
- uvicorn app.main:app --reload



### 5️⃣ Open API Docs
👉 http://127.0.0.1:8000/docs

---

## 🧠 Design Philosophy

- Modular service-based architecture
- Clear API contracts
- Ethical & mental-health-aware AI design
- Easy to extend with new models or features

---

## 🔮 Planned Enhancements

- Caching (Redis)
- Authentication & rate limiting
- Batch analysis endpoints
- URL-based content ingestion
- Production deployment with Docker

---

## 👤 Author

**Mahek Mehra**  
Emotion-Aware & Ethical GenAI Systems
