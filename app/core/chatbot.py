import json
import os
import numpy as np
from sentence_transformers import SentenceTransformer
import nltk
from pathlib import Path

# Descargar datos de NLTK necesarios
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# Ruta a la base de conocimientos
KNOWLEDGE_BASE_PATH = os.path.join(os.path.dirname(__file__), 'knowledge_base.json')

# Cargar la base de conocimientos
with open(KNOWLEDGE_BASE_PATH, 'r', encoding='utf-8') as file:
    knowledge_base = json.load(file)

# Cargar el modelo multilingüe usando sentence-transformers
model = None

def load_model():
    global model
    if model is None:
        try:
            model = SentenceTransformer('distiluse-base-multilingual-cased-v2')
            print("Modelo cargado: distiluse-base-multilingual-cased-v2")
        except Exception as e:
            print(f"Error al cargar el modelo principal: {e}")
            try:
                model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')
                print("Modelo cargado: paraphrase-multilingual-mpnet-base-v2")
            except Exception as e:
                print(f"Error al cargar el modelo alternativo: {e}")
                print("Usando modelo básico...")
                model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
    return model

# Pre-calcular los embeddings de las preguntas conocidas
question_embeddings = None
questions = None

def init_embeddings():
    global question_embeddings, questions
    if question_embeddings is None:
        model = load_model()
        questions = [item['question'] for item in knowledge_base['questions']]
        question_embeddings = model.encode(questions, convert_to_numpy=True)

def find_closest_question(user_query):
    # Asegurarse de que el modelo y los embeddings estén inicializados
    init_embeddings()
    model = load_model()
    
    # Calcular el embedding de la consulta del usuario
    query_embedding = model.encode(user_query, convert_to_numpy=True)
    
    # Calcular similitud con todas las preguntas conocidas
    similarities = np.dot(query_embedding, question_embeddings.T) / (
        np.linalg.norm(query_embedding) * np.linalg.norm(question_embeddings, axis=1)
    )
    
    # Encontrar el índice de la pregunta más similar
    closest_index = np.argmax(similarities)
    
    return closest_index, similarities[closest_index]

def process_message(message: str) -> str:
    """
    Procesa el mensaje entrante y genera una respuesta usando similitud semántica
    
    Args:
        message: El mensaje del usuario
        
    Returns:
        str: La respuesta del chatbot
    """
    if not message:
        return "Por favor, proporciona un mensaje."
    
    try:
        # Buscar la pregunta más similar en la base de conocimientos
        closest_index, similarity = find_closest_question(message)
        
        # Si la similitud es muy baja, podríamos no tener una buena respuesta
        if similarity < 0.3:
            return f"Lo siento, no tengo información suficiente para responder esa pregunta. ¿Podrías reformularla?"
        
        # Devolver la respuesta correspondiente
        return knowledge_base['questions'][closest_index]['answer']
        
    except Exception as e:
        print(f"Error: {e}")
        return "Lo siento, ha ocurrido un error al procesar tu mensaje." 