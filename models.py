from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Text
from database import Base



class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, unique=True)

    alimentos = relationship("Alimento", back_populates="categoria")


class Alimento(Base):
    __tablename__ = "alimentos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)

    calorias = Column(Float)
    proteinas = Column(Float)
    carboidratos = Column(Float)
    gorduras = Column(Float)
    fibras = Column(Float)

    acucares = Column(Float)
    sodio = Column(Float)
    potassio = Column(Float)
    calcio = Column(Float)
    ferro = Column(Float)
    magnesio = Column(Float)
    fosforo = Column(Float)

    vitamina_a = Column(Float)
    vitamina_c = Column(Float)

    porcao = Column(String)

    categoria_id = Column(Integer, ForeignKey("categorias.id"))

    # 👇 Coloque aqui dentro
    dados_json = Column(Text)

    categoria = relationship("Categoria", back_populates="alimentos")