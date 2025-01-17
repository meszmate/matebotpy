from dataclasses import dataclass
from typing import List
from matebot.dashboard.types import DPermission, Action

@dataclass
class WarnAutomation:
    """
    The number of warns needed to trigger the automation.
    """
    warns: str

    permission: DPermission
    
    def set_permission(self, permission: DPermission) -> None:
        self.permission = permission

    actions: List[Action]

    def add_action(self, action: Action) -> None:
        self.actions.append(action)
    
    def set_actions(self, actions: List[Action]) -> None:
        self.actions = actions
    
    def set_action(self, index: int, action: Action) -> None:
        self.actions[index] = action
    
    def remove_action(self, index: int) -> None:
        del self.actions[index]

@dataclass
class Warn:
    """
    Name if the author is in the server; otherwise, their ID.
    """
    author: str

    target: str
    time: int
    reason: str