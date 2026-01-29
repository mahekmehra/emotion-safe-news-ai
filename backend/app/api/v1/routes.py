from fastapi import APIRouter
from app.schemas.analysis import TextInput, AnalysisResponse
from app.services.emotion_service import detect_emotions
from app.services.scoring_service import compute_risk
from app.services.genai_service import explain, rewrite

router = APIRouter()

@router.post("/analyze", response_model=AnalysisResponse)
def analyze_content(payload: TextInput):
    emotions = detect_emotions(payload.text)
    risk_score, risk_level = compute_risk(emotions)

    explanation = explain(payload.text, emotions)
    rewritten = rewrite(payload.text, payload.tone)

    return AnalysisResponse(
        emotions=emotions,
        risk_score=risk_score,
        risk_level=risk_level,
        explanation=explanation,
        rewritten_text=rewritten
    )
