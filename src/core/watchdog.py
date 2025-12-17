import time
from core.state import state, lock
from config.settings import WATCHDOG_TIMEOUT, TELEMETRY_FIELDS

def watchdog():
    while True:
        time.sleep(0.1)
            
        with lock:
            if not state["connected"]:
                continue

            if time.time() - state["last_packet"] > WATCHDOG_TIMEOUT:
                state["connected"] = False
                for k in TELEMETRY_FIELDS:
                    state["telemetry"][k] = 0
                    
