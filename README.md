# App para interactuar con Llama desde su API (local en este caso), para chatbot de Rustic Linux

- Requiere una instancia de Ollama local, en este caso levantada en el puerto 7869

    Llamada a la API:  Biblioteca requests para enviar peticiones POST a la API Ollama en el puerto 7869.

    Definición de LLM:  Clase OllamaLLM que hereda de la clase base LLM de Langchain. Esta clase define cómo interactuar con Llama y las propiedades del modelo.

    Interacción:  La función interactuar_con_modelo() permite al usuario ingresar consultas y recibir respuestas del modelo Llama en un bucle infinito hasta que el usuario escribe "salir".


Se debe modificar app.py apuntando a la API a consultar y luego con docker:

`docker build . -t llm-app` Buildear la imagen con el tag 'llm-app'

`docker run --rm -it llm-app python app.py` Correr el contenedor y la app directamente

Se agrega 'run_app.sh' que genera un modelo nuevo en base a Modelfile, en este caso 'rustic', se le pasa como argumento.

Este genera el modelo en la instancia para que luego la app lo utilice

`./run_app.sh rustic`

- Me falta agregar un docker-compose a futuro con una db chromadb para RAG (origenes externos)
