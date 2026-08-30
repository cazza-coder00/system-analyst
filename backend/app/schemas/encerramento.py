# backend/app/schemas/encerramento.py

from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import date

# --- SCHEMAS PARA TERMOS DE ACEITE ---
class TermoAceiteBase(BaseModel):
    titulo_entrega: str = Field(..., max_length=150, description="Nome da entrega que está sendo validada")
    data_emissao: Optional[date] = None # Se não enviado, o banco preenche com a data atual
    status: Optional[str] = "Aguardando Assinatura"
    stakeholder_id: Optional[int] = None

class TermoAceiteCreate(TermoAceiteBase):
    """Schema para emissão de um novo termo de aceite."""
    pass

class TermoAceiteResponse(TermoAceiteBase):
    """Schema de retorno do termo de aceite criado."""
    id: int
    model_config = ConfigDict(from_attributes=True)


# --- SCHEMAS PARA LIÇÕES APRENDIDAS ---
class LicaoAprendidaBase(BaseModel):
    categoria: str = Field(..., max_length=50, description="Ex: Ponto Positivo, Ponto de Melhoria")
    descricao_fato: str = Field(..., description="O que ocorreu de fato")
    acao_recomendada: Optional[str] = Field(None, description="Recomendação para o futuro")

class LicaoAprendidaCreate(LicaoAprendidaBase):
    pass

class LicaoAprendidaResponse(LicaoAprendidaBase):
    id: int
    model_config = ConfigDict(from_attributes=True)