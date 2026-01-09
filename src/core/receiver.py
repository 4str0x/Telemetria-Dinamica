import socket
import time
from core.packet import Packet
from core.state import state_data, lock
from config.settings import *
from infra.logger import logger

def udp_receiver():
    logger.info("[UDP] Iniciado")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_HOST, UDP_PORT))
    logger.info(f"[UDP] Escutando em {UDP_HOST}:{UDP_PORT}")

    while True:
        data, addr = sock.recvfrom(BUFFER_SIZE)
        
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

        except Exception as e:
            logger.debug(f"[UDP] Erro ao processar pacote: {e}")
            continue

        with lock:
            for i, key in enumerate(TELEMETRY_FIELDS):
                if i < len(values):
                    state_data["telemetry"][key] = values[i]

            state_data["connected"] = True
            state_data["last_packet"] = time.time()
