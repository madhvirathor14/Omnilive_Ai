from fastapi import APIRouter
from app.models import UserInput, AIResponse
from app.gemini_engine import generate_response
from app.memory_engine import update_user_memory
from app.monitoring_engine import analyze_response

router = APIRouter()


@router.post("/chat", response_model=AIResponse)
async def chat(user_input: UserInput):

    # AI response generate
    ai_text = generate_response(user_input.message)

    # memory update
    update_user_memory(
        user_input.user_id,
        user_input.message,
        ai_text
    )

    # monitoring
    metrics = analyze_response(ai_text)

    return AIResponse(
        response=ai_text,
        confidence_score=metrics["confidence_score"]
    )