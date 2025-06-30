import requests

if __name__  == '__main__':
    url = 'http://127.0.0.1:8000'
    
while True:
    print('-- O que você deseja fazer? --')
    print('''
            1 - Listar todos os carros
            2 - Pesquisar carro
            3 - Cadastrar um carro
            4 - Deletar um carro
            5 - Editar um carro
            6 - Sair''')
    res = input('Digite: ')

    if res == '1':
        r = requests.get(f"{url}/carros")
        print(r.text)

    elif res == '2':
        placa = input('Digite a placa do carro: ')
        r = requests.get(f"{url}/carros/{placa}")
        print(r.status_code)
        print(r.text)

    elif res == '3':
        nome = input('Nome: ')
        marca = input('Marca: ')
        modelo = input('Modelo: ')
        placa = input('Placa: ')

        carro = {
        "nome": nome,
        "marca": marca,
        "modelo": modelo,
        "placa": placa
    }      
        r = requests.post(f"{url}/carros",json=carro)
        print(r.status_code)
        print(r.text)

    elif res == '4':
        deletar = input('Digite o carro que quer deletar: ')
        r = requests.delete(f"{url}/carros/{deletar}")
        print(r.status_code)

    elif res == '5':
        nome = input('Carro que deseja editar: ')
        novo_nome = input('Insira o novo nome: ')
        nova_marca = input('Insira a nova marca: ')
        novo_modelo = input('Insira o novo modelo: ')
        nova_placa = input('Insira a nova placa: ')
        carro = {
            'nome': novo_nome,
            'marca': nova_marca,
            'modelo': novo_modelo,
            'placa': nova_placa
        }
        r = requests.put(f'{url}/carros/{placa}', json=carro)
        print(r.status_code)
        print(r.text)

    elif res == '6':
        break