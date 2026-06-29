from pydantic import BaseModel


class CategoriaCreate(BaseModel):
    nome: str


class CategoriaResponse(BaseModel):
    id: int
    nome: str

    class Config:
        orm_mode = True


class AlimentoCreate(BaseModel):
    nome: str
    calorias: float
    proteinas: float
    carboidratos: float
    gorduras: float
    fibras: float

    acucares: float
    sodio: float
    potassio: float
    calcio: float
    ferro: float
    magnesio: float
    fosforo: float

    vitamina_a: float
    vitamina_c: float

    porcao: str

    categoria_id: int


class AlimentoResponse(AlimentoCreate):
    id: int

    class Config:
        orm_mode = True