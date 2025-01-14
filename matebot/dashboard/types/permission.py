from dataclasses import dataclass
from typing import List

@dataclass
class Permission:
    """
    Permission types:

    ~~~~~~~~~~
    1: Who have these roles
    2: Who doesn't have these roles
    ~~~~~~~~~~
    """
    type: int

    member: bool
    roles: List[str]

@dataclass
class DPermission:
    """
    Permission types:

    ~~~~~~~~~~
    1: Who have these roles
    2: Who doesn't have these roles
    ~~~~~~~~~~
    """
    type: int

    roles: List[str]
