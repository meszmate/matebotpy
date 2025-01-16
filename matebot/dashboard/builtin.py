from dataclasses import dataclass
from typing import List
from matebot.dashboard.types import ActionRow, PageActionRow, Embed

@dataclass
class BuiltinBasic:
    content: str
    embeds: List[Embed]
    actionrows: List[ActionRow]

    def add_embed(self, embed: Embed) -> None:
        self.embeds.append(embed)
    
    def set_embeds(self, embeds: List[Embed]) -> None:
        self.embeds = embeds
    
    def set_embed(self, index: int, embed: Embed) -> None:
        self.embeds[index] = embed
    
    def remove_embed(self, index: int) -> None:
        del self.embeds[index]

    def add_actionrow(self, actionrow: ActionRow) -> None:
        self.actionrows.append(actionrow)
    
    def set_actionrows(self, actionrows: List[ActionRow]) -> None:
        self.actionrows = actionrows
    
    def set_actionrow(self, index: int, actionrow: ActionRow) -> None:
        self.actionrows[index] = actionrow
    
    def remove_actionrow(self, index: int) -> None:
        del self.actionrows[index]

@dataclass
class BuiltinMessage:
    content: str
    embeds: List[Embed]
    actionrows: List[ActionRow]
    id: str

    def add_embed(self, embed: Embed) -> None:
        self.embeds.append(embed)
    
    def set_embeds(self, embeds: List[Embed]) -> None:
        self.embeds = embeds
    
    def set_embed(self, index: int, embed: Embed) -> None:
        self.embeds[index] = embed
    
    def remove_embed(self, index: int) -> None:
        del self.embeds[index]

    def add_actionrow(self, actionrow: ActionRow) -> None:
        self.actionrows.append(actionrow)
    
    def set_actionrows(self, actionrows: List[ActionRow]) -> None:
        self.actionrows = actionrows
    
    def set_actionrow(self, index: int, actionrow: ActionRow) -> None:
        self.actionrows[index] = actionrow
    
    def remove_actionrow(self, index: int) -> None:
        del self.actionrows[index]

@dataclass
class BuiltinPageBasic:
    max: str
    count: str
    content: str
    embeds: List[Embed]
    actionrows: List[ActionRow]

    def add_embed(self, embed: Embed) -> None:
        self.embeds.append(embed)
    
    def set_embeds(self, embeds: List[Embed]) -> None:
        self.embeds = embeds
    
    def set_embed(self, index: int, embed: Embed) -> None:
        self.embeds[index] = embed
    
    def remove_embed(self, index: int) -> None:
        del self.embeds[index]

    def add_actionrow(self, actionrow: ActionRow) -> None:
        self.actionrows.append(actionrow)
    
    def set_actionrows(self, actionrows: List[ActionRow]) -> None:
        self.actionrows = actionrows
    
    def set_actionrow(self, index: int, actionrow: ActionRow) -> None:
        self.actionrows[index] = actionrow
    
    def remove_actionrow(self, index: int) -> None:
        del self.actionrows[index]
    
@dataclass
class BuiltinWithErr:
    success: BuiltinBasic
    error: BuiltinBasic

@dataclass
class BuiltinPageWithErr:
    success: BuiltinPageBasic
    error: BuiltinBasic

@dataclass
class Builtin:
    clear: BuiltinBasic
    warning: BuiltinWithErr
    warnings: BuiltinPageWithErr
    delwarning: BuiltinWithErr
    clearwarnings: BuiltinBasic
    mute: BuiltinWithErr
    rankcard: BuiltinBasic
    xpleaderboard: BuiltinPageBasic
    balance: BuiltinBasic
    ecoleaderboard: BuiltinPageBasic
    giveaway: BuiltinBasic
    giveawayend: BuiltinBasic
    giveawayreroll: BuiltinBasic
    messages: List[BuiltinMessage]

    def add_message(self, message: BuiltinMessage) -> None:
        self.messages.append(message)
    
    def set_messages(self, messages: List[BuiltinMessage]) -> None:
        self.messages = messages
    
    def set_message(self, index: int, message: BuiltinMessage) -> None:
        self.messages[index] = message
    
    def remove_message(self, index: int) -> None:
        del self.messages[index]
    
    def remove_message_by_id(self, id: str) -> None:
        self.messages = [message for message in self.messages if message.id != id]