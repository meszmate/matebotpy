from dataclasses import dataclass
from typing import Dict, List

@dataclass
class MaterialParameter:
    name: str
    index: int
    value: float

@dataclass
class Material: 
    colors: Dict[str, str]
    parameters: List[MaterialParameter]
    image: str

@dataclass
class NewDisplayAsset:
    tag: str
    material: Material
    render: str
