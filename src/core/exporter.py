import time
import json
from typing import Any

from core.state import state, lock
from config.settings import EXPORT_INTERVAL, EXPORT_FILE

def exporter():
    while True:
        time.sleep(EXPORT_INTERVAL)

        with lock:
            snapshot: dict[str, Any] = {
                "timestamp": time.time(),
                "connected": state["connected"],
                "telemetry": state["telemetry"]
            }

        with open(EXPORT_FILE, "w") as f:
            json.dump(snapshot, f, indent=2)