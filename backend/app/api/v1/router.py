# backend/app/api/v1/router.py

from fastapi import APIRouter
from .endpoints import iniciacao, modelagem # Importe o novo módulo

api_router = APIRouter()

# Rotas do Módulo 1
api_router.include_router(iniciacao.router, prefix="/iniciacao", tags=["Iniciação e Levantamento"])

# Rotas do Módulo 2 (Nova inclusão)
api_router.include_router(modelagem.router, prefix="/modelagem", tags=["Modelagem e Especificação"])