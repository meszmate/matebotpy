from dataclasses import dataclass
from typing import Any, List, Optional, Union
from matebot.fortnite import Definition, NewDisplayAsset

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
    templateId: str
    quantity: float

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
    bundleInfo: Optional[ItemShopEntryBundleItemInfo]
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

@dataclass
class ItemShopRow:
    layoutId: str
    entries: List[ItemShopEntry]

@dataclass
class ItemShopSection:
    metadata: Any
    displayName: str
    sectionId: str
    rows: List[ItemShopRow]

@dataclass
class ItemShopCategory:
    name: str
    sections: List[ItemShopSection]

@dataclass
class ItemShop:
    refreshIntervalHours: float
    dailyPurchaseHours: float
    expiration: str
    categories: List[ItemShopCategory]