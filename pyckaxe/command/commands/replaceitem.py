from pyckaxe.command.abc.command import CommandArgument, CommandLiteral, CommandNode
from pyckaxe.types import CommandTarget, Item, ItemSlot, Position


class ReplaceitemBECommandMixin:
    def slot(self: CommandNode, slot: ItemSlot) -> "ReplaceitemBESlotCommand":
        return ReplaceitemBESlotCommand(self, slot)


class ReplaceitemCommand(CommandLiteral):
    _LITERAL = "replaceitem"

    @property
    def block(self) -> "ReplaceitemBlockCommand":
        return ReplaceitemBlockCommand(self)

    @property
    def entity(self) -> "ReplaceitemEntityCommand":
        return ReplaceitemEntityCommand(self)


class ReplaceitemBlockCommand(CommandLiteral):
    _LITERAL = "block"

    def __call__(
        self, position: Position, slot: ItemSlot, item: Item, count: int
    ) -> "ReplaceitemBESlotItemCountCommand":
        return self.position(position).slot(slot).item(item).count(count)

    def position(self, position: Position) -> "ReplaceitemBlockPositionCommand":
        return ReplaceitemBlockPositionCommand(self, position)


class ReplaceitemBlockPositionCommand(CommandArgument, ReplaceitemBECommandMixin):
    pass


class ReplaceitemEntityCommand(CommandLiteral):
    _LITERAL = "entity"

    def __call__(
        self, targets: CommandTarget, slot: ItemSlot, item: Item, count: int
    ) -> "ReplaceitemBESlotItemCountCommand":
        return self.targets(targets).slot(slot).item(item).count(count)

    def targets(self, targets: CommandTarget) -> "ReplaceitemEntityTargetsCommand":
        return ReplaceitemEntityTargetsCommand(self, targets)


class ReplaceitemEntityTargetsCommand(CommandArgument, ReplaceitemBECommandMixin):
    pass


class ReplaceitemBESlotCommand(CommandArgument):
    def item(self, item: Item) -> "ReplaceitemBESlotItemCommand":
        return ReplaceitemBESlotItemCommand(self, item)


class ReplaceitemBESlotItemCommand(CommandArgument):
    def count(self, count: int) -> "ReplaceitemBESlotItemCountCommand":
        return ReplaceitemBESlotItemCountCommand(self, count)


class ReplaceitemBESlotItemCountCommand(CommandArgument):
    pass