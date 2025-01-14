from dataclasses import dataclass
from typing import List, Optional
from matebot.dashboard.types import Action, Permission

@dataclass
class Emoji:
    """
    Emoji types:

    ~~~~~~~~~~
    0: None
    1: Normal Emoji
    2: Discord Emoji
    ~~~~~~~~~~
    """
    type: int
    name: str
    id: str
    animated: bool

@dataclass
class Form:
    label: str
    placeholder: str
    long: bool
    required: bool
    min: str
    max: str
    value: str

@dataclass
class ActionStruct:
    actions: List[Action]
    title: str
    forms: List[Form]

@dataclass
class Button:
    """
    Button styles:

    ~~~~~~~~~~
    1: Primary (blue)
    2: Secondary (grey)
    3: Success (green)
    4: Danger (red)
    5: Link (grey)
    ~~~~~~~~~~
    """
    style: int

    disabled: bool
    label: str
    url: str
    emoji: Emoji
    action: ActionStruct
    erractions: List[Action]
    permactions: List[Action]
    cooldownactions: List[Action]
    cooldown: int
    isglobal: bool
    shared: bool
    permission: Permission

@dataclass
class Option:
    label: str
    description: str
    emoji: Emoji
    permission: Permission
    action: ActionStruct
    erractions: List[Action]
    permactions: List[Action]
    cooldownactions: List[Action]
    cooldown: int
    isglobal: bool
    shared: bool

@dataclass
class SelectMenu:
    """
    SelectMenu types:

    ~~~~~~~~~~
    1: Normal
    2: Users
    3: Roles
    4: Mentionables
    5: Channels
    ~~~~~~~~~~
    """
    type: int

    placeholder: str
    disabled: bool
    options: List[Option]

@dataclass
class ActionRow:
    type: int
    buttons: List[Button]
    selectmenu: SelectMenu