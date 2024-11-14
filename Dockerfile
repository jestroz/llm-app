# Usamos una imagen base de Python
FROM python:3.9-slim AS builder

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los requerimientos de la aplicación
COPY src/requirements.txt .

# Copiar el archivo requirements.txt y instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install -U langchain-community

FROM builder

# Copiar el codigo de la aplicación
COPY src/app.py /app/

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
