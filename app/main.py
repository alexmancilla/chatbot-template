from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routers import chatbot

app = FastAPI(
    title="API del Chatbot USEP",
    description="API para el Chatbot de USEP",
    version="0.1.0"
)

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Para producción, especifica los orígenes permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(chatbot.router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API del Chatbot USEP"} 