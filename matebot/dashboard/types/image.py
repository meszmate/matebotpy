from dataclasses import dataclass
from typing import List

@dataclass
class ImageBackground:
    type: int
    color: str
    upload: str
    url: str
    opacity: str
    blur: str
    cover: bool
    width: str
    height: str

@dataclass
class ImageElement:
    type: int
    url: str
    upload: str
    positionx: str
    positiony: str
    alignx: float
    font: int
    fontsize: str
    fontweight: int
    content: str
    width: str
    height: str
    cover: bool
    radius: str
    opacity: float
    color: str
    blur: str
    progress: bool
    verticalprogress: bool

@dataclass
class Image:
    background: ImageBackground
    elements: List[ImageElement]