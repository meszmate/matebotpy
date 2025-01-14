from dataclasses import dataclass
from typing import List

@dataclass
class EmbedImage:
    type: int
    url: str
    upload: str

@dataclass
class EmbedAuthor:
    name: str
    url: str
    icon: EmbedImage

@dataclass
class EmbedFooter:
    text: str
    icon: EmbedImage

@dataclass
class EmbedField:
    name: str
    value: str
    inline: bool

@dataclass
class Embed:
    title: str
    description: str
    url: str
    color: str
    timestamp: bool
    footer: EmbedFooter
    author: EmbedAuthor
    image: EmbedImage
    thumbnail: EmbedImage
    fields: List[EmbedField]