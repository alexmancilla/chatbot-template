from app.core.chatbot import process_message

def main():
    print("Bot de Preguntas y Respuestas - Escribe 'salir' para terminar")
    while True:
        user_query = input("\nEscribe tu pregunta: ")
        if user_query.lower() in ['salir', 'salida', 'exit', 'quit', 'q']:
            print("¡Hasta luego!")
            break
        try:
            answer = process_message(user_query)
            print(f"Respuesta: {answer}")
        except Exception as e:
            print(f"Error: {e}")
            print("Lo siento, no pude encontrar una respuesta a tu pregunta.")

if __name__ == "__main__":
    main() 