from dataclasses import dataclass
from typing import Optional, List
from matebot.valorant.base import XYValue

@dataclass
class CharacterRole:
    uuid: str
    name: str
    description: str
    icon: str

@dataclass
class CharacterPortraitRenderTransformation:
    translation: XYValue
    scale: XYValue

@dataclass
class CharacterAbility:
    id: str
    name: str
    description: str
    icon: str

@dataclass
class Character:
    uuid: str
    id: str
    developerName: str
    shippingName: str
    name: str
    description: str
    icon: str
    portrait: str
    background: str
    killFeedIcon: str
    isPlayableCharacter: str
    role: Optional[CharacterRole]
    portraitRenderTransform: CharacterPortraitRenderTransformation
    abilities: List[CharacterAbility]