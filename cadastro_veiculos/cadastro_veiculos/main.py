from fastapi import FastAPI,HTTPException
from models import Carro
from typing import List
app = FastAPI()
carros:List[Carro]=[]

@app.get("/carros",response_model=List[Carro])
def listar_carros():
    return carros

@app.get("/carros/{placa}",response_model=Carro)
def listar_carros( placa:str):
    for carro in carros:
        if carro.placa == placa:
            return carro
    raise HTTPException(404,"Não localizado")

@app.delete("/carros/{placa}", response_model=Carro)
def deletar_carro(placa: str):
    for i, carro in enumerate(carros):
        if carro.placa == placa:
            return carros.pop(i)
    raise HTTPException(404, "Não localizado")


@app.post("/carros", response_model=Carro)
def criar_carro(carro:Carro):
    carros.append(carro)
    return carro
    raise HTTPException(404,"Não localizado")

@app.put('/carros/{placa}', response_model=Carro)
def atualizar_carro(placa:str, atualizado:Carro):
    for i, carro in enumerate(carros):
        if carro.placa == placa:
            carros[i] = atualizado
            return atualizado
    raise HTTPException(404,"Não localizado")
        