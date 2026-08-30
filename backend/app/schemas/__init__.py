# backend/app/schemas/__init__.py
# (Mantenha os imports dos Módulos 1, 2 e 3)

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

from .execucao import (
    CasoTesteCreate, CasoTesteResponse,
    MudancaEscopoCreate, MudancaEscopoResponse
)

# Adicione os imports do Módulo 4
from .encerramento import (
    TermoAceiteCreate, TermoAceiteResponse,
    LicaoAprendidaCreate, LicaoAprendidaResponse
)