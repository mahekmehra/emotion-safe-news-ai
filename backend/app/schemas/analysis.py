from pydantic import BaseModel
from typing import Dict

class TextInput(BaseModel):
    text: str
    tone: str = "neutral"  # neutral | educational | reassuring


class AnalysisResponse(BaseModel):
    emotions: Dict[str, float]
    risk_score: float
    risk_level: str
    explanation: str
    rewritten_text: str
