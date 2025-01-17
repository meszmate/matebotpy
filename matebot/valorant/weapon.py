from dataclasses import dataclass
from typing import Optional, List, Dict
from matebot.valorant import XYValue, Position

@dataclass
class DamageRange:
    rangeStartMeters: float
    rangeEndMeters: float
    head: float
    body: float
    leg: float

@dataclass
class WeaponsStatsAltShotgunStats:
    shotgunPelletCount: int
    burstRate: float

@dataclass
class WeaponStatsAirBurst:
    burstDistance: float
    shotgunPelletCount: int

@dataclass
class WeaponStatsADSStats:
    zoomMultiplier: float
    fireRate: float
    runSpeedMultiplier: float
    burstCount: int
    firstBulletAccuracy: float

@dataclass
class WeaponStats:
    fireMode: str
    fireRate: float
    magazineSize: int
    runSpeedMultiplier: float
    equipTimeSeconds: float
    reloadTimeSeconds: float
    firstBulletAccuracy: float
    shotgunPelletCount: int
    wallPenetration: str
    damageRanges: List[DamageRange]
    altFireType: str
    ads: Optional[WeaponStatsADSStats]
    airBurst: Optional[WeaponStatsAirBurst]
    altShotgunStats: Optional[WeaponsStatsAltShotgunStats]
    feature: str

@dataclass
class WeaponLevel:
    uuid: str
    name: str
    icon: str

@dataclass
class WeaponChroma:
    uuid: str
    name: str
    render: str
    swatch: str
    icon: str

@dataclass
class WeaponSkin:
    name: str
    icon: str
    wallpaper: str
    defaultChroma: str
    theme: str
    contentTier: str
    levels: List[WeaponLevel]
    chromas: List[WeaponChroma]

@dataclass
class WeaponShopDataGrid:
    column: int
    row: int

@dataclass
class WeaponShopData:
    price: int
    category: str
    categoryText: str
    image: str
    grid: WeaponShopDataGrid

@dataclass
class Weapon:
    uuid: str
    defaultSkin: str
    name: str
    category: str
    icon: str
    killIcon: str
    cameraPosition: Optional[Position]
    pivotPoint: Optional[Position]
    minFov: float
    maxFov: float
    defaultFov: float
    buddyCameraPosition: Optional[Position]
    buddyDefaultFov: float
    buddyMaxFov: float
    buddyMinFov: float
    stats: Optional[WeaponStats]
    shopData: Optional[WeaponShopData]
    skins: Dict[str, WeaponSkin]