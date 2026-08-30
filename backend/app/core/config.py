# backend/app/core/config.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Nome e versão do projeto para a documentação automática do Swagger
    PROJECT_NAME: str = "Sistema de Apoio a Projetos TI"
    PROJECT_VERSION: str = "1.0.0"
    
    # URL de conexão com o banco de dados PostgreSQL
    # Formato padrão: postgresql://usuario:senha@host:porta/nome_banco
    DATABASE_URL: str = "postgresql://postgres:admin@localhost:5432/db_projetos"

    class Config:
        # Define que o Pydantic pode buscar essas variáveis em um arquivo .env
        env_file = ".env"

# Instancia as configurações para serem importadas globalmente
settings = Settings()