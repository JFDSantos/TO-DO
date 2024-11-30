# Usar uma imagem oficial do Python como base
FROM python:3.10-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar apenas o arquivo de dependências primeiro (melhora cache)
COPY requirements.txt .

# Instalar dependências
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código para o contêiner
COPY . .

# Expor a porta padrão do FastAPI
EXPOSE 8000

# Definir a variável de ambiente para melhor saída de logs
ENV PYTHONUNBUFFERED 1

# Comando de inicialização
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
