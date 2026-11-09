# api-base

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-D71F00?logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> Production-ready FastAPI starter template. Fork this repository to bootstrap new APIs with a clean, layered architecture, database migrations, JWT authentication, and best-practice tooling out of the box.

## ✨ Why this template?

Setting up a new API usually means re-doing the same boilerplate: database wiring, migrations, auth, settings, and code quality. **api-base** gives you all of that in a maintainable, scalable layout — so you can focus on business logic from day one.

## 🧱 Tech Stack

| Layer | Technology |
|---|---|
| Web framework | FastAPI + Uvicorn |
| ORM | SQLAlchemy 2.0 |
| Migrations | Alembic |
| Database | PostgreSQL |
| Auth | JWT (`python-jose`) + Argon2 password hashing (`passlib`) |
| Validation | Pydantic |
| Code quality | Ruff, mypy, pre-commit |
| Testing | pytest + pytest-cov + httpx |

## 📁 Project Structure

```
src/
├── main.py            # App factory and entrypoint
├── settings.py        # Environment-based configuration
├── core/              # Cross-cutting concerns (config, security, deps)
├── models/            # SQLAlchemy ORM models
├── schemas/           # Pydantic schemas (request/response)
├── routes/            # API routers
├── services/          # Business logic
└── integrations/      # External service clients
alembic/               # Database migrations
pyproject.toml         # Dependencies and tooling config
```

Clean separation of concerns: routes handle HTTP, services hold the business rules, repositories/models talk to the database.

## 🚀 Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL running locally or via Docker

### Setup

```bash
# 1. Clone the template
git clone https://github.com/XVINILX/api-base.git my-new-api
cd my-new-api

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# 3. Install dependencies (core + dev tooling)
pip install -e ".[dev]"

# 4. Configure environment variables
cp .env.example .env   # set DATABASE_URL, JWT_SECRET, etc.

# 5. Run migrations
alembic upgrade head

# 6. Start the server
uvicorn src.main:app --reload
```

The API will be available at `http://localhost:8000` with interactive docs at `/docs` (Swagger UI).

### With Docker

```bash
docker compose up --build
```

## 🧪 Testing

```bash
# Run the test suite with coverage
pytest --cov=src --cov-report=term-missing

# Lint and type-check
ruff check .
mypy src/
```

## 🔐 Authentication

JWT-based authentication is pre-configured:
- `POST /auth/register` — create a user (password hashed with Argon2)
- `POST /auth/login` — obtain an access token
- Protected routes expect `Authorization: Bearer <token>`

## 📜 License

[MIT](LICENSE) — free to use in personal and commercial projects.

---

⭐ **Star this repo** if you found it useful for bootstrapping your own APIs!
