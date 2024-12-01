# Usar uma imagem oficial do Python como base
FROM python:3.10-slim

# Atualizar o sistema e instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean

# Configuração do diretório de trabalho
WORKDIR /app

# Copiar os arquivos da aplicação
COPY . /app

# Instalar as dependências da aplicação
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Expor a porta padrão do FastAPI
EXPOSE 80

# Comando de inicialização
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
