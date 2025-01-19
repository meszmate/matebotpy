import asyncio
import aiohttp
from typing import Callable, Optional, Any
import json
import time

class WebsocketClosed(Exception):
    def __init__(self, message="WebSocket is closed"):
        super().__init__(message)

class WebsocketClient:
    def __init__(self, uri: str, *, session: aiohttp.ClientSession):
        self._uri = uri
        self.onconnect: Optional[Callable[[str], None]] = None
        self.on_message: Optional[Callable[[str, Any], None]] = None
        self.timeout = 600
        self.id: str = ""
        self.websocket: Optional[aiohttp.ClientWebSocketResponse] = None
        self.heartbeat_interval: int = 20
        self.session = session

    async def _handle_messages(self, id: str, data: Any):
        if self.on_message:
            asyncio.create_task(self.on_message(id, data))

    async def _heartbeat(self):
        while True:
            await asyncio.sleep(self.heartbeat_interval)
            if self.websocket:
                await self.websocket.send_str(json.dumps({"type": "HEARTBEAT"}))

    async def connect(self):
        try:
            async with self.session.ws_connect(self._uri) as ws:
                self.websocket = ws
                if self.onconnect:
                    asyncio.create_task(self.onconnect(self.id))
                asyncio.create_task(self._heartbeat())
                async for msg in ws:
                    if msg.type == aiohttp.WSMsgType.TEXT:
                        await self._handle_messages(self.id, json.loads(msg.data))
                    elif msg.type == aiohttp.WSMsgType.CLOSED:
                        raise WebsocketClosed
                    elif msg.type == aiohttp.WSMsgType.ERROR:
                        raise Exception(f"WebSocket error: {msg.data}")
        except Exception as e:
            print(e)
            raise e
    async def close(self):
        await self.websocket.close()

    async def ping(self) -> float:
        if not self.websocket:
            raise Exception("WebSocket is not connected")
        start = time.monotonic()
        pong_waiter = await self.websocket.ping()
        await pong_waiter
        return time.monotonic() - start