from fastapi import APIRouter
from app.schemas.analysis import TextInput, AnalysisResponse
from app.services.emotion_service import detect_emotions
from app.services.highlight_service import highlight_text
from app.services.scoring_service import compute_risk, risk_badge
from app.services.genai_service import explain, rewrite
from app.services.url_service import extract_text_from_url
from app.schemas.url_analysis import URLInput
from app.schemas.batch import BatchInput

router = APIRouter()

@router.post("/analyze", response_model=AnalysisResponse)
def analyze_content(payload: TextInput):
    emotions = detect_emotions(payload.text)
    risk_score, risk_level = compute_risk(emotions)
    badge = risk_badge(risk_score)

    highlights = highlight_text(payload.text)

    explanation = explain(payload.text, emotions)
    rewritten = rewrite(payload.text, payload.tone)

    return AnalysisResponse(
        emotions=emotions,
        risk_score=risk_score,
        risk_level=risk_level,
        risk_badge=badge,
        highlights=highlights,
        explanation=explanation,
        rewritten_text=rewritten
    )

@router.post("/analyze-url", response_model=AnalysisResponse)
def analyze_url(payload: URLInput):
    text = extract_text_from_url(payload.url)

    emotions = detect_emotions(text)
    risk_score, risk_level = compute_risk(emotions)
    badge = risk_badge(risk_score)
    highlights = highlight_text(text)

    explanation = explain(text, emotions)
    rewritten = rewrite(text, payload.tone)

    return AnalysisResponse(
        emotions=emotions,
        risk_score=risk_score,
        risk_level=risk_level,
        risk_badge=badge,
        highlights=highlights,
        explanation=explanation,
        rewritten_text=rewritten
    )

@router.post("/analyze-batch")
def analyze_batch(payload: BatchInput):
    results = []

    for text in payload.texts:
        emotions = detect_emotions(text)
        risk_score, risk_level = compute_risk(emotions)
        badge = risk_badge(risk_score)
        highlights = highlight_text(text)

        rewritten = rewrite(text, payload.tone)

        results.append({
            "text": text,
            "risk_score": risk_score,
            "risk_level": risk_level,
            "risk_badge": badge,
            "highlights": highlights,
            "rewritten_text": rewritten
        })

    return {"results": results}