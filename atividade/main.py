from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from datetime import date
from typing import List, Dict, Optional

app = FastAPI()

class Carro(BaseModel):
    id: int
    modelo: str
    marca: str
    ano: int
    disponivel: bool = True

class Cliente(BaseModel):
    id: int
    nome: str
    cpf: str
    telefone: str

class Reserva(BaseModel):
    id: int
    cliente_id: int
    carro_id: int
    data_inicio: date
    data_fim: date

carros_db: List[Carro] = []
clientes_db: List[Cliente] = []
reservas_db: List[Reserva] = []
id_counter = {"carro": 1, "cliente": 1, "reserva": 1}

@app.get("/carros", response_model=List[Carro])
def listar_carros():
    return carros_db

@app.post("/carros", status_code=status.HTTP_201_CREATED, response_model=Carro)
def adicionar_carro(carro: Carro):
    carro.id = id_counter["carro"]
    id_counter["carro"] += 1
    carros_db.append(carro)
    return carro

@app.put("/carros/{id}", response_model=Carro)
def atualizar_carro(id: int, carro_atualizado: Carro):
    for idx, carro in enumerate(carros_db):
        if carro.id == id:
            carros_db[idx] = carro_atualizado
            return carro_atualizado
    raise HTTPException(status_code=404, detail="Carro não encontrado")

@app.delete("/carros/{id}", status_code=status.HTTP_204_NO_CONTENT)
def remover_carro(id: int):
    for idx, carro in enumerate(carros_db):
        if carro.id == id:
            for reserva in reservas_db:
                if reserva.carro_id == id and reserva.data_fim >= date.today():
                    raise HTTPException(
                        status_code=400,
                        detail="Não é possível remover um carro com reserva ativa"
                    )
            carros_db.pop(idx)
            return
    raise HTTPException(status_code=404, detail="Carro não encontrado")

@app.get("/carros/disponiveis", response_model=List[Carro])
def listar_carros_disponiveis():
    return [carro for carro in carros_db if carro.disponivel]

@app.get("/clientes", response_model=List[Cliente])
def listar_clientes():
    return clientes_db

@app.post("/clientes", status_code=status.HTTP_201_CREATED, response_model=Cliente)
def adicionar_cliente(cliente: Cliente):
    if any(c.cpf == cliente.cpf for c in clientes_db):
        raise HTTPException(
            status_code=400,
            detail="Já existe um cliente cadastrado com este CPF"
        )
    
    cliente.id = id_counter["cliente"]
    id_counter["cliente"] += 1
    clientes_db.append(cliente)
    return cliente

@app.get("/clientes/{id}", response_model=Cliente)
def buscar_cliente(id: int):
    for cliente in clientes_db:
        if cliente.id == id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente não encontrado")

@app.post("/reservas", status_code=status.HTTP_201_CREATED, response_model=Reserva)
def criar_reserva(reserva: Reserva):
    if reserva.data_fim < reserva.data_inicio:
        raise HTTPException(
            status_code=400,
            detail="Data de fim não pode ser anterior à data de início"
        )

    cliente_existe = any(c.id == reserva.cliente_id for c in clientes_db)
    if not cliente_existe:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    carro_encontrado = None
    for carro in carros_db:
        if carro.id == reserva.carro_id:
            carro_encontrado = carro
            break
    
    if not carro_encontrado:
        raise HTTPException(status_code=404, detail="Carro não encontrado")
    
    if not carro_encontrado.disponivel:
        raise HTTPException(status_code=400, detail="Carro não está disponível")

    for r in reservas_db:
        if r.carro_id == reserva.carro_id and not (
            reserva.data_fim < r.data_inicio or reserva.data_inicio > r.data_fim
        ):
            raise HTTPException(
                status_code=400,
                detail="Carro já reservado para este período"
            )

    reserva.id = id_counter["reserva"]
    id_counter["reserva"] += 1
    reservas_db.append(reserva)
    
    for idx, carro in enumerate(carros_db):
        if carro.id == reserva.carro_id:
            carros_db[idx].disponivel = False
            break
    
    return reserva

@app.get("/reservas", response_model=List[Reserva])
def listar_reservas():
    return reservas_db

@app.delete("/reservas/{id}", status_code=status.HTTP_204_NO_CONTENT)
def cancelar_reserva(id: int):
    for idx, reserva in enumerate(reservas_db):
        if reserva.id == id:
            for carro_idx, carro in enumerate(carros_db):
                if carro.id == reserva.carro_id:
                    carros_db[carro_idx].disponivel = True
                    break
            
            reservas_db.pop(idx)
            return
    
    raise HTTPException(status_code=404, detail="Reserva não encontrada")