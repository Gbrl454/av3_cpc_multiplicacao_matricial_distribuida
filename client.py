import socket
from datetime import datetime
from save_json_util import save_json
from matrix import (
    get_matrix,
    get_row_length,
    get_column_length,
    get_row,
    get_column,
)
from concurrent.futures import ThreadPoolExecutor, as_completed
from socket_utils import send_packet, recv_packet, check_server_alive

MAX_CPU_CORES = 4
SERVERS = [("127.0.0.1", 5000 + i) for i in range(19)]


def get_available_servers(servers):
    return [s for s in servers if check_server_alive(*s)]


def transform_matrix_in_vector(matrix_1, matrix_2):
    matrix_parts = []
    for x in range(get_column_length(matrix_2)):
        for y in range(get_row_length(matrix_1)):
            m1 = get_row(matrix_1, x)
            m2 = get_column(matrix_2, y)
            matrix_parts.append([m1, m2, [x, y]])
    return matrix_parts


def split_vector(vector, serves):
    n = len(serves)
    size = len(vector) // n

    parts = []
    start = 0

    for i in range(n):
        parts.append(vector[start:] if i == n - 1 else vector[start : start + size])
        start += size

    return parts


def send_to_server(server_info, part):
    host, port = server_info
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port))

        send_packet(client, part)
        response = recv_packet(client)

        return response


def main(matrix_1, matrix_2):
    available_servers = get_available_servers(SERVERS)
    if not available_servers:
        print("Nenhum servidor disponível!")
        return

    print(f"Há {len(available_servers)} servidores disponíveis")

    rows = get_column_length(matrix_1)
    cols = get_row_length(matrix_2)
    matrix_result = [[0] * cols for _ in range(rows)]

    vector_matrix = transform_matrix_in_vector(matrix_1, matrix_2)
    parts = split_vector(vector_matrix, (available_servers))
    print(
        f"As matrizes foram particionadas em {len(parts)} e distribuidas em {[len(i) for i in parts]} sub-problemas"
    )

    with ThreadPoolExecutor(
        max_workers=min(len(available_servers), MAX_CPU_CORES)
    ) as executor:
        futures = []

        for idx, part in enumerate(parts):
            server = available_servers[idx]
            futures.append(executor.submit(send_to_server, server, part))

        for future in as_completed(futures):
            responses = future.result()
            for result, x, y in responses:
                matrix_result[x][y] = result
    print("matrix_result:", matrix_result)


if __name__ == "__main__":
    # for n in range(10,301,10): # Ns para Teste
    for n in [15]:
        initial_time = datetime.now()
        available_servers = len(get_available_servers(SERVERS))
        matrix_1 = get_matrix(n, n)
        matrix_2 = get_matrix(n, n)
        print("matrix_1:", matrix_1)
        print("matrix_2:" ,matrix_2)
        main(matrix_1, matrix_2)
        final_time = datetime.now()
        duration_time = final_time - initial_time

        info = {
            "initial_time": initial_time,
            "final_time": final_time,
            "duration_time": duration_time,
            "available_servers": available_servers,
        }
        save_json(info, f'results/{available_servers}_servers/matrix_{n}.json')
