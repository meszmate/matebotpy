from dataclasses import dataclass
from typing import List
from matebot.dashboard.types import Action, DPermission, Channels

@dataclass
class DefenderDefault:
    value: bool
    time: int
    max: str
    permission: DPermission
    actions: List[Action]

    def add_action(self, action: Action) -> None:
        self.actions.append(action)
    
    def set_actions(self, actions: List[Action]) -> None:
        self.actions = actions

    def remove_action(self, index: int) -> None:
        del self.actions[index]

    def set_permission(self, permission: DPermission) -> None:
        self.permission = permission

@dataclass
class DefenderMessage:
    value: bool
    time: int
    max: str
    permission: DPermission
    channels: Channels
    actions: List[Action]

    def add_action(self, action: Action) -> None:
        self.actions.append(action)
    
    def set_actions(self, actions: List[Action]) -> None:
        self.actions = actions

    def remove_action(self, index: int) -> None:
        del self.actions[index]

    def set_permission(self, permission: DPermission) -> None:
        self.permission = permission

    def set_channels(self, channels: Channels) -> None:
        self.channels = channels

@dataclass
class Defender:
    ban: DefenderDefault
    kick: DefenderDefault
    invite: DefenderMessage