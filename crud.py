from sqlalchemy.orm import Session
from models import Categoria, Alimento


def criar_categoria(db: Session, nome: str):
    categoria = Categoria(nome=nome)
    db.add(categoria)
    db.commit()
    db.refresh(categoria)
    return categoria


def listar_categorias(db: Session):
    return db.query(Categoria).all()


def criar_alimento(db: Session, dados):
    alimento = Alimento(**dados.dict())
    db.add(alimento)
    db.commit()
    db.refresh(alimento)
    return alimento


def listar_alimentos(db: Session):
    return db.query(Alimento).all()
    
    
def buscar_alimento(db: Session, alimento_id: int):
    return db.query(Alimento).filter(
        Alimento.id == alimento_id
    ).first()
    
    
    
def calcular_alimento(db, alimento_id: int, gramas: float):
    alimento = buscar_alimento(db, alimento_id)

    if alimento is None:
        return None

    fator = gramas / 100

    return {
        "id": alimento.id,
        "nome": alimento.nome,
        "gramas": gramas,
        "calorias": round(alimento.calorias * fator, 2),
        "proteinas": round(alimento.proteinas * fator, 2),
        "carboidratos": round(alimento.carboidratos * fator, 2),
        "gorduras": round(alimento.gorduras * fator, 2),
        "fibras": round(alimento.fibras * fator, 2)
    }
    
def buscar_por_nome(db, nome: str):
    return (
        db.query(Alimento)
        .filter(Alimento.nome.ilike(f"%{nome}%"))
        .all()
    )