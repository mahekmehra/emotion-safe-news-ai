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
    try:
        tone_instruction = {
            "neutral": "Rewrite in a neutral, factual, and calm tone.",
            "educational": "Rewrite in an educational tone that explains context clearly without emotional language.",
            "reassuring": "Rewrite in a reassuring tone that reduces anxiety while remaining factual."
        }.get(tone, "Rewrite in a neutral and calm tone.")

        prompt = f"""
{tone_instruction}

Avoid fear-based or sensational language.
Do not minimize facts, but present them responsibly.

Text:
{text}
"""
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception:
        return (
            "This content discusses an event based on available information. "
            "Readers are encouraged to review verified sources calmly."
        )

