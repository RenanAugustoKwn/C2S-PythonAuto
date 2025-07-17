from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Vehicle(Base):
    __tablename__ = 'carros'

    id = Column(Integer, primary_key=True)
    marca = Column(String)
    modelo = Column(String)
    ano = Column(Integer)
    motorizacao = Column(String)
    combustivel = Column(String)
    cor = Column(String)
    quilometragem = Column(Integer)
    num_portas = Column(Integer)
    transmissao = Column(String)
    preco = Column(Float)

def create_and_populate_db(db_path='carros.db'):
    engine = create_engine(f"sqlite:///{db_path}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    carros = [
        Vehicle(marca='Toyota', modelo='Corolla', ano=2020, motorizacao='1.8L', combustivel='Flex',
                cor='Prata', quilometragem=35000, num_portas=4, transmissao='Automático', preco=85000.0),
        Vehicle(marca='Ford', modelo='Fiesta', ano=2018, motorizacao='1.6L', combustivel='Gasolina',
                cor='Vermelho', quilometragem=60000, num_portas=4, transmissao='Manual', preco=45000.0),
        Vehicle(marca='Chevrolet', modelo='Onix', ano=2021, motorizacao='1.0L', combustivel='Flex',
                cor='Preto', quilometragem=20000, num_portas=4, transmissao='Automático', preco=70000.0),
        Vehicle(marca='Honda', modelo='Civic', ano=2019, motorizacao='2.0L', combustivel='Gasolina',
                cor='Branco', quilometragem=40000, num_portas=4, transmissao='Automático', preco=90000.0),
        Vehicle(marca='Volkswagen', modelo='Gol', ano=2017, motorizacao='1.6L', combustivel='Flex',
                cor='Azul', quilometragem=75000, num_portas=4, transmissao='Manual', preco=38000.0),
    ]

    session.add_all(carros)
    session.commit()
    session.close()
    print(f"Banco criado e populado em '{db_path}' com {len(carros)} veículos.")

if __name__ == '__main__':
    create_and_populate_db()
