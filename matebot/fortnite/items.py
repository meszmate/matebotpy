from dataclasses import dataclass
from typing import List, Optional

@dataclass
class JamTrack:
    title: str
    releaseYear: float
    duration: float
    album: str
    bpm: float
    scale: str
    artist: str
    midiDataURL: str
    albumArtURL: str
    templateId: str

@dataclass
class CosmeticIconLegoElement:
    wide: str
    small: str
    large: str

@dataclass
class CosmeticIconLego:
    first: CosmeticIconLegoElement
    second: CosmeticIconLegoElement

@dataclass
class CosmeticIcon:
    small: str
    large: str

@dataclass
class CosmeticVariantPart:
    name: str
    icon: str
    isDefault: bool
    tag: str

@dataclass
class CosmeticVariant:
    channel: str
    tag: str
    parts: List[CosmeticVariantPart]

@dataclass
class Cosmetic:
    name: str
    description: str
    shortDescription: str
    rarity: str
    variants: List[CosmeticVariant]
    tags: List[str]
    icon: CosmeticIcon

@dataclass
class Character:
    name: str
    description: str
    shortDescription: str
    gender: str
    rarity: str
    variants: List[CosmeticVariant]
    tags: List[str]
    icon: CosmeticIcon
    bean: Optional[CosmeticIcon]
    lego: Optional[CosmeticIconLego]

@dataclass
class Juno:
    id: str
    name: str
    rarity: str
    tags: List[str]
    icon: CosmeticIcon

@dataclass
class CarCosmetic:
    name: str
    description: str
    shortDescription: str
    variants: List[CosmeticVariant]
    tags: List[str]
    icon: CosmeticIcon

@dataclass
class CosmeticVariantToken:
    cosmetic: str
    channelTag: str
    nameTag: str
    name: str
    description: str
    shortDescription: str
    tags: List[str]
    icon: CosmeticIcon

@dataclass
class CosmeticVehicleVariantAdditional:
    channelTag: str
    variantTag: str

@dataclass
class CosmeticVehicleVariant:
    cosmetic: str
    channelTag: str
    nameTag: str
    name: str
    description: str
    shortDescription: str
    rarity: str
    additional: List[CosmeticVehicleVariantAdditional]

@dataclass
class Instrument:
    name: str
    description: str
    shortDescription: str
    rarity: str
    variants: List[CosmeticVariant]
    tags: List[str]
    icon: CosmeticIcon