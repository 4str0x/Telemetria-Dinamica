import json
import time

from core.state import state_data
from infra.logger import logger
from infra.websocket_server import ws_server


def exporter():
    logger.info("[EXPORTER] Iniciado")

    while True:
        state = state_data

        if state:
            data = state.copy()
            
            with open("telemetry_state.json", "w") as f:
                json.dump(data, f, indent=2)

            try:
                ws_server.broadcast(data)
            except RuntimeError:
                pass

        time.sleep(1)
