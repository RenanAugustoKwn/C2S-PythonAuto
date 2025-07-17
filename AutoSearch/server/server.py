import socket
import json
from sqlalchemy.orm import sessionmaker
from database.models import Vehicle, get_engine
from server.mcp_protocol import parse_request

engine = get_engine()
Session = sessionmaker(bind=engine)

def handle_client(conn):
    data = conn.recv(2048).decode()
    filters = parse_request(data)
    
    session = Session()
    query = session.query(Vehicle)

    for attr, val in filters.items():
        if hasattr(Vehicle, attr):
            query = query.filter(getattr(Vehicle, attr).ilike(f"%{val}%"))

    results = query.limit(10).all()
    output = [
        {
            "marca": v.marca,
            "modelo": v.modelo,
            "ano": v.ano,
            "cor": v.cor,
            "quilometragem": v.quilometragem,
            "preco": v.preco
        }
        for v in results
    ]
    conn.send(json.dumps(output, indent=2).encode())
    conn.close()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", 5555))
        s.listen()
        print("Servidor MCP ouvindo na porta 5555...")

        while True:
            conn, _ = s.accept()
            handle_client(conn)

if __name__ == "__main__":
    start_server()
