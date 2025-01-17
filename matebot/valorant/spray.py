from dataclasses import dataclass
from typing import List

@dataclass
class SprayLevel:
    uuid: str
    level: int
    name: str

@dataclass
class Spray:
    uuid: str
    category: str
    theme: str
    name: str
    icon: str
    levels: List[SprayLevel]