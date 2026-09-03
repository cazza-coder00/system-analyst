# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.api.v1.router import api_router

# 1. Primeiro cria a instância do FastAPI
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description="API para gestão do ciclo de vida de projetos de TI"
)

# 2. Configura os middlewares (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Permite requisições do front-end (React)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 3. Registra as rotas da API v1
app.include_router(api_router, prefix="/api/v1")

# 4. Rota raiz para verificação de status
@app.get("/")
def health_check():
    """Endpoint raiz para verificação de status do servidor."""
    return {"status": "ok", "mensagem": "API de Apoio a Projetos em execução."}