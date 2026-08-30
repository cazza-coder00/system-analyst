# backend/app/core/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

# Cria o motor (engine) de conexão com o PostgreSQL usando a URL das configurações
engine = create_engine(settings.DATABASE_URL)

# Cria a fábrica de sessões (SessionLocal). 
# autocommit=False e autoflush=False garantem o controle manual das transações.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base genérica que todos os nossos modelos ORM herdarão
Base = declarative_base()

# Função geradora para fornecer uma sessão do banco de dados por requisição (Dependency)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        # Garante que a conexão será fechada após o processamento da requisição
        db.close()