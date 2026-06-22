#1. Usamos una imagen oficial de python ligera como base
FROM python:3.11-slim

#2. Definimos el directorio de trabajo dentro del contenedor
WORKDIR /app

#3. Copiamos el archivo de requerimientos primero (optimiza la caché de Docker)
COPY requirements.txt .

#4. Instalamos las dependencias dentro del contenedor
RUN pip install --no-cache-dir -r requirements.txt

#5. Copiamos el resto de nuestro código fuente

COPY . .

#6. Definimos el comando que se ejecutara al iniciar el contenedor
CMD ["python", "app.py"]