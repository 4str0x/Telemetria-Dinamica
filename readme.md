
<h1 align="center">🚀 Dynamic Telemetry (Juno New Origin)</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Version-Alpha-green" alt="Version Badge" />
  <img src="https://wakatime.com/badge/user/8edf9756-b6e5-4a16-afcc-b737762a79ad/project/38867b66-57d9-4077-bdf0-969b5e37d355.svg" alt="WakaTime Badge" />
  <img src="https://img.shields.io/badge/Status-Developing-purple" alt="Status Badge" />
</p>

---

## Overview

A **real-time telemetry system** designed to continuously receive data via UDP, maintain a **centralized thread-safe state**, monitor connection integrity through a **watchdog**, and export **periodic JSON snapshots** for consumption by control panels or external systems.

The architecture is modular and robust, clearly separating the responsibilities of data reception, processing, monitoring, and export.

---

## Requirements

- **Python** 3.10 or higher
- Operating system with thread support (Linux, Windows, macOS)
- Juno New Origin (JNO) with the SR2LoggerPlus mod
- Vizzy from [this craft](https://google.com)

---

## Configuration

System settings are centralized in:

**`src/config/settings.py`**

You can adjust the following parameters:

| Parameter | Description |
|-----------|-------------|
| `UDP_HOST` | Listening IP address (default: `localhost`) |
| `UDP_PORT` | UDP Port (default: `5005`) |
| `WEBSOCKET_HOST` | WebSocket server host (default: `localhost`) |
| `WEBSOCKET_PORT` | WebSocket Port (default: `8765`) |
| `WATCHDOG_TIMEOUT` | Disconnection timeout in seconds |
| `EXPORT_INTERVAL` | Export interval in seconds |
| `TELEMETRY_FIELDS` | List of expected telemetry fields |

> ⚠️ **Recommendation**: Adjust the settings according to your infrastructure before starting the system.

---

## Initialization

### Basic Execution

```bash

$ pip install -r requirements.txt

$ python ./src/main.py
```

### What happens at startup

1. **Configuration Display** - Shows the current configuration table.
2. **WebSocket Server** - Starts the server on the configured port.
3. **UDP Receiver** - Begins listening for telemetry data.
4. **Connection Monitor** - Watchdog active to detect signal loss.
5. **Export Pipeline** - Periodic snapshots are exported.

---

## Architecture

### Execution Model

The system utilizes **multithreading**, where each component operates independently in its own thread:

```
┌─────────────────────────────────────────┐
│          Main Thread (main)             │
└──────────┬──────────────────────────────┘
           │
    ┌──────┼──────┬─────────────┬──────────┐
    │      │      │             │          │
    ▼      ▼      ▼             ▼          ▼
  [UDP]  [WS]  [WATCHDOG]  [EXPORTER]  [CORE]

```

| Component | Function |
| --- | --- |
| **UDP Receiver** | Receives real-time telemetry data |
| **WebSocket Server** | Broadcasts telemetry to connected clients |
| **Watchdog** | Monitors connection timeout and resets state |
| **Exporter** | Exports periodic JSON snapshots |
| **Central State** | Synchronizes data between threads using locks |

### Data Synchronization

Despite using multiple threads, access to the state is protected by `threading.Lock` to ensure **thread-safety**. This prevents race conditions and data corruption.

> 📌 **Technical Note**: Python executes threads on a single core (GIL). This model is ideal for I/O-intensive operations like networking and disk writing.

---

## Features

* ✅ **UDP Reception** - Receives telemetry data in real-time.
* ✅ **Centralized State** - Synchronized and thread-safe data with locks.
* ✅ **Disconnection Detection** - Watchdog monitors signal loss.
* ✅ **JSON Export** - Periodic snapshots for persistence.
* ✅ **WebSocket Server** - Real-time data broadcast to clients.
* ✅ **Structured Logs** - Tracking via the Rich library.
* ✅ **Modular Architecture** - Independent and reusable components.

---

## Snapshot Example

```json
{
  "timestamp": 1704720890.123,
  "connected": true,
  "telemetry": {
    "Velocity (m/s)": 123.4,
    "Altitude (m)": 4567.8,
    "Fuel (%)": 78.9
  }
}

```

---

## File Structure

```
src/
├── main.py                 # Entry point
├── config/
│   ├── settings.py         # Global settings
│   └── __pycache__/
├── core/
│   ├── receiver.py         # UDP Receiver
│   ├── watchdog.py         # Connection monitor
│   ├── exporter.py         # Snapshot exporter
│   ├── packet.py           # Packet parser
│   ├── state.py            # Centralized state
│   └── __pycache__/
└── infra/
    ├── logger.py           # Logging system
    ├── websocket_server.py # WebSocket server
    ├── startup_config.py   # Config display
    └── __pycache__/

```

---

## Development

To contribute to the project:

1. Clone the repository.
2. Create a branch for your feature (`git checkout -b feature/MyFeature`).
3. Commit your changes (`git commit -am 'Add MyFeature'`).
4. Push to the branch (`git push origin feature/MyFeature`).
5. Open a Pull Request.

---

**Developed with ❤️ for the community**