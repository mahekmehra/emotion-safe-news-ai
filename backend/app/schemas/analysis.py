from typing import Dict, List
from pydantic import BaseModel


class TextInput(BaseModel):
    text: str
    tone: str = "neutral"  # neutral | educational | reassuring


class Highlight(BaseModel):
    word: str
    emotion: str
    start: int
    end: int


class RiskBadge(BaseModel):
    label: str
    color: str
    description: str


class AnalysisResponse(BaseModel):
    emotions: Dict[str, float]
    risk_score: float
    risk_level: str
    risk_badge: RiskBadge
    highlights: List[Highlight]
    explanation: str
    rewritten_text: str

