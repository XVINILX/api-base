## Instalando dependências
pip install -e .

## Configurando banco de dados
alembic init ./src/base_project_user

### Criando migration
alembic revision --autogenerate -m "create users table"

## Aplicando Migração
alembic upgrade head
