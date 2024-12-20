# Usar una imagen base ligera de Python
FROM python:3.10-slim

# Configurar el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los requerimientos para instalar las dependencias
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación al contenedor
COPY . .

# Configurar variables de entorno para Django
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Exponer el puerto de Django
EXPOSE 8000

# Ejecutar las migraciones y levantar el servidor de desarrollo
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

