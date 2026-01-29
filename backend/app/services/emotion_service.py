import spacy
from transformers import pipeline

nlp = spacy.load("en_core_web_sm")

emotion_model = pipeline(
    "text-classification",
    model="SamLowe/roberta-base-go_emotions",
    return_all_scores=True
)

def preprocess(text: str) -> str:
    doc = nlp(text.lower())
    return " ".join([t.text for t in doc if not t.is_stop])


def detect_emotions(text: str) -> dict:
    processed = preprocess(text)[:512]
    result = emotion_model(processed)[0]
    return {r["label"]: r["score"] for r in result}
