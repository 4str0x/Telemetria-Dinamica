UDP_HOST = "127.0.0.1"
UDP_PORT = 2345
BUFFER_SIZE = 2048

WATCHDOG_TIMEOUT = 2.0
EXPORT_INTERVAL = 1.0
EXPORT_FILE = "telemetry_state.json"

WEBSOCKET_HOST = "localhost"
WEBSOCKET_PORT = 8765

TELEMETRY_FIELDS = [
    "time (s)",
    "Velocity (m/s)",
    "Altitude (m)",
    "Apoastro (km)",
    "Periastro (km)",
    "time-apostaro (s)",
    "Fuel (%)",
    "Mass (kg)",
    "Roll (°)",
]