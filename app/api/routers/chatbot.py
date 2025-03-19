from fastapi import APIRouter, Depends, HTTPException
from app.api.models.chat import ChatRequest, ChatResponse
from app.core.chatbot import process_message

router = APIRouter(tags=["chatbot"])

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Procesa un mensaje de chat y devuelve una respuesta
    """
    try:
        response = process_message(request.message)
        return ChatResponse(
            message=response,
            success=True
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 