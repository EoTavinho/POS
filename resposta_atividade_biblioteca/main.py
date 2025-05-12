from fastapi import FastAPI, HTTPException
from models import Usuario, Livro, Biblioteca, Emprestimo
from typing import List

app = FastAPI()

usuarios: List[Usuario] = []
livros: List[Livro] = []
bibliotecas: List[Biblioteca] = []
emprestimos: List[Emprestimo] = []

@app.get('/biblioteca/', response_model=List[Biblioteca])
def listar_biblioteca():
    return bibliotecas

@app.post('/biblioteca/')
def criar_biblioteca(nome:str):
    data = {
        'nome':nome,
        '':
        '':
        '':
    }
    bibliotecas.append(biblioteca)
    return biblioteca

@app.delete('/biblioteca/{nome}', response_model=Biblioteca)
def excluir_biblioteca(nome:str):
    for index, biblioteca in enumerate(Biblioteca):
        if biblioteca.nome == nome:
            return bibliotecas.pop(index)
    raise HTTPException(status_code=404, detail='Biblioteca não localizada')



@app.get('/usuario/{biblioteca}', response_model=List[Usuario])
def listar_usuario():
    for biblioteca in bibliotecas:
        if biblioteca.nome == biblioteca:
            return Biblioteca.usuarios
        else:

    return usuarios

@app.post('/usuario')
def criar_usuario(usuario:Usuario):
    usuarios.append(usuario)
    return usuario

@app.delete('/usuario/{username}', response_model=Usuario)
def excluir_usuario(username:str):
    for index, usuario in enumerate(Usuario):
        if usuario.username == username:
            return usuarios.pop(index)
    raise HTTPException(status_code=404, detail='Usuario não localizado')

@app.get('/livro/', response_model=List[Livro])
def listar_livro():
    return livros

@app.post('/livro/')
def criar_livro(livro:Livro):
    livros.append(livro)
    return livro


@app.delete('/livro/{titulo}', response_model=Livro)
def excluir_livro(titulo:str):
    for index, livro in enumerate(Livro):
        if livro.titulo == titulo:
            return livro.pop(index)
    raise HTTPException(status_code=404, detail='Livro não localizado')
