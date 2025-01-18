from dataclasses import dataclass
from typing import List, Dict, Optional
from matebot.fortnite import CosmeticIcon

@dataclass
class QuestsBundleItem:
    id: str
    name: str
    description: str
    shortDescription: str
    completion: str
    rewards: List[str]
    sortPriority: int
    rarity: str
    category: str
    tags: List[str]
    count: int

@dataclass
class QuestsBundle:
    id: str
    name: str
    description: str
    shortDescription: str
    goal: str
    tags: List[str]
    icon: CosmeticIcon
    items: List[QuestsBundleItem]

@dataclass
class QuestsReward:
    reward: str
    quantity: int
    visible: bool

@dataclass
class QuestsDef:
    name: str
    description: str
    shortDescription: str
    searchTags: str
    tags: List[str]
    icon: CosmeticIcon

@dataclass
class Quests:
    athenaSeasonalXP: Optional[QuestsDef]
    athenaLevelUp: Optional[QuestsDef]
    rewards: Dict[str, QuestsReward]
    folders: Dict[str, List[QuestsBundle]]