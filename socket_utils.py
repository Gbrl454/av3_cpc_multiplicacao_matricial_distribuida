import socket
import pickle
import struct

def check_server_alive(host, port, timeout=1.0):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except:
        return False

def send_packet(conn, obj):
    data = pickle.dumps(obj)
    size = struct.pack("!I", len(data))  # 4 bytes big-endian
    conn.sendall(size)
    conn.sendall(data)

def recv_packet(conn):
    raw_header = conn.recv(4)
    if not raw_header:
        return None

    size = struct.unpack("!I", raw_header)[0]

    data = b""
    while len(data) < size:
        packet = conn.recv(4096)
        if not packet:
            break
        data += packet

    return pickle.loads(data)