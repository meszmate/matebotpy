from matebot.dashboard.types import Channel, Role, Guild as GuildData
from matebot.dashboard import Welcome, Defender, AutomationsData, WarnAutomation, Warn, Builtin, SlashCommands, LevelSettings, Giveaway, TempChannelSettings
from matebot import DashboardClient
from typing import List
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
        await self.parse(g)

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

    async def _handle_updates(self, id, g: GuildData):
        if id == self.id:
            await self.parse(g)
    
    def fetch_welcome(self) -> Welcome:
        return Welcome(**self._client._request("get", f"/dashboard/{self.id}/welcome"))

    def set_welcome(self, data: Welcome) -> None:
        self._client._request("post", f"/dashboard/{self.id}/welcome", data=data)
    
    def fetch_defender(self) -> Defender:
        return Defender(**self._client._request("get", f"/dashboard/{self.id}/defender"))
    
    def set_defender(self, data: Defender) -> None:
        self._client._request("post", f"/dashboard/{self.id}/defender", data=data)
    
    def fetch_automations(self) -> AutomationsData:
        return List[AutomationsData](**self._client._request("get", f"/dashboard/{self.id}/automations"))
    
    def set_automations(self, data: AutomationsData) -> None:
        self._client._request("post", f"/dashboard/{self.id}/automations", data=data)

    def fetch_warn_automations(self) -> List[WarnAutomation]:
        return [WarnAutomation(**item) for item in self._client._request("get", f"/dashboard/{self.id}/warns")]

    def set_warn_automations(self, automations: List[WarnAutomation]) -> None:
        self._client._request("post", f"/dashboard/{self.id}/warns", data=automations)
    
    def check_user_warnings(self, userid: str) -> List[Warn]:
        return [Warn(**item) for item in self._client._request("get", f"/dashboard/{self.id}/warns/{userid}")]
    
    def del_user_warn(self, userid: str, time: int) -> None:
        self._client._request("delete", f"/dashboard/{self.id}/warns/{userid}/{time}")
    
    def fetch_builtin(self) -> Builtin:
        return Builtin(**self._client._request("get", f"/dashboard/{self.id}/builtin"))

    def set_builtin(self, builtin: Builtin) -> None:
        self._client._request("post", f"/dashboard/{self.id}/builtin", data=builtin)
    
    def get_slashcommands(self) -> SlashCommands:
        return SlashCommands(**self._client._request("get", f"/dashboard/{self.id}/slash"))

    def set_slashcommands(self, commands: SlashCommands) -> None:
        self._client._request("post", f"/dashboard/{self.id}/slash", data=commands)

    def get_level_settings(self) -> LevelSettings:
        return LevelSettings(**self._client._request("get", f"/dashboard/{self.id}/levels"))
    
    def set_level_settings(self, settings: LevelSettings) -> None:
        self._client._request("post", f"/dashboard/{self.id}/levels", data=settings)
        
    def get_giveaways(self) -> List[Giveaway]:
        return [Giveaway(**gw) for gw in self._client._request("get", f"/dashboard/{self.id}/giveaways")]

    def set_giveaway(self, giveaway: Giveaway) -> None:
        self._client._request("post", f"/dashboard/{self.id}/giveaways", data=giveaway)
    
    def delete_giveaway(self, channelid: str, messageid: str) -> None:
        self._client._request("delete", f"/dashboard/{self.id}/giveaways?channelid={channelid}&messageid={messageid}")

    def get_tempchannels(self) -> TempChannelSettings:
        return TempChannelSettings(**self._client._request("get", f"/dashboard/{self.id}/tempchannels"))
    
    def set_tempchannels(self, channels: TempChannelSettings) -> None:
        self._client._request("post", f"/dashboard/{self.id}/tempchannels", data=channels)