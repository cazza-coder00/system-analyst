# backend/app/schemas/modelagem.py

from pydantic import BaseModel, Field, HttpUrl, ConfigDict
from typing import Optional

# --- SCHEMAS PARA PROCESSOS BPMN ---
class ProcessoBPMNBase(BaseModel):
    nome: str = Field(..., max_length=100)
    descricao: Optional[str] = None
    # HttpUrl garante que o dado enviado seja um link da web válido
    link_diagrama: HttpUrl 
    requisito_id: Optional[int] = None

class ProcessoBPMNCreate(ProcessoBPMNBase):
    pass

class ProcessoBPMNResponse(ProcessoBPMNBase):
    id: int
    # Converte HttpUrl para string na resposta para facilitar o uso no front-end
    link_diagrama: str 
    model_config = ConfigDict(from_attributes=True)


# --- SCHEMAS PARA TELAS E WIREFRAMES ---
class TelaWireframeBase(BaseModel):
    codigo: str = Field(..., max_length=20)
    nome: str = Field(..., max_length=100)
    link_prototipo: HttpUrl
    user_story_id: Optional[int] = None

class TelaWireframeCreate(TelaWireframeBase):
    pass

class TelaWireframeResponse(TelaWireframeBase):
    id: int
    link_prototipo: str
    model_config = ConfigDict(from_attributes=True)