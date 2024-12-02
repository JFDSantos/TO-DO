# To-Do Application API

Este projeto é uma API para gerenciar uma aplicação de tarefas (To-Do), construída utilizando **FastAPI**. A API permite criar, listar, editar e excluir tarefas, com integração com **PostgreSQL** e **Redis** para armazenamento e cache. O sistema está configurado para funcionar tanto em ambientes locais com docker quanto na nuvem com o **Azure**.

## Tecnologias Utilizadas

- **FastAPI**: Framework moderno e de alto desempenho para a construção de APIs com Python. Escolhido por sua rapidez, segurança e facilidade de uso.
- **Docker**: Utilizado para criar containers de serviços, garantindo um ambiente isolado e replicável para os serviços de banco de dados e cache.
- **PostgreSQL**: Banco de dados relacional utilizado para armazenar as tarefas.
- **Redis**: Cache de alto desempenho utilizado para armazenar dados frequentemente acessados e otimizar as respostas.
- **SQLAlchemy**: ORM (Object-Relational Mapping) utilizado para interagir com o banco de dados PostgreSQL de forma eficiente.
- **Uvicorn**: Servidor ASGI usado para rodar a aplicação FastAPI.
- **Docker Compose**: Ferramenta para orquestrar múltiplos containers (PostgreSQL, Redis e a aplicação) em um único comando, simplificando a configuração do ambiente.
- **Azure**: Plataforma de nuvem onde o ambiente de produção é configurado para escalar e gerenciar os recursos de forma eficiente.
    - **Azure App Service**: Plataforma oferece diversas funcionalidades para hospedar e gerenciar seus aplicativos de forma escalável e segura.
    - **Azure App Service**:Plataforma oferece uma instância do Redis que é gerenciada pelo Azure, eliminando a necessidade de configurar, gerenciar e manter o Redis manualmente.
    - **Azure Database for PostgreSQL Flexible Server**: O Flexible Server é uma das opções de banco de dados gerenciado do Azure, projetada para fornecer flexibilidade e controle sobre a configuração do banco de dados, com alta disponibilidade e facilidade de gerenciamento.

## Workflow de Desenvolvimento e Produção

### Desenvolvimento Local

O ambiente local é configurado com **Docker Compose**, o que permite rodar os serviços de banco de dados, cache e a API em containers separados. Esse setup é ideal para desenvolvimento e testes antes de rodar na nuvem.

#### Diferença de Ambientes Local e Produção

- **Local**: Durante o desenvolvimento local, os containers de PostgreSQL e Redis são configurados com senhas e configurações específicas, mas são isolados e não precisam de certificados SSL. O ambiente local também é configurado com variáveis de ambiente que podem ser facilmente manipuladas em um arquivo `.env` ou diretamente no Docker Compose.
  
- **Produção (Azure)**: No ambiente de produção, as credenciais e variáveis sensíveis são gerenciadas de maneira segura utilizando serviços como **Azure App Configuration**. Além disso, a API é configurada para utilizar SSL para comunicação segura com os clientes e para acessar o banco de dados e o Redis. O Azure também gerencia o escalonamento automático de recursos, como contêineres e máquinas virtuais.

### Como Funciona o Docker Compose

O **Docker Compose** é utilizado para orquestrar todos os containers necessários para rodar a aplicação. Ele cria um ambiente isolado, facilitando a configuração e a comunicação entre os serviços de forma simples. O `docker-compose.yml` inclui os serviços do **PostgreSQL**, **Redis** e da própria **API**.

## Instalação Local
### Passo 1: Clonar o Repositório

Clone o repositório do projeto para sua máquina local:

```bash
git clone https://github.com/JFDSantos/TO-DO.git
cd to-do
```

### Passo 2: Instalar as dependências
Instale as dependências:
```bash
pip install --no-cache-dir --upgrade pip
pip install -r requirements.txt
pip install psycopg2-binary
pip install python-multipart 
pip install redis
```

### Passo 3: Subir os containers
Suba os containers do docker:
```bash
docker-compose up -d
```

### Passo 4: Inicializar a aplicação
Inicialize a aplicação localmente
```bash
uvicorn app.main:app --reload
```

