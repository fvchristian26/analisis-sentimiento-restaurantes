# Usar imagen ligera de Python
FROM python:3.9-slim

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiar e instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código fuente y el modelo al contenedor
COPY . /app/

# Comando por defecto para ejecutar tu script principal
CMD ["python", "simular.py"]