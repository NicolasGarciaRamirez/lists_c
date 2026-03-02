FROM python:3.12-slim

WORKDIR /app

# Evita archivos .pyc y buffer de stdout
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Dependencias (si luego agregas alguna)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Código fuente

# CMD ["python", "src/main.py"]
