import json

from database import SessionLocal
from models import Categoria, Alimento


def importar_taco():
    db = SessionLocal()

    # Se já existem alimentos, não importa novamente
    if db.query(Alimento).count() > 0:
        db.close()
        return

    with open("taco.json", "r", encoding="utf-8") as f:
        dados = json.load(f)

    categorias = {}

    for item in dados:

        nome_categoria = item["category"]

        if nome_categoria not in categorias:

            categoria = Categoria(nome=nome_categoria)

            db.add(categoria)
            db.commit()
            db.refresh(categoria)

            categorias[nome_categoria] = categoria

        alimento = Alimento(
            nome=item["description"],
            calorias=float(item["energy_kcal"] or 0),
            proteinas=float(item["protein_g"] or 0),
            carboidratos=float(item["carbohydrate_g"] or 0),
            gorduras=float(item["lipid_g"] or 0),
            fibras=float(item["fiber_g"] or 0),
            categoria_id=categorias[nome_categoria].id
        )

        db.add(alimento)

    db.commit()
    db.close()

    print("TACO importada com sucesso.")