# Use uma imagem oficial do Python
FROM python:3.10-slim

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie os arquivos do projeto para o contêiner
COPY . /app

# Atualize o sistema e instale as dependências do sistema necessárias
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Instale as dependências do Python
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Exponha a porta para a aplicação FastAPI (geralmente 8000 por padrão no FastAPI)
EXPOSE 8000

# Comando para rodar a aplicação FastAPI com Uvicorn
CMD ["uvicorn", "main:app", "--reload"]
