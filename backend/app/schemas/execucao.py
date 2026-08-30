# backend/app/schemas/execucao.py

from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from enum import Enum

# Replicamos o Enum de status para validação de entrada
class StatusTeste(str, Enum):
    PENDENTE = "Pendente"
    APROVADO = "Aprovado"
    REPROVADO = "Reprovado"

# --- SCHEMAS PARA CASOS DE TESTE (BDD) ---
class CasoTesteBase(BaseModel):
    codigo: str = Field(..., max_length=20)
    cenario: str = Field(..., max_length=150, description="Nome ou resumo do cenário de teste")
    dado_que: str = Field(..., description="Contexto inicial (Given)")
    quando: str = Field(..., description="Ação executada (When)")
    entao: str = Field(..., description="Resultado esperado (Then)")
    status: Optional[StatusTeste] = StatusTeste.PENDENTE
    user_story_id: Optional[int] = None

class CasoTesteCreate(CasoTesteBase):
    """Schema para cadastro de um novo caso de teste."""
    pass

class CasoTesteResponse(CasoTesteBase):
    """Schema de retorno com os dados persistidos."""
    id: int
    model_config = ConfigDict(from_attributes=True)


# --- SCHEMAS PARA MUDANÇAS DE ESCOPO (CHANGE REQUESTS) ---
class MudancaEscopoBase(BaseModel):
    motivo: str = Field(..., description="Justificativa para a mudança")
    impacto_estimado: Optional[str] = Field(None, max_length=100)
    status_aprovacao: Optional[str] = "Em Análise"
    requisito_id: Optional[int] = None

class MudancaEscopoCreate(MudancaEscopoBase):
    pass

class MudancaEscopoResponse(MudancaEscopoBase):
    id: int
    model_config = ConfigDict(from_attributes=True)