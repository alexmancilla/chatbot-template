from pydantic import BaseModel

class ChatRequest(BaseModel):
    """
    Modelo de solicitud de chat
    """
    message: str

class ChatResponse(BaseModel):
    """
    Modelo de respuesta de chat
    """
    message: str
    success: bool 