
from contextlib import asynccontextmanager
from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from schemas import (
    CategoriaCreate,
    CategoriaResponse,
    AlimentoCreate,
    AlimentoResponse
)
import crud
from seed import importar_taco


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Cria as tabelas antes da importação
    Base.metadata.create_all(bind=engine)

    # Importa a TACO automaticamente se o banco estiver vazio
    importar_taco()

    yield


app = FastAPI(
    title="NutriAPI",
    version="2.2.0",
    lifespan=lifespan
)


@app.get("/")
def inicio():
    return {
        "mensagem": "NutriAPI funcionando com SQLite!"
    }


@app.get("/buscar", response_model=List[AlimentoResponse])
def buscar(
    nome: str,
    db: Session = Depends(get_db)
):
    return crud.buscar_por_nome(db, nome)


@app.post("/categorias", response_model=CategoriaResponse)
def criar_categoria(
    categoria: CategoriaCreate,
    db: Session = Depends(get_db)
):
    return crud.criar_categoria(db, categoria.nome)


@app.get("/categorias", response_model=list[CategoriaResponse])
def listar_categorias(
    db: Session = Depends(get_db)
):
    return crud.listar_categorias(db)


@app.post("/alimentos", response_model=AlimentoResponse)
def criar_alimento(
    alimento: AlimentoCreate,
    db: Session = Depends(get_db)
):
    return crud.criar_alimento(db, alimento)


@app.get("/alimentos", response_model=list[AlimentoResponse])
def listar_alimentos(
    db: Session = Depends(get_db)
):
    return crud.listar_alimentos(db)


@app.get("/alimentos/{alimento_id}", response_model=AlimentoResponse)
def buscar_alimento(
    alimento_id: int,
    db: Session = Depends(get_db)
):
    alimento = crud.buscar_alimento(db, alimento_id)

    if alimento is None:
        raise HTTPException(
            status_code=404,
            detail="Alimento não encontrado."
        )

    return alimento


@app.get("/calcular/{alimento_id}")
def calcular(
    alimento_id: int,
    gramas: float,
    db: Session = Depends(get_db)
):
    resultado = crud.calcular_alimento(
        db,
        alimento_id,
        gramas
    )

    if resultado is None:
        raise HTTPException(
            status_code=404,
            detail="Alimento não encontrado."
        )

    return resultado
