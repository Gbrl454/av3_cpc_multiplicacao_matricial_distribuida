import socket
import sys
from matrix import matrix_multiply
from socket_utils import send_packet, recv_packet

HOST = "127.0.0.1"


def start_server(port):
    vm_id = f"VM-{port}"
    print(f"[{vm_id}] Servidor iniciado na porta {port}")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, port))
        server.listen()

        while True:
            conn, addr = server.accept()
            print(f"[{vm_id}] Conexão de {addr}")

            with conn:
                part = recv_packet(conn)
                if part is None:
                    continue

                print(f"Foram recebidas {len(part)} sub-problemas")

                results = []
                for m1, m2, (x, y) in part:
                    r = matrix_multiply(m1, m2)[0][0]
                    results.append((r, x, y))

                send_packet(conn, results)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    port = int(sys.argv[1])
    start_server(port)
