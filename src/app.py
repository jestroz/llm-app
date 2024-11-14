import requests
from langchain.llms.base import LLM

class OllamaLLM(LLM):
    def _call(self, prompt: str, stop=None):
        # Llamada a la API local de Ollama
        response = requests.post(
            "http://192.168.100.35:7869/api/generate",
            json={
                "model": "rustic",
                "prompt": prompt,
                "stream": False
            }
        )
        result = response.json()
        return result["response"]

    @property
    def _identifying_params(self):
        return {"model": "rustic"}

    @property
    def _llm_type(self) -> str:
        return "ollama"

llm = OllamaLLM()

def conversacion():
    estado = "bienvenido"
    historial = []
    empresa = "Rustic Linux"

    # Bienvenida e introducción
    print(f"\nSoy Rustic-BOT de {empresa}. Estoy aquí para ayudarte.\n")
    nombre_usuario = input(f"Primero dime ¿Cómo te llamas? ")

    # Bucle de conversación
    while True:
        if estado == "bienvenido":
            print(f"- Rustic-BOT: Hola {nombre_usuario}!! En que te puedo ayudar?")
            mensaje_usuario = input(f"- {nombre_usuario}: ")
            historial.append(f"{nombre_usuario}: {mensaje_usuario}")
            estado = "conversando"
        else:
            print(f"Puedes escribir 'salir' en cualquier momento para abandonar la conversacion\n")
            mensaje_usuario = input(f"- {nombre_usuario}: ")
            historial.append(f"{nombre_usuario}: {mensaje_usuario}")

        # Si el usuario quiere salir
        if mensaje_usuario.lower() == "salir":
            print(f"- Rustic-BOT: Adiós, {nombre_usuario}. ¡Que tengas un buen día!")
            break

        # Procesar el mensaje del usuario
        respuesta = procesar_mensaje(mensaje_usuario, historial, estado, nombre_usuario)
        print(f"- Rustic-BOT: {respuesta} \n")

def procesar_mensaje(mensaje_usuario, historial, estado, nombre_usuario):
    # Convertir historial a cadena legible
    historial_str = "\n".join(historial[-5:])  # Limitar a los últimos 5 mensajes
    prompt = f"Conversación previa:\n{historial_str}\nUsuario: {mensaje_usuario}\n"
    prompt += f"Recuerda que estás hablando con {nombre_usuario}, un cliente o futuro cliente."

    try:
        # Llamar al modelo LLM
        respuesta_modelo = llm.invoke(prompt)
        return respuesta_modelo.strip()
    except Exception as e:
        return f"Ocurrió un error: {e}"

# Iniciar la conversación
conversacion()
