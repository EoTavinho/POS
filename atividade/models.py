from pydantic import BaseModel
from datetime import date

class Carro(BaseModel):
    id:int
    modelo:str
    marca:str
    ano:int
    disponivel:bool
class Cliente(BaseModel):
    id:int
    nome:str
    cpf:str
    telefone:str

class Reserva(BaseModel):
    id:int
    cliente_id:int
    carro_id:int
    data_inicio:date
    data_fim:date  