### Passo 5: Acessar a aplicação
Acesse o endereço: http://127.0.0.1:8000/docs

## Visualização na Nuvem
### Passo 1: Acessar a API 

Link para acesso: https://to-do-g3h2b8hrfcayd4d5.eastus2-01.azurewebsites.net/docs

## Documentação das Rotas/Endpoints
### POST /tasks

Cria uma nova tarefa.

```json
{
  "title": "Título da tarefa",
  "description": "Descrição da tarefa",
  "completed": false
}
```

### POST /tasks
Cria uma nova tarefa.

```json
{
  "title": "Título da tarefa",
  "description": "Descrição da tarefa",
  "completed": false
}
```

Resposta:

```json
{
  "id": 1,
  "title": "Título da tarefa",
  "description": "Descrição da tarefa",
  "completed": false,
  "created_at": "2024-12-01T12:00:00Z",
  "updated_at": "2024-12-01T12:00:00Z"
}
```

### GET /tasks
Retorna uma lista de todas as tarefas.

Resposta:

```json
[
  {
    "id": 1,
    "title": "Título da tarefa",
    "description": "Descrição da tarefa",
    "completed": false,
    "created_at": "2024-12-01T12:00:00Z",
    "updated_at": "2024-12-01T12:00:00Z"
  },
  {
    "id": 2,
    "title": "Outra tarefa",
    "description": "Descrição da outra tarefa",
    "completed": true,
    "created_at": "2024-12-01T12:00:00Z",
    "updated_at": "2024-12-01T12:00:00Z"
  }
]
```

### PUT /tasks/{task_id}
Atualiza uma tarefa existente.

Parâmetros:
task_id (int): ID da tarefa.
```json
{
  "title": "Título atualizado",
  "description": "Descrição atualizada",
  "completed": true
}
```

Resposta:

```json
{
  "id": 1,
  "title": "Título atualizado",
  "description": "Descrição atualizada",
  "completed": true,
  "created_at": "2024-12-01T12:00:00Z",
  "updated_at": "2024-12-01T12:00:00Z"
}
```

### DELETE /tasks/{task_id}
Exclui uma tarefa existente.

Parâmetros:
task_id (int): ID da tarefa.

Resposta:
```json
{
  "message": "Tarefa excluída com sucesso"
}

```

## Tecnologias Utilizadas e Justificativas
### 1. FastAPI
Por que usar: O FastAPI foi escolhido pela sua facilidade de uso, desempenho e pela geração automática de documentação com o Swagger. Ele também oferece validação de dados baseada em Pydantic, que melhora a confiabilidade da API.
### 2. Docker
Por que usar: O Docker foi utilizado para criar containers isolados para cada serviço (PostgreSQL, Redis e o app). Isso facilita a configuração, torna o ambiente replicável em qualquer lugar e elimina problemas de "funciona na minha máquina".
### 3. PostgreSQL
Por que usar: O PostgreSQL foi escolhido por ser um banco de dados relacional robusto, amplamente utilizado em aplicações modernas. Ele também é facilmente integrável com o SQLAlchemy e fornece escalabilidade e confiabilidade.
### 4. Redis
Por que usar: O Redis foi integrado como uma camada de cache para melhorar a performance da API. Ele armazena dados frequentemente acessados em memória, permitindo respostas rápidas para consultas repetidas.
### 5. SQLAlchemy
Por que usar: O SQLAlchemy foi escolhido como ORM devido à sua flexibilidade e capacidade de trabalhar bem com o PostgreSQL. Ele facilita a criação e manutenção do esquema de banco de dados, além de simplificar a manipulação dos dados.
### 6. Uvicorn
Por que usar: O Uvicorn é um servidor ASGI rápido e leve, que é ideal para aplicações assíncronas como o FastAPI. Ele é muito rápido e suporta escalabilidade em ambientes de produção.
### 7. Psycopg / Psycopg2
Ideal para interações síncronas com PostgreSQL. Oferece desempenho e confiabilidade, mas exige mais código para gerenciamento de transações e conexões.
### 8. Databases: 
Ideal para aplicações assíncronas. Ele abstrai o uso do banco de dados e oferece uma interface mais simples e intuitiva, enquanto o psycopg faz o trabalho de comunicação com o banco por trás.