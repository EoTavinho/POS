from pydantic import BaseModel
from datetime import date
from typing import List

class Usuario(BaseModel):
    username:str
    password:str
    data_criacao:date

class Livro:
    titulo:str
    ano:int
    edicao:int


class Emprestimo:
    usuario:Usuario
    livro:Livro
    data_emprestimo:date

class Biblioteca:
    nome:str
    acervo:List[Livro]
    usuario:List[Usuario]
    emprestimo: List[Emprestimo]
    data_devolucao:date
