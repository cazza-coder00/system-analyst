# backend/app/api/v1/router.py

from fastapi import APIRouter
from .endpoints import iniciacao, modelagem, execucao # Adicione a importação de execucao

api_router = APIRouter()

# Módulo 1
api_router.include_router(iniciacao.router, prefix="/iniciacao", tags=["Iniciação e Levantamento"])

# Módulo 2
api_router.include_router(modelagem.router, prefix="/modelagem", tags=["Modelagem e Especificação"])

# Módulo 3 (Nova inclusão)
api_router.include_router(execucao.router, prefix="/execucao", tags=["Execução e Homologação"])