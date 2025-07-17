from faker import Faker
import random
from models import Vehicle, Base, get_engine
from sqlalchemy.orm import sessionmaker

faker = Faker()
engine = get_engine()
Session = sessionmaker(bind=engine)

def populate():
    Base.metadata.create_all(engine)
    session = Session()

    marcas_modelos = {
        "Toyota": ["Corolla", "Etios", "Yaris"],
        "Ford": ["Ka", "Fiesta", "Focus"],
        "Chevrolet": ["Onix", "Prisma", "Cruze"]
    }

    for _ in range(100):
        marca = random.choice(list(marcas_modelos.keys()))
        modelo = random.choice(marcas_modelos[marca])
        ano = random.randint(2005, 2023)
        motorizacao = f"{random.choice([1.0, 1.6, 2.0])}L"
        combustivel = random.choice(["Gasolina", "Etanol", "Flex"])
        cor = random.choice(["Prata", "Preto", "Branco", "Vermelho", "Azul"])
        km = random.randint(10000, 200000)
        portas = random.choice([2, 4])
        transm = random.choice(["Manual", "Automático"])
        preco = round(random.uniform(20000, 100000), 2)

        v = Vehicle(
            marca=marca,
            modelo=modelo,
            ano=ano,
            motorizacao=motorizacao,
            combustivel=combustivel,
            cor=cor,
            quilometragem=km,
            num_portas=portas,
            transmissao=transm,
            preco=preco
        )
        session.add(v)

    session.commit()
    session.close()

if __name__ == "__main__":
    populate()
