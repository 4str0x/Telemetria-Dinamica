import threading
import time

from core import receiver
from core.watchdog import watchdog
from core.exporter import exporter
from infra.logger import logger
from infra.startup_config import show_startup_config

if __name__ == "__main__":
    show_startup_config()
    time.sleep(2)
    
    logger.info("SR2 CORE ONLINE[/] | aguardando UDP…")

    logger.info("📡 Iniciando receptor UDP")
    threading.Thread(target=receiver.udp_receiver, daemon=True).start()

    logger.info("🧠 Ativando watchdog de conexão")
    threading.Thread(target=watchdog, daemon=True).start()

    logger.info("📦 Iniciando pipeline de exportação")
    threading.Thread(target=exporter, daemon=True).start()
    
    while True:
        time.sleep(1)