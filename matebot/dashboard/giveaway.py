from dataclasses import dataclass
from typing import List
from matebot.dashboard.types import DPermission, Action

@dataclass
class GiveawayMultiplier:
    chance: float

    permission: DPermission

    def set_permission(self, permission: DPermission) -> None:
        self.permission = permission

@dataclass
class Giveaway:
    channelid: str
    messageid: str
    description: str
    finaldescription: str
    winners: str

    permission: DPermission

    def set_permission(self, permission: DPermission) -> None:
        self.permission = permission

    expire: int

    multipliers: List[GiveawayMultiplier]

    def add_multiplier(self, multiplier: GiveawayMultiplier) -> None:
        self.multipliers.append(multiplier)
    
    def set_multipliers(self, multipliers: List[GiveawayMultiplier]) -> None:
        self.multipliers = multipliers
    
    def set_multiplier(self, index: int, multiplier: GiveawayMultiplier) -> None:
        self.multipliers[index] = multiplier
    
    def remove_multiplier(self, index: int) -> None:
        del self.multipliers[index]

    actions: List[Action]

    def add_action(self, action: Action) -> None:
        self.actions.append(action)
    
    def set_actions(self, actions: List[Action]) -> None:
        self.actions = actions
    
    def set_action(self, index: int, action: Action) -> None:
        self.actions[index] = action
    
    def remove_action(self, index: int) -> None:
        del self.actions[index]

    rerollactions: List[Action]

    def add_reroll_action(self, action: Action) -> None:
        self.rerollactions.append(action)
    
    def set_reroll_actions(self, actions: List[Action]) -> None:
        self.rerollactions = actions
    
    def set_reroll_action(self, index: int, action: Action) -> None:
        self.rerollactions[index] = action
    
    def remove_reroll_action(self, index: int) -> None:
        del self.rerollactions[index]