
from sqlmodel import Field, SQLModel, create_engine, Session, select
from fastapi import FastAPI, HTTPException
from typing import Optional
import pandas as pd
from pathlib import Path

app = FastAPI()
database = "sqlite:///pedidos.db"
engine = create_engine(database, echo=False)
csv_pacote = Path(__file__).with_name("20250702_Pedidos_csv_2025.csv")

class Pedido(SQLModel, table=True):
    id_pedido: int = Field(alias="IdPedido", primary_key=True)
    protocolo: str = Field(alias="ProtocoloPedido")
    esfera: str
    uf: Optional[str] = None
    municipio: Optional[str] = None
    orgao_destinatario: Optional[str] = Field(alias="OrgaoDestinatario", default=None)
    situacao: str
    data_registro: str = Field(alias="DataRegistro")
    assunto: Optional[str] = None
    descricao: Optional[str] = None
    tag: Optional[str] = None
    data_resposta: Optional[str] = Field(alias="DataResposta", default=None)
    decisao: Optional[str] = None
    especificacao_decisao: Optional[str] = Field(alias="EspecificacaoDecisao", default=None)

SQLModel.metadata.create_all(engine)

def carregar_dados():
    with Session(engine) as session:
        if session.exec(select(Pedido).limit(1)).first():
            return
        df = pd.read_csv(csv_pacote, sep=";", encoding="utf-16")
        df = df.rename(columns=str.strip)
        for _, linha in df.iterrows():
            pedido = Pedido(
                id_pedido=linha["IdPedido"],
                protocolo=linha["ProtocoloPedido"],
                esfera=linha["Esfera"],
                uf=linha.get("UF"),
                municipio=linha.get("Municipio"),
                orgao_destinatario=linha.get("OrgaoDestinatario"),
                situacao=linha["Situacao"],
                data_registro=linha["DataRegistro"],
                assunto=linha.get("Assunto"),
                descricao=linha.get("Descricao"),
                tag=linha.get("Tag"),
                data_resposta=linha.get("DataResposta"),
                decisao=linha.get("Decisao"),
                especificacao_decisao=linha.get("EspecificacaoDecisao"),
            )
            session.add(pedido)
        session.commit()

carregar_dados()

@app.get("/pedidos/{id_pedido}", response_model=Pedido)
def get_pedido(id_pedido: int):
    engine = create_engine(database, echo=False)
    with Session(engine) as session:
        pedido = session.get(Pedido, id_pedido)
        if not pedido:
            raise HTTPException(status_code=404, detail="Pedido não encontrado")
        return pedido