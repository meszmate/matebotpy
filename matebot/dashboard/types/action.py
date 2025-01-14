from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ActionMessageDeleteChoice:
    channel: int
    channelid: str
    messageid: str
    count: str
    parameters: str

@dataclass
class ActionMessageChoice:
    channel: int
    channelid: str
    messageid: str
    member: str
    message: str
    ephemeral: bool
    mention: bool

@dataclass
class ActionMessage:
    """
    Description of ActionMessage types:
    
    ~~~~~~~~~~
    1: Send - Sends a message.
    2: Reply - Replies to an existing message.
    3: Edit - Edits an existing message.
    4: Delete - Deletes a message.
    5: Bulk Delete - Deletes multiple messages.
    ~~~~~~~~~~
    """
    type: int

    """ 
    'choices' is used for action types 1, 2, and 3.
    A list of 'ActionMessageChoice' objects that represent the choices for the action (send, reply, edit).
    The bot will randomly select one of the available choices for the action.
    """
    choices: List[ActionMessageChoice]

    """ 
    'delchoices' is used for action types 4 and 5.
    A list of 'ActionMessageDeleteChoice' objects that represent the choices for deleting messages.
    The bot will randomly select one of the available delete choices for the action.
    """
    delchoices: List[ActionMessageDeleteChoice]

    def add_choice(self, choice: ActionMessageChoice) -> None:
        self.choices.append(choice)

    def set_choices(self, choices: List[ActionMessageChoice]) -> None:
        self.choices = choices
    
    def add_delchoice(self, choice: ActionMessageDeleteChoice) -> None:
        self.delchoices.append(choice)
    
    def set_delchoices(self, choices: List[ActionMessageDeleteChoice]) -> None:
        self.delchoices = choices

@dataclass
class ActionRoleChoice:
    member: str
    roleid: str
    reason: str

@dataclass
class ActionRole:
    """
    Description of ActionRole types:
    
    ~~~~~~~~~~
    1: Add - Adds a role to a user.
    2: Remove - Removes a role from a user.
    3: Toggle - Toggles the role (adds if not present, removes if present).
    4: Create - Creates a new role.
    5: Delete - Deletes a role.
    ~~~~~~~~~~
    """
    type: int

    """ 
    'choices' is used for action types 1, 2, and 3.
    A list of 'ActionRoleChoice' objects that represent the choices for the action.
    The bot will randomly select one of the choices for the action.
    """
    choices: List[ActionRoleChoice]

    """
    'roles' is used for action types 4 and 5.
    A list of role names or ids involved in the action.
    """
    roles: List[str]

@dataclass
class Action:
    """
    ~~~~~~~~~~
    1: Message
    2: Role
    3: Channel
    4: Ban
    5: Unban
    6: Kick
    7: Mute
    8: Giveaway
    9: Websocket
    10: Warning
    11: Reaction
    12: XP
    13: Economy
    14: Interaction Response (Message Update with no data)
    15: Interaction Response (Deferred Channel Message)
    16: Interaction Response (Deferred Message Update)
    ~~~~~~~~~~
    """
    type: int
    message: Optional[ActionMessage]
    role: Optional[ActionRole]