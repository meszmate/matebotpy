from dataclasses import dataclass
from matebot.fortnite import CosmeticIcon, PrimarySecondaryColor
from typing import List, Dict

@dataclass
class Banner:
    name: str
    description: str
    shortDescription: str
    rarity: str
    tags: List[str]
    icon: CosmeticIcon

@dataclass
class BannerCategory:
    name: str
    sortPriority: int
    banners: Dict[str, Banner]

@dataclass
class Banners:
    colors: Dict[str, PrimarySecondaryColor]
    categories: List[BannerCategory]