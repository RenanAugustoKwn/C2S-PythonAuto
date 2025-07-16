import socket
from client.agent import conversar
import json

def montar_requisicao(filtros: dict) -> str:
    filtros_str = ";".join(f"{k}={v}" for k, v in filtros.items())
    return f"MCP/1.0 FILTER {filtros_str}"

def main():
    filtros = conversar()
    req = montar_requisicao(filtros)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(("localhost", 5555))
        s.send(req.encode())
        resposta = s.recv(4096).decode()

    resultados = json.loads(resposta)
    if not resultados:
        print("🚫 Nenhum veículo encontrado com esses critérios.")
    else:
        print("✅ Veículos encontrados:")
        for v in resultados:
            print(f"- {v['marca']} {v['modelo']} {v['ano']} - {v['cor']} - {v['quilometragem']}km - R$ {v['preco']:.2f}")

if __name__ == "__main__":
    main()
