# backend/app/api/v1/router.py

from fastapi import APIRouter
from .endpoints import iniciacao

# Cria o roteador principal da API v1
api_router = APIRouter()

# Inclui as rotas do módulo de iniciação com um prefixo e uma tag para organização no Swagger
api_router.include_router(iniciacao.router, prefix="/iniciacao", tags=["Iniciação e Levantamento"])