# API de Chatbot

Este es un backend FastAPI para una aplicación de chatbot

## Configuración

1. Clonar el repositorio
2. Crear un entorno virtual: `python3 -m venv venv`
3. Activar el entorno virtual:
   - En Windows: `venv\Scripts\activate`
   - En macOS/Linux: `source venv/bin/activate`
4. Instalar dependencias: `pip install -r requirements.txt`
5. Copiar `.env.example` a `.env` y ajustar la configuración según sea necesario
6. Iniciar el servidor de desarrollo: `uvicorn app.main:app --reload`

## Documentación de la API

Cuando el servidor está en ejecución, puedes acceder a la documentación de la API autogenerada en:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Características

- Backend FastAPI con soporte asincrónico
- Lógica de chatbot basada en similitud semántica con modelos multilingües
- Endpoints API para interacción con el chat
- Soporte CORS

## Tecnologías utilizadas

- FastAPI para la API REST
- Sentence Transformers para el modelo de similitud semántica
- NLTK para procesamiento de lenguaje natural
- PyTorch como backend para los modelos

## Licencia

[MIT](https://choosealicense.com/licenses/mit/) 
