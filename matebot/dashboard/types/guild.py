from dataclasses import dataclass
from typing import List

@dataclass
class Channel:
    id: str
    position: int
    parentid: str
    name: str

@dataclass
class Role:
    id: str
    position: int
    color: str
    name: str

@dataclass
class Guild:
    owner: bool
    name: str
    membercount: int
    channels: List[Channel]
    categories: List[Channel]
    voices: List[Channel]
    roles: List[Role]
    premium: bool