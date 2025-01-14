from dataclasses import dataclass
from typing import List
from matebot.dashboard.types import Embed, ActionRow, Image

@dataclass
class WelcomeMessage:
    message: bool
    channelid: str
    content: str
    embeds: List[Embed]
    actionrows: List[ActionRow]
    image: bool
    imagedata: Image

@dataclass
class GoodbyeMessage:
    message: bool
    channelid: str
    content: str
    embeds: List[Embed]
    actionrows: List[ActionRow]
    image: bool
    imagedata: Image

@dataclass
class WelcomePrivateMessage:
    message: bool
    content: str
    embeds: List[Embed]
    actionrows: List[ActionRow]
    image: bool
    imagedata: Image

@dataclass
class Welcome:
    welcome: WelcomeMessage
    goodbye: GoodbyeMessage
    private: WelcomePrivateMessage