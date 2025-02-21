from dataclasses import dataclass
from typing import Any, List, Optional
from matebot.fortnite.base import Definition, DefinitionTypes
from matebot.fortnite.newdisplayassets import NewDisplayAsset
from matebot.fortnite.tracks import SparkTrack
from matebot.fortnite.items import Cosmetic, Juno, CarCosmetic, Instrument, Character, CosmeticVehicleVariant, CosmeticVariantToken
import inspect

@dataclass
class ItemShopEntryBundleItemInfo:
    templateId: str
    quantity: float

@dataclass
class ItemShopEntryBundleItem:
    bCanOwnMultiple: bool
    regularPrice: float
    discountedPrice: float
    alreadyOwnedPriceReduction: float
    item: Optional[ItemShopEntryBundleItemInfo]

    def __post_init__(self):
        if self.item:
            self.item = ItemShopEntryBundleItemInfo(**self.item)

@dataclass
class ItemShopEntryBundle:
    name: str
    discountedBasePrice: float
    regularBasePrice: float
    floorPrice: float
    currencyType: str
    currencySubType: str
    displayType: str
    bundleItems: List[ItemShopEntryBundleItem]

    def __post_init__(self):
        self.bundleItems = [ItemShopEntryBundleItem(**item) for item in self.bundleItems]

@dataclass
class ItemShopEntryColors:
    color1: str
    color2: str
    color3: str
    textBackground: str

@dataclass
class ItemShopEntryItem:
    templateId: str
    quantity: str
    definition: Optional[Definition]

    def __post_init__(self):
        if self.definition and isinstance(self.definition, dict):
            x = self.templateId.lower().split(":")
            if len(x) > 0:
                x = x[0]
                if x == "sparkssong":
                    self.definition = SparkTrack(**self.definition)
                elif x == "athenacharacter":
                    self.definition = Character(**self.definition)
                elif x.startswith("vehiclecosmetics"):
                    self.definition = CarCosmetic(**self.definition)
                elif x.startswith("sparks"):
                    self.definition = Instrument(**self.definition)
                elif x.startswith("juno"):
                    self.definition = Juno(**self.definition)
                elif x == "cosmeticvarianttoken":
                    if not self.definition.get("rarity"):
                        self.definition = CosmeticVehicleVariant(**self.definition)
                    else:
                        self.definition = CosmeticVariantToken(**self.definition)
                else:
                    self.definition = Cosmetic(**self.definition)

@dataclass
class ItemShopEntryPrice:
    basePrice: float
    currencySubType: float
    currencyType: str
    dynamicRegularPrice: float
    finalPrice: float
    regularPrice: float
    saleExpiration: str

@dataclass
class ItemShopEntryGrant:
    minQuantity: float
    requiredId: str
    requirementType: str

@dataclass
class ItemShopEntry:
    size: str
    sortPriority: float
    catalogGroupPriority: float
    devName: str
    offerId: str
    offerTag: str
    baseItem: Optional[Definition]
    images: List[NewDisplayAsset]
    prices: List[ItemShopEntryPrice]
    bundleInfo: Optional[ItemShopEntryBundle]
    newDisplayAssetPath: str
    displayAssetPath: str
    templateId: str
    giftable: bool
    colors: ItemShopEntryColors
    refundable: bool
    inDate: str
    outDate: str
    requirements: List[ItemShopEntryGrant]
    items: List[ItemShopEntryItem]
    additionalGrants: List[Any]

    def __post_init__(self):
        if isinstance(self.bundleInfo, dict):
            self.bundleInfo = ItemShopEntryBundle(**self.bundleInfo)

        self.images = [NewDisplayAsset(**img) for img in self.images]
        self.prices = [ItemShopEntryPrice(**price) for price in self.prices]
        self.items = [ItemShopEntryItem(**item) for item in self.items]
        self.requirements = [ItemShopEntryGrant(**grant) for grant in self.requirements]
        self.colors = ItemShopEntryColors(**self.colors)

        if self.baseItem and isinstance(self.baseItem, dict):
            x = self.templateId.lower().split(":")
            if len(x) > 0:
                x = x[0]
                if x == "sparkssong":
                    self.baseItem = SparkTrack(**self.baseItem)
                elif x == "athenacharacter":
                    self.baseItem = Character(**self.baseItem)
                elif x.startswith("vehiclecosmetics"):
                    self.baseItem = CarCosmetic(**self.baseItem)
                elif x.startswith("sparks"):
                    self.baseItem = Instrument(**self.baseItem)
                elif x.startswith("juno"):
                    self.baseItem = Juno(**self.baseItem)
                elif x == "cosmeticvarianttoken":
                    if not self.baseItem.get("rarity"):
                        self.baseItem = CosmeticVehicleVariant(**self.baseItem)
                    else:
                        self.baseItem = CosmeticVariantToken(**self.baseItem)
                else:
                    self.baseItem = Cosmetic(**self.baseItem)

            

@dataclass
class ItemShopRow:
    layoutId: str
    entries: List[ItemShopEntry]

    def __post_init__(self):
        self.entries = [ItemShopEntry(**entry) for entry in self.entries]

@dataclass
class ItemShopSection:
    metadata: Any
    displayName: str
    sectionId: str
    rows: List[ItemShopRow]

    def __post_init__(self):
        self.rows = [ItemShopRow(**row) for row in self.rows]

@dataclass
class ItemShopCategory:
    name: str
    sections: List[ItemShopSection]

    def __post_init__(self):
        self.sections = [ItemShopSection(**section) for section in self.sections]

@dataclass
class ItemShop:
    refreshIntervalHours: float
    dailyPurchaseHours: float
    expiration: str
    categories: List[ItemShopCategory]
    
    def __post_init__(self):
        self.categories = [ItemShopCategory(**category) for category in self.categories]