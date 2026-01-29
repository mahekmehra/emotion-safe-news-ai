import re
from app.core.emotion_triggers import EMOTION_TRIGGERS

def highlight_text(text: str):
    highlights = []

    lowered = text.lower()

    for emotion, words in EMOTION_TRIGGERS.items():
        for word in words:
            for match in re.finditer(rf"\b{word}\b", lowered):
                highlights.append({
                    "word": text[match.start():match.end()],
                    "emotion": emotion,
                    "start": match.start(),
                    "end": match.end()
                })

    return highlights
