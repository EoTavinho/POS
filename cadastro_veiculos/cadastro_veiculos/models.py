from pydantic import BaseModel

class Carro(BaseModel):
    nome:str
    marca:str
    modelo:str
    placa:str