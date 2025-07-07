import requests
import sys

def consultar_pedido():
    BASE_URL = "http://localhost:8000"
    
    if len(sys.argv) > 1:
        pedido_id = sys.argv[1]
    else:
        pedido_id = input("Digite o ID do pedido: ")
    
    try:
        response = requests.get(f"{BASE_URL}/pedidos/{pedido_id}")
        response.raise_for_status()
        
        pedido = response.json()
        
        print("\nDados do Pedido:")
        print("----------------")
        for key, value in pedido.items():
            print(f"{key}: {value}")
            
    except requests.exceptions.HTTPError as err:
        if err.response.status_code == 404:
            print(f"\nErro: Pedido com ID {pedido_id} não encontrado.")
        else:
            print(f"\nErro na requisição: {err}")
    except requests.exceptions.RequestException as err:
        print(f"\nErro ao conectar com a API: {err}")

if __name__ == "__main__":
    consultar_pedido()