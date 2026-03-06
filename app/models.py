from pydantic import BaseModel
from typing import Optional


class UserInput(BaseModel):
    message: Optional[str] = None
    image_base64: Optional[str] = None
    user_id: str


class AIResponse(BaseModel):
    response: str
    confidence_score: float