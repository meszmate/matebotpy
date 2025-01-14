import asyncio
import websockets
from typing import Callable, Dict, Optional, List
import time
import json

class WebsocketClient:
    def __init__(self, uri: str):
        self._uri = uri
        self.onconnect: Optional[Callable]
        self.on_message: Optional[Callable[[str, any], None]]
        self.timeout = 600
        self.id: str
        self.websocket = Optional[websockets.ClientProtocol]
        self.heartbeat_interval: int = 20
    
    async def _handle_messages(self, id, data: any):
        self.on_message(id, data)
    
    async def _heartbeat(self):
        while True:
            time.sleep(self.heartbeat_interval)
            self.websocket.send(json.dumps({"type": "HEARTBEAT"}))
    
    async def connect(self):
        self.websocket = await websockets.connect(self._uri)
        self.onconnect(self.id)
        asyncio.create_task(self._heartbeat())
        while True:
            msg = await self.websocket.recv()
            self._handle_messages(self.id, json.loads(msg))
    
    async def ping(self) -> int:
        start = time.monotonic()
        await self.websocket.ping()
        return time.monotonic()-start