# backend/app/schemas/__init__.py
# (Mantenha os imports do Módulo 1)

from .iniciacao import (
    StakeholderCreate, StakeholderResponse,
    GlossarioCreate, GlossarioResponse,
    RequisitoCreate, RequisitoResponse,
    UserStoryCreate, UserStoryResponse
)

# Adicione os imports do Módulo 2
from .modelagem import (
    ProcessoBPMNCreate, ProcessoBPMNResponse,
    TelaWireframeCreate, TelaWireframeResponse
)