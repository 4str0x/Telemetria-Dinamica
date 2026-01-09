import time
from core.state import state_data, lock
from config.settings import WATCHDOG_TIMEOUT, TELEMETRY_FIELDS
from infra.logger import logger

def watchdog():
    logger.info("[WATCHDOG] Iniciado")
    while True:
        time.sleep(0.1)
            
        with lock:
            if not state_data["connected"]:
                continue

            if time.time() - state_data["last_packet"] > WATCHDOG_TIMEOUT:
                logger.warning("[WATCHDOG] Perda de conexão detectada")
                state_data["connected"] = False
                for k in TELEMETRY_FIELDS:
                    state_data["telemetry"][k] = 0
                    
