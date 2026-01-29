def compute_risk(emotions: dict) -> tuple:
    risk_score = (
        emotions.get("fear", 0)
        + emotions.get("anger", 0)
        + emotions.get("sadness", 0)
        + emotions.get("nervousness", 0)
    ) * 100

    risk_score = round(min(risk_score, 100), 2)

    if risk_score < 30:
        level = "Safe"
    elif risk_score < 60:
        level = "Caution"
    else:
        level = "High Emotional Risk"

    return risk_score, level

def risk_badge(score: float) -> dict:
    if score < 30:
        return {
            "label": "Safe",
            "color": "green",
            "description": "Content is unlikely to cause emotional distress."
        }
    elif score < 60:
        return {
            "label": "Caution",
            "color": "yellow",
            "description": "Content may cause mild emotional discomfort."
        }
    else:
        return {
            "label": "High Emotional Risk",
            "color": "red",
            "description": "Content may significantly impact mental well-being."
        }