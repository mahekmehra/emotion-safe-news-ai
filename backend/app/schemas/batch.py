from pydantic import BaseModel
from typing import List

class BatchInput(BaseModel):
    texts: List[str]
    tone: str = "neutral"
