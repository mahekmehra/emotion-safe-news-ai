from fastapi import FastAPI
from app.api.v1.routes import router

app = FastAPI(
    title="Emotion-Aware GenAI Media Guard",
    description="Detects emotional manipulation and rewrites content safely",
    version="1.0.0"
)

app.include_router(router, prefix="/api/v1")
