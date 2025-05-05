### Coding Dojo API

Nesse repositório estou incluindo o mínimo necessário para o desenvolvimento de uma aplicação REST API usando:
- Python
- UV como gerenciamento de dependências
- Docker
- Postgres

### Requisitos necessários:
---
- UV instalado -  [Link](https://docs.astral.sh/uv/)
- Docker instalado - [Link](https://docs.docker.com/engine/install/ubuntu/)
- Plugin Docker Compose instalado - [Link](https://docs.docker.com/compose/)


### Instruções de uso:
---
1. Baixe o repositório para o seu computador
2. No terminal, acesse o diretório criado
```bash
cd coding-dojo-api
```
3. Crie um arquivo **.env**
```bash
touch .env
```

  4. Coloque nesse arquivo .env as credenciais para uso no Postgres
```bash
POSTGRES_USER=admin
POSTGRES_PASSWORD=secret
POSTGRES_DB=mydatabase
POSTGRES_HOST=db
POSTGRES_PORT=5432
```
5.  Use o comando venv do UV para criar um ambiente virtual
```bash
uv venv
```
6. Crie o container no Docker para desenvolvimento:
```bash
docker compose up --build
```

