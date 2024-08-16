FROM python:3.12-slim

# Crear un usuario no root
RUN adduser --disabled-password --gecos '' appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Cambiar la propiedad de los archivos de la aplicación al usuario no root
RUN chown -R appuser:appuser /app

# Cambiar al usuario no root
USER appuser

EXPOSE 8000

# Quitar --reload para producción
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]