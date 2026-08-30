# backend/app/schemas/iniciacao.py

from pydantic import BaseModel, Field, ConfigDict
from typing import Optional, List
from enum import Enum

# Replicamos os Enums para validação de entrada
class TipoRequisito(str, Enum):
    FUNCIONAL = "Funcional"
    NAO_FUNCIONAL = "Não Funcional"
    REGRA_NEGOCIO = "Regra de Negócio"

class Prioridade(str, Enum):
    BAIXA = "Baixa"
    MEDIA = "Média"
    ALTA = "Alta"

# --- STAKEHOLDER SCHEMAS ---
class StakeholderBase(BaseModel):
    nome: str = Field(..., description="Nome do stakeholder", max_length=100)
    papel: str = Field(..., description="Papel no projeto (ex: Patrocinador, Usuário Chave)", max_length=100)
    expectativa: Optional[str] = None
    nivel_poder_interesse: Optional[str] = None

class StakeholderCreate(StakeholderBase):
    """Schema usado para criar um novo Stakeholder (POST)"""
    pass

class StakeholderResponse(StakeholderBase):
    """Schema usado para retornar os dados do Stakeholder (GET)"""
    id: int
    
    # Permite que o Pydantic leia dados de objetos ORM (SQLAlchemy)
    model_config = ConfigDict(from_attributes=True)


# --- GLOSSÁRIO SCHEMAS ---
class GlossarioBase(BaseModel):
    termo: str = Field(..., max_length=100)
    definicao: str
    contexto_negocio: Optional[str] = Field(None, max_length=200)

class GlossarioCreate(GlossarioBase):
    pass

class GlossarioResponse(GlossarioBase):
    id: int
    model_config = ConfigDict(from_attributes=True)


# --- REQUISITO SCHEMAS ---
class RequisitoBase(BaseModel):
    codigo: str = Field(..., max_length=20)
    tipo: TipoRequisito
    descricao: str
    prioridade: Prioridade
    status: Optional[str] = "Em Levantamento"
    stakeholder_id: Optional[int] = None

class RequisitoCreate(RequisitoBase):
    pass

class RequisitoResponse(RequisitoBase):
    id: int
    # Opcional: incluir os dados do stakeholder aninhados na resposta
    responsavel: Optional[StakeholderResponse] = None
    model_config = ConfigDict(from_attributes=True)


# --- USER STORY SCHEMAS ---
class UserStoryBase(BaseModel):
    codigo: str = Field(..., max_length=20)
    ator: str = Field(..., max_length=100)
    acao: str
    beneficio: str
    criterio_aceite: Optional[str] = None
    requisito_id: Optional[int] = None

class UserStoryCreate(UserStoryBase):
    pass

class UserStoryResponse(UserStoryBase):
    id: int
    requisito: Optional[RequisitoResponse] = None
    model_config = ConfigDict(from_attributes=True)