import threading
import time

from core import receiver
from core.watchdog import watchdog
from core.exporter import exporter
from infra.logger import logger
from infra.startup_config import show_startup_config
from infra.websocket_server import start_ws_thread


if __name__ == "__main__":
    show_startup_config()
    time.sleep(2)

    logger.info("[WS] Iniciando servidor WebSocket")
    start_ws_thread()

    logger.info("[UDP] Iniciando receptor")
    threading.Thread(target=receiver.udp_receiver, daemon=True).start()

    logger.info("[WATCHDOG] Ativando monitor de conexão")
    threading.Thread(target=watchdog, daemon=True).start()

    logger.info("[EXPORTER] Iniciando pipeline de exportação")
    threading.Thread(target=exporter, daemon=True).start()

    logger.info("[CORE] Sistema online | CTRL+C para encerrar")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logger.info("[CORE] Sistema encerrado")
