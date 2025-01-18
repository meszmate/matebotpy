import aiohttp
from matebot.fortnite import WebsocketEvent, Cosmetics, NewDisplayAsset, Quests, Banners, SparkTrack, Banner, ItemShop
from matebot.websocket import WebsocketClient
from matebot import WebsocketClosed
from typing import Optional, List, Callable, Dict, Any
import asyncio

FortniteLanguages = [
    "en",
    "ar",
    "de",
    "es",
    "es-419",
    "fr",
    "it",
    "ja",
    "ko",
    "pl",
    "pt-BR",
    "ru",
    "tr",
    "zh-CN"
]

class FortniteCache:
    def __init__(self):
        self.cosmetics: Cosmetics
        self.newdisplayassets: Dict[str, List[NewDisplayAsset]]
        self.displayassets: Dict[str, str]
        self.quests: Quests
        self.banners: Banners
        self.sparktracks: Dict[str, SparkTrack]
        self.news: Any
        self.itemshop: ItemShop

class ValorantClient:
    def __init__(self, api_key: str, *, base_url: Optional[str], log: bool = True):
        self._api_key = api_key
        self._ws_listeners = List[Callable[[WebsocketEvent], None]] = []
        self._ws_connect = List[Callable[[], None]] = []
        self._ws_disconnect = List[Callable[[], None]] = []
        self._websocket_connection: WebsocketClient
        self.heartbeat_interval: int = 20
        self._log: bool = log
        self.max_retries: int = 10
        self.retry_delay: int = 180
        self.session = aiohttp.ClientSession("https://api.matebot.xyz/fn" if not base_url else base_url)
        self._cache: Dict[str, FortniteCache] = {}

    def data(self, lang: str) -> FortniteCache:
        return self._cache[lang]
    
    def remove_data(self, lang: str) -> None:
        del self._cache[lang]
    
    async def setup(self, lang: str) -> None:
        if not any(l.lower() == lang.lower() for l in FortniteLanguages):
            raise Exception("Language not found.")
        newCache = FortniteCache()
        (
            newCache.cosmetics,
            newCache.newdisplayassets,
            newCache.displayassets,
            newCache.quests,
            newCache.banners,
            newCache.sparktracks,
            newCache.news,
            newCache.itemshop
        ) = await asyncio.gather(
            self.fetch_cosmetics(lang=lang),
            self.fetch_newdisplayassets(lang=lang),
            self.fetch_displayassets(lang=lang),
            self.fetch_quests(lang=lang),
            self.fetch_banners(lang=lang),
            self.fetch_sparktracks(lang=lang),
            self.fetch_news(lang=lang),
            self.fetch_shop_br(lang=lang)
        )
        self._cache[lang] = newCache
        if self._on_change not in self._ws_listeners:
            self._ws_listeners.append(self._on_change)
        
    async def _on_change(self, event: WebsocketEvent) -> None:
        tasks = []
        task_info = []

        if event.type == "COSMETICS":
            func = self.fetch_cosmetics
        elif event.type == "SPARKTRACKS":
            func = self.fetch_sparktracks
        elif event.type == "BANNERS":
            func = self.fetch_banners
        elif event.type == "ITEMSHOP":
            func = self.fetch_shop_br
        elif event.type == "NEWS":
            func = self.fetch_news
        elif event.type == "DISPLAYASSETS":
            func = self.fetch_displayassets
        elif event.type == "NEWDISPLAYASSETS":
            func = self.fetch_newdisplayassets
        elif event.type == "QUESTS":
            func = self.fetch_quests
        else:
            return

        for lang in event.data.languages:
            if not self._cache[lang]:
                continue

            tasks.append(func(lang=lang))
            task_info.append(lang)
        
        results = await asyncio.gather(*tasks)

        for lang, result in zip(task_info, results):
            if event.type == "COSMETICS":
                self._cache[lang].cosmetics = result
            elif event.type == "SPARKTRACKS":
                self._cache[lang].sparktracks = result
            elif event.type == "BANNERS":
                self._cache[lang].banners = result
            elif event.type == "ITEMSHOP":
                self._cache[lang].itemshop = result
            elif event.type == "NEWS":
                self._cache[lang].news = result
            elif event.type == "DISPLAYASSETS":
                self._cache[lang].displayassets = result
            elif event.type == "NEWDISPLAYASSETS":
                self._cache[lang].newdisplayassets = result
            elif event.type == "QUESTS":
                self._cache[lang].quests = result

    def _get_headers(self):
        return {
            "X-API-KEY": self._api_key
        }
    
    async def _request(self, method: str, url: str, *, auth: Optional[bool]=True, lang:Optional[str]) -> Any:
        if lang:
            url+="?lang="+lang
        async with self.session.request(method,url,headers=self._get_headers() if auth else None) as response:
            if response.status == 200:
                try:
                    return await response.json()
                except:
                    return await response.text()
            else:
                raise Exception(f"Request failed: {response.status} - {await response.text()}")

    def add_guild_update_handler(self, listener: Callable[[WebsocketEvent], None]) -> None:
        self._ws_listeners.append(listener)

    def add_guild_update_handler_connect(self, listener: Callable[[], None]) -> None:
        self._ws_connect.append(listener)

    def add_guild_update_handler_disconnect(self, listener: Callable[[], None]) -> None:
        self._ws_listeners.append(listener)
    
    async def _on_message(self, _, data: Any):
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
                ws = WebsocketClient(self.session._base_url.replace("https", "wss")+"/ws")
                self._websocket_connection = ws
                ws.on_message = self._on_message
                ws.onconnect = self._on_connect
                try:
                    await ws.connect()
                except WebsocketClosed:
                    retries = 0
                    self._websocket_connection = None
                    asyncio.create_task(self._on_disconnect())
                    raise WebsocketClosed
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
    
    async def fetch_cosmetics(self, lang: Optional[str]) -> Cosmetics:
        return Cosmetics(**await self._request("get", "/cosmetics", lang=lang))
    
    async def fetch_cosmetics_item(self, templateid: str, lang: Optional[str]) -> Any:
        return await self._request("get", "/cosmetics/"+templateid, lang=lang)
    
    async def fetch_banners(self, lang: Optional[str]) -> Banners:
        return Banners(**await self._request("get", "/banners", lang=lang))

    async def fetch_banners_item(self, id: str, lang: Optional[str]) -> Banner:
        return Banners(**await self._request("get", "/banners/"+id, lang=lang))
    
    async def fetch_newdisplayassets(self, lang: Optional[str]) -> Dict[str, List[NewDisplayAsset]]:
        return {
            key: NewDisplayAsset(**data)
            for key, data in await self._request("get", "/newdisplayassets", lang=lang).items()
        }
    
    async def fetch_newdisplayassets_item(self, lang: Optional[str]) -> NewDisplayAsset:
        return NewDisplayAsset(**await self._request("get", "/newdisplayassets", lang=lang))

    async def fetch_displayassets(self, lang: Optional[str]) -> Dict[str, str]:
        return {
            key: str(data)
            for key, data in await self._request("get", "/displayassets", lang=lang).items()
        }
    
    async def fetch_displayassets_item(self, id: str, lang: Optional[str]) -> str:
        return str(await self._request("get", "/displayassets/"+id, lang=lang))

    async def fetch_quests(self, lang: Optional[str]) -> Quests:
        return Quests(**await self._request("get", "/quests", lang=lang))

    async def fetch_sparktracks(self, lang: Optional[str]) -> List[SparkTrack]:
        return [SparkTrack(**item) for item in await self._request("get", "/sparktracks", lang=lang)]
    
    async def fetch_news(self, lang: Optional[str]) -> Any:
        return await self._request("get", "/news", lang=lang)
    
    async def fetch_shop_br(self, lang: Optional[str]) -> Any:
        return ItemShop(**await self._request("get", "/shop/br", lang=lang))