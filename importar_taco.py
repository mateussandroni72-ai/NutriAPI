import json

from database import SessionLocal
from models import Categoria, Alimento

db = SessionLocal()

with open("taco.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

categorias = {}

# Criar categorias
for item in dados:
    nome_categoria = item["category"]

    categoria = db.query(Categoria).filter(
        Categoria.nome == nome_categoria
    ).first()

    if not categoria:
        categoria = Categoria(nome=nome_categoria)
        db.add(categoria)
        db.commit()
        db.refresh(categoria)

    categorias[nome_categoria] = categoria.id

# Converter valores inválidos
def numero(valor):
    if isinstance(valor, (int, float)):
        return float(valor)
    return 0.0

# Importar alimentos
for item in dados:

    alimento = Alimento(
        nome=item["description"],
        calorias=numero(item["energy_kcal"]),
        proteinas=numero(item["protein_g"]),
        carboidratos=numero(item["carbohydrate_g"]),
        gorduras=numero(item["lipid_g"]),
        fibras=numero(item["fiber_g"]),

        acucares=0,
        sodio=numero(item["sodium_mg"]),
        potassio=numero(item["potassium_mg"]),
        calcio=numero(item["calcium_mg"]),
        ferro=numero(item["iron_mg"]),
        magnesio=numero(item["magnesium_mg"]),
        fosforo=numero(item["phosphorus_mg"]),

        vitamina_a=0,
        vitamina_c=numero(item["vitaminC_mg"]),

        porcao="100 g",

        categoria_id=categorias[item["category"]],

        dados_json=json.dumps(item, ensure_ascii=False)
    )

    db.add(alimento)

db.commit()

print(f"{len(dados)} alimentos importados com sucesso!")