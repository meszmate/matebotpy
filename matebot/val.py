import aiohttp
from matebot.valorant import WebsocketEvent, Weapon, Buddy, Character, LevelBorder, PlayerCard, Spray, Theme, ContentTier, Bundle, Map
from matebot.websocket import WebsocketClient
from typing import Optional, List, Callable, Dict
import asyncio
import websockets
from dataclasses import asdict

class ValorantClient:
    def __init__(self, api_key: str, *, base_url: Optional[str] = None, log: bool = True):
        self._api_key = api_key
        self._ws_listeners = List[Callable[[WebsocketEvent], None]] = []
        self._ws_connect = List[Callable[[], None]] = []
        self._ws_disconnect = List[Callable[[], None]] = []
        self._websocket_connection: WebsocketClient
        self.heartbeat_interval: int = 20
        self._log: bool = log
        self.max_retries: int = 10
        self.retry_delay: int = 180
        self.session = aiohttp.ClientSession("https://api.matebot.xyz/val" if not base_url else base_url)

    def _get_headers(self):
        return {
            "X-API-KEY": self._api_key
        }
    
    async def _request(self, method: str, url: str, *, auth: Optional[bool]=True, data: Optional[any]) -> any:
        async with self.session.request(method,url,headers=self._get_headers() if auth else None, json=asdict(data) if data else None) as response:
            if response.status == 200:
                return await response.json()
            else:
                raise Exception(f"Request failed: {response.status} - {await response.text()}")

    def add_guild_update_handler(self, listener: Callable[[WebsocketEvent], None]) -> None:
        self._ws_listeners.append(listener)

    def add_guild_update_handler_connect(self, listener: Callable[[], None]) -> None:
        self._ws_connect.append(listener)

    def add_guild_update_handler_disconnect(self, listener: Callable[[], None]) -> None:
        self._ws_listeners.append(listener)
    
    async def _on_message(self, _, data: any):
        for i in self._ws_listeners:
            asyncio.create_task(i(WebsocketEvent(**data)))

    async def _on_connect(self, _):
        for i in self._ws_connect:
            asyncio.create_task(i(id))

    async def _on_disconnect(self, _):
        for i in self._ws_disconnect:
            asyncio.create_task(i())

    async def run(self):
        retries = 0
        while True:
            try:
                ws = WebsocketClient(self.base_url.replace("https", "wss")+"/ws")
                self._websocket_connection = ws
                ws.on_message = self._on_message
                ws.onconnect = self._on_connect
                try:
                    await ws.connect()
                except websockets.ConnectionClosed:
                    retries = 0
                    self._websocket_connection = None
                    asyncio.create_task(self._on_disconnect())
                    raise websockets.ConnectionClosed
                except Exception as e:
                    self._websocket_connection = None
                    raise e
            except Exception as e:
                if retries >= self.max_retries:
                    raise Exception("All connection attempts failed. Stopping retries.")
                retries+=1
                if self._log:
                    print(f"Connection failed. Retrying in {self.retry_delay} seconds... ({retries}/{self.max_retries})\nError: {e}")

    async def ping(self) -> int:
        ws = self._websocket_connection
        return await ws.ping()
    
    async def fetch_weapons(self) -> List[Weapon]:
        return [Weapon(**weapon) for weapon in await self._request("get", "/weapons")]
    
    async def fetch_meele(self) -> Weapon:
        return Weapon(**await self._request("get", "/meele"))
    
    async def fetch_buddies(self) -> List[Buddy]:
        return [Buddy(**buddy) for buddy in await self._request("get", "/buddies")]
    
    async def fetch_characters(self) -> List[Character]:
        return [Character(**character) for character in await self._request("get", "/characters")]
    
    async def fetch_levelborders(self) -> List[LevelBorder]:
        return [LevelBorder(**levelborder) for levelborder in await self._request("get", "/levelborders")]
    
    async def fetch_playercards(self) -> List[PlayerCard]:
        return [PlayerCard(**playercard) for playercard in await self._request("get", "/playercards")]
    
    async def fetch_sprays(self) -> List[Spray]:
        return [Spray(**spray) for spray in await self._request("get", "/sprays")]
    
    async def fetch_themes(self) -> Dict[str, Theme]:
        return {
            key: Theme(**data)
            for key, data in await self._request("get", "/themes").items()
        }

    async def fetch_contenttiers(self) -> Dict[str, ContentTier]:
        return {
            key: ContentTier(**data)
            for key, data in await self._request("get", "/contenttiers").items()
        }
    
    async def fetch_bundles(self) -> List[Bundle]:
        return [Bundle(**bundle) for bundle in await self._request("get", "/bundles")]
    
    async def fetch_maps(self) -> List[Map]:
        return [Map(**mapdata) for mapdata in await self._request("get", "/maps")]