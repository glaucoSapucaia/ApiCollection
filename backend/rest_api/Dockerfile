FROM python:3.11-slim

WORKDIR /app

# Instala netcat para o entrypoint.sh poder usar 'nc'
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x ./scripts/entrypoint.sh

ENTRYPOINT ["sh", "./scripts/entrypoint.sh"]
