#pip install requests

import requests

if __name__ == "__main__":
    url = "http://127.0.0.1:8000"


while True:
    print('O que quer fazer?')
    print('''
            1 - Listar todos os livros
            2 - Pesquisa livro por título
            3 - Cadastrar um livro
            4 - Deletar um livro
            5 - Editar um livro
            6 - Sair''')
    res = input('Digite: ')
    
    if res == '1':
        r = requests.get(f"{url}/livros")
        print(r.text)
    elif res == '2':
        titulo = input('Digite o titulo do livro: ')
        r = requests.get(f"{url}/livros/{titulo}")
        print(r.status_code)
        print(r.text)
    elif res == '3':
        titulo = input('Titulo: ')
        ano = input('Ano: ')
        edicao = input('Edição: ')

        livro = {
        "titulo": titulo,
        "ano": ano,
        "edicao": edicao
    }      
        r = requests.post(f"{url}/livros",json=livro)
        print(r.status_code)
        print(r.text)
    elif res == '4':
        deletar = input('Digite o livro que quer deletar: ')
        r = requests.delete(f"{url}/livros/{deletar}")
        print(r.status_code)
    elif res == '5':
        titulo = input('Livro que deseja editar: ')
        novo_titulo = input('Insira o novo Titulo: ')
        novo_ano = input('Insira o novo ano: ')
        nova_edicao = input('Insira a nova edição: ')
        livro = {
            'titulo': novo_titulo,
            'ano': novo_ano,
            'edicao': nova_edicao
        }
        r = requests.put(f'{url}/livros/{titulo}', json=livro)
        print(r.status_code)
        print(r.text)
    elif res == '6':
        break