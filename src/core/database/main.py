# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:asd@localhost:5432/meubanco")
print(DATABASE_URL)
engine = create_engine(DATABASE_URL)

# Criar sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criar base para os modelos
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()