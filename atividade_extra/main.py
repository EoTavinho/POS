from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
from typing import Optional
import uvicorn

app = FastAPI()

# Carrega os dados do CSV
try:
    df = pd.read_csv('20250702_Pedidos_csv_2025.csv', sep=';', encoding='utf-16')
    # Converte todas as colunas para string para evitar problemas com tipos
    df = df.astype(str)
except Exception as e:
    print(f"Erro ao carregar o arquivo: {e}")
    df = pd.DataFrame()

# Modelo Pydantic para o pedido
class Pedido(BaseModel):
    IdPedido: str
    ProtocoloPedido: str
    Esfera: str
    UF: str
    Municipio: str
    OrgaoDestinatario: str
    Situacao: str
    DataRegistro: str
    PrazoAtendimento: str
    FoiProrrogado: str
    FoiReencaminhado: str
    FormaResposta: str
    OrigemSolicitacao: str
    IdSolicitante: str
    AssuntoPedido: str
    SubAssuntoPedido: str
    Tag: str
    DataResposta: str
    Decisao: str
    EspecificacaoDecisao: str

@app.get("/pedidos/{pedido_id}", response_model=Pedido)
async def get_pedido(pedido_id: str):
    if df.empty:
        raise HTTPException(status_code=500, detail="Dados não carregados corretamente")
    
    # Busca o pedido no DataFrame
    pedido = df[df['IdPedido'] == pedido_id]
    
    if pedido.empty:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    
    # Converte a primeira linha encontrada para dicionário
    pedido_dict = pedido.iloc[0].to_dict()
    
    return pedido_dict

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)