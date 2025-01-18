# Guardião API

Guardião é uma API desenvolvida com **FastAPI** e **SQLAlchemy** para gerenciar agendamentos de salas e eventos.

## Recursos

- Criar agendamentos.
- Listar agendamentos existentes.
- Conexão com banco de dados PostgreSQL.
- Persistência e gerenciamento de dados utilizando SQLAlchemy ORM.

## Pré-requisitos

- **Python 3.9+**
- **PostgreSQL**
- **Docker** (opcional, para uso com Docker Compose)

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/iot-guardiao/guardiao-api-fastapi.git
   cd guardiao-api-fastapi
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/MacOS
   .venv\Scripts\activate     # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure o banco de dados:
   - Crie um arquivo `.env` na raiz do projeto com a variável de conexão:
     ```env
     DB_URI=postgresql+psycopg2://guardiao_user:guardiao_password@0.0.0.0:5432/guardiao_db
     ```

5. Execute o servidor:
   ```bash
   uvicorn main:app --reload
   ```

6. Acesse a documentação interativa:
   - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Uso com Docker

1. Certifique-se de ter o **Docker** e o **Docker Compose** instalados.

2. Suba os serviços:
   ```bash
   docker-compose up -d
   ```

3. Acesse a documentação interativa da API:
   - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)

---

## Contribuindo

1. Faça um fork do projeto.
2. Crie uma nova branch para a sua feature ou correção:
   ```bash
   git checkout -b minha-feature
   ```
3. Commit suas alterações:
   ```bash
   git commit -m "Minha nova feature"
   ```
4. Envie suas alterações:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request no repositório original.

