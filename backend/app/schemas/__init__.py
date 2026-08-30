# backend/app/schemas/__init__.py
# (Mantenha os imports do Módulo 1 e 2)

from .iniciacao import (
    StakeholderCreate, StakeholderResponse,
    GlossarioCreate, GlossarioResponse,
    RequisitoCreate, RequisitoResponse,
    UserStoryCreate, UserStoryResponse
)

from .modelagem import (
    ProcessoBPMNCreate, ProcessoBPMNResponse,
    TelaWireframeCreate, TelaWireframeResponse
)

# Adicione os imports do Módulo 3
from .execucao import (
    CasoTesteCreate, CasoTesteResponse,
    MudancaEscopoCreate, MudancaEscopoResponse
)