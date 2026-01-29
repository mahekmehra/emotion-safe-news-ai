import google.generativeai as genai
from app.core.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

def explain(text: str, emotions: dict) -> str:
    prompt = f"""
Explain calmly why the following content may emotionally manipulate readers.
Avoid alarming language.

Text:
{text}

Detected emotions:
{emotions}
"""
    return model.generate_content(prompt).text.strip()


def rewrite(text: str, tone: str) -> str:
    prompt = f"""
Rewrite the following content in a {tone} tone.
Ensure it is mentally safe, calm, and factual.

Text:
{text}
"""
    return model.generate_content(prompt).text.strip()
