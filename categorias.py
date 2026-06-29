from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from .. import schemas
from ..services.categoria_service import CategoriaService

router = APIRouter(
    prefix="/categorias",
    tags=["Categorias"]
)

@router.get("/", response_model=List[schemas.Categoria])
def listar_categorias(db: Session = Depends(get_db)):
    """Retorna todas as categorias ativas."""
    return CategoriaService.listar_todas(db)

@router.post("/", response_model=schemas.Categoria, status_code=status.HTTP_201_CREATED)
def criar_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    """Cria uma nova categoria de alimentos."""
    return CategoriaService.criar(db, categoria)