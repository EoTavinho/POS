import requests

BASE_URL = "http://127.0.0.1:8000/pedidos/"

def main() -> None:
    while True:
        try:
            pedido_id = int(input("\nDigite o IdPedido (0 para sair): "))
        except ValueError:
            print("❌  Id inválido — digite apenas números!")
            continue
        if pedido_id == 0:
            break

        resp = requests.get(BASE_URL + str(pedido_id))
        if resp.status_code == 404:
            print("⚠️  Pedido não encontrado!")
        elif resp.ok:
            dados = resp.json()
            print("\n📦  Pedido:", dados["id_pedido"])
            print("      Protocolo :", dados["protocolo"])
            print("      Órgão     :", dados["orgao_destinatario"])
            print("      Assunto   :", dados.get("assunto") or "(vazio)")
            print("      Decisão   :", dados.get("decisao")  or "(vazio)")
        else:
            print("❌  Erro:", resp.status_code, resp.text)

if __name__ == "__main__":
    main()
