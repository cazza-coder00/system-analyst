# backend/app/api/v1/endpoints/modelagem.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.models import modelagem as models
from app.schemas import modelagem as schemas

router = APIRouter()

# --- ROTAS PARA PROCESSOS BPMN ---

@router.post("/processos/", response_model=schemas.ProcessoBPMNResponse, status_code=status.HTTP_201_CREATED)
def criar_processo(processo: schemas.ProcessoBPMNCreate, db: Session = Depends(get_db)):
    """
    Cadastra um novo fluxo de processo BPMN.
    """
    # Convertemos os dados do schema para um dicionário
    processo_data = processo.model_dump()
    # O HttpUrl do Pydantic precisa ser convertido para string antes de salvar no banco
    processo_data['link_diagrama'] = str(processo_data['link_diagrama'])
    
    db_processo = models.ProcessoBPMN(**processo_data)
    db.add(db_processo)
    db.commit()
    db.refresh(db_processo)
    return db_processo

@router.get("/processos/", response_model=List[schemas.ProcessoBPMNResponse])
def listar_processos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Lista os processos BPMN cadastrados."""
    return db.query(models.ProcessoBPMN).offset(skip).limit(limit).all()


# --- ROTAS PARA TELAS E WIREFRAMES ---

@router.post("/telas/", response_model=schemas.TelaWireframeResponse, status_code=status.HTTP_201_CREATED)
def criar_tela(tela: schemas.TelaWireframeCreate, db: Session = Depends(get_db)):
    """
    Cadastra um novo protótipo de tela. Valida se o código da tela é único.
    """
    tela_existente = db.query(models.TelaWireframe).filter(models.TelaWireframe.codigo == tela.codigo).first()
    if tela_existente:
        raise HTTPException(status_code=400, detail="Código de tela já cadastrado.")
    
    tela_data = tela.model_dump()
    tela_data['link_prototipo'] = str(tela_data['link_prototipo'])

    db_tela = models.TelaWireframe(**tela_data)
    db.add(db_tela)
    db.commit()
    db.refresh(db_tela)
    return db_tela

@router.get("/telas/", response_model=List[schemas.TelaWireframeResponse])
def listar_telas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Lista as telas e wireframes cadastrados."""
    return db.query(models.TelaWireframe).offset(skip).limit(limit).all()