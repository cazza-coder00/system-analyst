# backend/app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
# Importe o roteador da API v1 no topo do arquivo main.py
from app.api.v1.router import api_router

# ... (código existente do main.py) ...

# Registra todas as rotas da v1 no aplicativo FastAPI
app.include_router(api_router, prefix="/api/v1")

# Inicializa o framework FastAPI com metadados do projeto
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
    description="API para gestão do ciclo de vida de projetos de TI"
)

# Configuração de CORS (Cross-Origin Resource Sharing)
# Permite que o front-end (React) em outra porta se comunique com o back-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Em produção, alterar para a URL exata do front-end
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota de health check para validar se a API está no ar
@app.get("/")
def health_check():
    """
    Endpoint raiz para verificação de status do servidor.
    """
    return {"status": "ok", "mensagem": "API de Apoio a Projetos em execução."}