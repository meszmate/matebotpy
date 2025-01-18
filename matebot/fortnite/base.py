from dataclasses import dataclass
from typing import List, Optional, Any, Dict, Union
from matebot.fortnite.items import Character, Cosmetic, CarCosmetic, Instrument, CosmeticVariantToken, CosmeticVehicleVariant, Juno

@dataclass
class PrimarySecondaryColor:
    primary: str
    secondary: str

@dataclass
class WebsocketEventData:
    languages: List[str]

@dataclass
class WebsocketEvent:
    type: str
    data: WebsocketEventData
    timestamp: int

@dataclass
class StatsTrack:
    gameId: str
    trackguid: str
    accountId: str
    rankingType: str
    lastUpdated: str
    currentDivision: float
    highestDivision: float
    promotionProgress: float
    currentPlayerRanking: Optional[float]

@dataclass
class Stats:
    accountId: str
    stats: Dict[str, Any]
    ranks: List[StatsTrack]

Definition = Union[Character, Cosmetic, CarCosmetic, Instrument, CosmeticVariantToken, CosmeticVehicleVariant, Juno]