import socket
import time
from core.packet import Packet
from core.state import state, lock
from config.settings import *

def udp_receiver():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_HOST, UDP_PORT))

    while True:
        data, _ = sock.recvfrom(BUFFER_SIZE)
        
        if len(data) < 5:
            continue
        
        try:
            p = Packet(data)
            msg_type = p.read("B")
            if msg_type != 2:
                continue

            msg_len = p.read("I")
            message = p.get(msg_len).decode("utf-8", errors="replace")
            values = message.split("ç")

        except Exception:
            continue

        with lock:
            for i, key in enumerate(TELEMETRY_FIELDS):
                if i < len(values):
                    state["telemetry"][key] = values[i]

            state["connected"] = True
            state["last_packet"] = time.time()
