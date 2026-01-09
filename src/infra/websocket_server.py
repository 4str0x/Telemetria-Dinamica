# src/infra/websocket_server.py

import asyncio
import json
import threading
from typing import Set, Any

import websockets

from infra.logger import logger
from config.settings import WEBSOCKET_HOST, WEBSOCKET_PORT


class WebSocketServer:
    def __init__(
        self,
        host: str = WEBSOCKET_HOST,
        port: int = WEBSOCKET_PORT
    ) -> None:
        self.host = host
        self.port = port
        self.clients: Set[Any] = set()
        self.loop: asyncio.AbstractEventLoop | None = None

    async def handler(self, websocket: Any) -> None:
        self.clients.add(websocket)
        logger.info(f"[WS] Cliente conectado de {websocket.remote_address}")
        try:
            async for _ in websocket:
                pass
        finally:
            self.clients.discard(websocket)
            logger.info(f"[WS] Cliente {websocket.remote_address} desconectado")

    async def _broadcast(self, data: dict[str, Any]) -> None:
        if not self.clients:
            return

        payload = json.dumps(data)
        dead: Set[Any] = set()

        for ws in self.clients:
            try:
                await ws.send(payload)
            except Exception:
                dead.add(ws)

        self.clients -= dead

    def broadcast(self, data: dict[str, Any]) -> None:
        if self.loop and self.loop.is_running():
            asyncio.run_coroutine_threadsafe(
                self._broadcast(data),
                self.loop
            )

    async def _start_server(self) -> None:
        async with websockets.serve(
            self.handler,
            self.host,
            self.port
        ):
            logger.info(f"[WS] Servidor iniciado em ws://{self.host}:{self.port}")
            await asyncio.Future()

    def start(self) -> None:
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)

        try:
            self.loop.run_until_complete(self._start_server())
        except KeyboardInterrupt:
            logger.info("[WS] Servidor parado pelo usuário")
        finally:
            self.loop.close()


ws_server = WebSocketServer()


def start_ws_thread() -> None:
    threading.Thread(
        target=ws_server.start,
        daemon=True
    ).start()
