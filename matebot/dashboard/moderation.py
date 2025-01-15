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
class Warn:
    """
    Name if the author is in the server; otherwise, their ID.
    """
    author: str

    target: str
    time: int
    reason: str