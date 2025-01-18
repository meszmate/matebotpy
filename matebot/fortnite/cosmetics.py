from dataclasses import dataclass
from typing import Dict, List
from matebot.fortnite import Cosmetic, CarCosmetic, CosmeticVehicleVariant, Character, CosmeticVariantToken, Instrument, Juno

@dataclass
class Help:
    display: str
    help: str

@dataclass
class CosmeticsBattleRoyale:
    characters: Dict[str, Character]
    backpacks: Dict[str, Cosmetic]
    gliders: Dict[str, Cosmetic]
    petcarriers: Dict[str, Cosmetic]
    contrails: Dict[str, Cosmetic]
    pickaxes: Dict[str, Cosmetic]
    dances: Dict[str, Cosmetic]
    emojis: Dict[str, Cosmetic]
    toys: Dict[str, Cosmetic]
    sprays: Dict[str, Cosmetic]
    wraps: Dict[str, Cosmetic]
    loadingScreens: Dict[str, Cosmetic]
    musicPacks: Dict[str, Cosmetic]
    variants: Dict[str, CosmeticVariantToken]

@dataclass
class CosmeticsCars:
    bodies: Dict[str, CarCosmetic]
    wheels: Dict[str, CarCosmetic]
    boosters: Dict[str, CarCosmetic]
    driftTrails: Dict[str, CarCosmetic]
    skins: Dict[str, CarCosmetic]
    variants: Dict[str, CosmeticVehicleVariant]

@dataclass
class CosmeticsInstrument:
    aura: Dict[str, Instrument]
    bass: Dict[str, Instrument]
    drum: Dict[str, Instrument]
    guitar: Dict[str, Instrument]
    keytar: Dict[str, Instrument]
    mic: Dict[str, Instrument]
    variants: Dict[str, CosmeticVariantToken]

@dataclass
class CosmeticsLego:
    buildingSets: Dict[str, Juno]
    buildingProps: Dict[str, Juno]

@dataclass
class Cosmetics:
    sets: Dict[str, str]
    filters: Dict[str, List[str]]
    texts: Dict[str, Help]
    br: CosmeticsBattleRoyale
    cars: CosmeticsCars
    instruments: CosmeticsInstrument
    legos: CosmeticsLego