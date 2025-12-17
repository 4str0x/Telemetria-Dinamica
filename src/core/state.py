import threading
from typing import Any
from config.settings import TELEMETRY_FIELDS

state: dict[str,Any] = {
    "connected": False,
    "last_packet": 0.0,
    "telemetry": {k: 0 for k in TELEMETRY_FIELDS}
}

lock = threading.Lock()