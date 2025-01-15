from matebot.dashboard.types import Channel, Role, Guild as GuildData
from matebot import DashboardClient
from typing import List, Optional
import asyncio

class Guild:
    def __init__(self, id: str, *, client: DashboardClient, fetch: bool=True, ws: bool = False):
        self.id: str = id
        self.owner: bool
        self.name: str
        self.membercount: int
        self.channels: List[Channel]
        self.categories: List[Channel]
        self.voices: List[Channel]
        self.roles: List[Role]
        self.premium: bool
        self._client: DashboardClient = client
        self._client.add_guild_update_handler(self.id, self._handle_updates)
        if fetch:
            asyncio.run(self.fetch())
            if ws:
                self._ws = asyncio.create_task(self.start_handle_updates())

    async def fetch(self) -> None:
        g = await self._client._fetch_guild(self.id)
        self.parse(g)

    async def start_handle_updates(self) -> None:
        asyncio.run(self._client.run_update_listener(self.id))
    
    async def stop_updates(self) -> None:
        self._ws.cancel()
        self._ws = None

    async def parse(self, g: GuildData) -> None:
        self.owner = g.owner
        self.name = g.name
        self.membercount = g.membercount
        self.categories = g.categories
        self.channels = g.channels
        self.voices = g.voices
        self.roles = g.roles
        self.premium = g.premium

    async def _handle_updates(self, _, g: GuildData):
        self.parse(g)