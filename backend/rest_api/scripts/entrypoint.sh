#!/bin/bash

# Aguarda o banco ficar pronto
echo "Aguardando o PostgreSQL iniciar..."
while ! nc -z db 5432; do
  sleep 1
done

echo "Banco de dados está pronto. Rodando migrations..."

# Executa as migrations Alembic
alembic upgrade head

# Inicia o servidor FastAPI
echo "Iniciando a API REST..."
exec uvicorn main:app --host 0.0.0.0 --port 8000