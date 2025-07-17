from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

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

def get_engine():
    return create_engine("sqlite:///data/carros.db")
