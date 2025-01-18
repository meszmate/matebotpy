import aiohttp
from matebot.dashboard import Stats, User, GuildResponse, Guild
from matebot.dashboard.types import Guild as GuildData
from matebot.websocket import WebsocketClient, WebsocketClosed
from typing import Optional, List, Callable, Dict, Any
import asyncio
import websockets
from dataclasses import asdict

class DashboardClient:
    def __init__(self, token: str, *, base_url: Optional[str] = None, log: bool = True):
        self._token = token
        self._ws_guild_update_listeners = List[Callable[[str, GuildData], None]] = []
        self._ws_guild_update_connect = List[Callable[[str], None]] = []
        self._ws_guild_update_disconnect = List[Callable[[str], None]] = []
        self._ws_guild_event_listeners = List[Callable[[str, Dict[str, str]], None]] = []
        self._ws_guild_event_connect = List[Callable[[str], None]] = []
        self._ws_guild_event_disconnect = List[Callable[[str], None]] = []
        self.heartbeat_interval: int = 20
        self._log: bool = log
        self._websocket_update_connections: Dict[str, WebsocketClient] = {}
        self._websocket_event_connections: Dict[str, WebsocketClient] = {}
        self.max_retries: int = 10
        self.retry_delay: int = 180
        self.session = aiohttp.ClientSession("https://api.matebot.xyz/dc" if not base_url else base_url)

    def _get_headers(self):
        return {
            "Authorization": self._token
        }
    
    async def _request(self, method: str, url: str, *, auth: Optional[bool]=True, data: Optional[Any]) -> Any:
        async with self.session.request(method,url,headers=self._get_headers() if auth else None, json=asdict(data) if data else None) as response:
            if response.status == 200:
                return await response.json()
            else:
                raise Exception(f"Request failed: {response.status} - {await response.text()}")

    def add_guild_update_handler(self, listener: Callable[[str, GuildData], None]) -> None:
        self._ws_guild_update_listeners.append(listener)

    def add_guild_update_handler_connect(self, listener: Callable[[str], None]) -> None:
        self._ws_guild_update_connect.append(listener)

    def add_guild_update_handler_disconnect(self, listener: Callable[[str], None]) -> None:
        self._ws_guild_update_connect.append(listener)

    def add_guild_event_handler(self, listener: Callable[[str, Dict[str, str]], None]) -> None:
        self._ws_guild_event_listeners.append(listener)
        
    def add_guild_event_handler_connect(self, listener: Callable[[str], None]) -> None:
        self._ws_guild_event_connect.append(listener)

    def add_guild_event_handler_disconnect(self, listener: Callable[[str], None]) -> None:
        self._ws_guild_event_connect.append(listener)
    
    async def _on_update_message(self, id: str, data: Any):
        for i in self._ws_guild_update_listeners:
            asyncio.create_task(i(id, GuildData(**data)))

    async def _on_update_connect(self, id: str):
        for i in self._ws_guild_update_connect:
            asyncio.create_task(i(id))

    async def _on_update_disconnect(self, id: str):
        for i in self._ws_guild_update_disconnect:
            asyncio.create_task(i(id))

    async def run_update_listener(self, guildid):
        retries = 0
        while True:
            try:
                ws = WebsocketClient(self.session._base_url.replace("https", "wss")+"/dashboard/"+guildid+"/ws?auth="+self._token)
                self._websocket_update_connections[guildid] = ws
                ws.on_message = self._on_update_message
                ws.onconnect = self._on_update_connect
                try:
                    await ws.connect()
                except WebsocketClosed:
                    retries = 0
                    del self._websocket_update_connections[guildid]
                    asyncio.create_task(self._on_update_disconnect(guildid))
                    raise WebsocketClosed
                except Exception as e:
                    del self._websocket_update_connections[guildid]
                    raise e
            except Exception as e:
                if retries >= self.max_retries:
                    raise Exception("All connection attempts failed. Stopping retries.")
                retries+=1
                if self._log:
                    print(f"Connection failed. Retrying in {self.retry_delay} seconds... ({retries}/{self.max_retries})\nError: {e}")

    async def _on_events_message(self, id: str, data: any):
        for i in self._ws_guild_event_listeners:
            asyncio.create_task(i(id, dict(**data)))

    async def _on_events_connect(self, id: str):
        for i in self._ws_guild_event_connect:
            asyncio.create_task(i(id))

    async def _on_events_disconnect(self, id: str):
        for i in self._ws_guild_event_disconnect:
            asyncio.create_task(i(id))

    async def run_event_listener(self, guildid):
        retries = 0
        while True:
            try:
                ws = WebsocketClient(self.base_url.replace("https", "wss")+"/dashboard/"+guildid+"/events")
                self._websocket_update_connections[guildid] = ws
                ws.on_message = self._on_events_message
                ws.onconnect = self._on_events_connect
                try:
                    await ws.connect()
                except websockets.ConnectionClosed:
                    retries = 0
                    del self._websocket_update_connections[guildid]
                    asyncio.create_task(self._on_events_disconnect(guildid))
                    raise websockets.ConnectionClosed
                except Exception as e:
                    del self._websocket_update_connections[guildid]
                    raise e
            except Exception as e:
                if retries >= self.max_retries:
                    raise Exception("All connection attempts failed. Stopping retries.")
                retries+=1
                if self._log:
                    print(f"Connection failed. Retrying in {self.retry_delay} seconds... ({retries}/{self.max_retries})\nError: {e}")
    
    async def update_ping(self, guildid: str) -> int:
        ws = self._websocket_update_connections[guildid]
        return await ws.ping()

    async def events_ping(self, guildid: str) -> int:
        ws = self._websocket_update_connections[guildid]
        return await ws.ping()
    
    async def fetch_stats(self) -> Stats:
        return Stats(**await self._request("get", "/stats", auth=False))
    
    async def fetch_me(self) -> User:
        return User(**await self._request("get", "/users/me"))
    
    async def reset(self) -> None:
        await self._request("post", "/users/me/refresh")
    
    async def fetch_me(self) -> User:
        return User(**await self._request("get", "/users/me"))
    
    async def fetch_guilds(self) -> GuildResponse:
        return GuildResponse(**await self._request("get", "/guilds"))
    
    def guild(self, id, *, fetch: bool = True, ws: bool = False) -> Guild:
        return Guild(id, client=self, fetch=fetch, ws=ws)
    
    async def _fetch_guild(self, id: str) -> GuildData:
        return GuildData(**await self._request("get", f"/dashboard/{id}"))