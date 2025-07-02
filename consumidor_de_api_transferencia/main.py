import requests

BASE_URL = "https://api.portaldatransparencia.gov.br/api-de-exemplo"
# Substitua pelo endpoint real da API de dados abertos do governo
HEADERS = {
    "chave-api-dados": "6c1cceef7135c31218252d7a884e204c"  # Adicione sua chave de API aqui
}

def consultar_bolsa_familia(cpf_ou_nis, mes, ano):
    url = f"{BASE_URL}/bolsa-familia/por-cpf-ou-nis"
    params = {"cpfNis": cpf_ou_nis, "mesAno": f"{ano}-{mes:02}"}
    response = requests.get(url, headers=HEADERS, params=params)
    return response.json()

def consultar_bolsa_familia_por_id(id_registro):
    url = f"{BASE_URL}/bolsa-familia/{id_registro}"
    response = requests.get(url, headers=HEADERS)
    return response.json()

def consultar_garantia_safra(cpf_ou_nis, mes, ano):
    url = f"{BASE_URL}/garantia-safra/por-cpf-ou-nis"
    params = {"cpfNis": cpf_ou_nis, "mesAno": f"{ano}-{mes:02}"}
    response = requests.get(url, headers=HEADERS, params=params)
    return response.json()

def consultar_seguro_defeso(cpf_ou_nis, mes, ano):
    url = f"{BASE_URL}/seguro-defeso/por-cpf-ou-nis"
    params = {"cpfNis": cpf_ou_nis, "mesAno": f"{ano}-{mes:02}"}
    response = requests.get(url, headers=HEADERS, params=params)
    return response.json()

def consultar_servidor_publico(cpf):
    url = f"{BASE_URL}/servidores/cpf/{cpf}"
    response = requests.get(url, headers=HEADERS)
    return response.json()


# Menu simples
def main():
    while True:
        print("\n--- CONSULTAS DISPONÍVEIS ---")
        print("1 - Bolsa Família por CPF/NIS")
        print("2 - Bolsa Família por ID")
        print("3 - Garantia Safra por CPF/NIS")
        print("4 - Seguro Defeso por CPF/NIS")
        print("5 - Servidor Público Federal por CPF")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            break

        if opcao == "1":
            cpf_nis = input("Informe CPF ou NIS: ")
            mes = int(input("Mês (1-12): "))
            ano = int(input("Ano (ex: 2025): "))
            print(consultar_bolsa_familia(cpf_nis, mes, ano))

        elif opcao == "2":
            id_registro = input("Informe o ID do registro: ")
            print(consultar_bolsa_familia_por_id(id_registro))

        elif opcao == "3":
            cpf_nis = input("Informe CPF ou NIS: ")
            mes = int(input("Mês (1-12): "))
            ano = int(input("Ano (ex: 2025): "))
            print(consultar_garantia_safra(cpf_nis, mes, ano))

        elif opcao == "4":
            cpf_nis = input("Informe CPF ou NIS: ")
            mes = int(input("Mês (1-12): "))
            ano = int(input("Ano (ex: 2025): "))
            print(consultar_seguro_defeso(cpf_nis, mes, ano))

        elif opcao == "5":
            cpf = input("Informe o CPF do servidor: ")
            print(consultar_servidor_publico(cpf))

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
