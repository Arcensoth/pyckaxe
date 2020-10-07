from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.types import CommandTarget, Item


class GiveCommand(CommandLiteral):
    _LITERAL = "give"

    def __call__(
        self, targets: CommandTarget, item: Item, count: int
    ) -> "GiveTargetsItemCountCommand":
        return self.targets(targets).item(item).count(count)

    def targets(self, targets: CommandTarget) -> "GiveTargetsCommand":
        return GiveTargetsCommand(self, targets)


class GiveTargetsCommand(CommandArgument):
    def item(self, item: Item) -> "GiveTargetsItemCommand":
        return GiveTargetsItemCommand(self, item)


class GiveTargetsItemCommand(CommandArgument):
    def count(self, count: int) -> "GiveTargetsItemCountCommand":
        return GiveTargetsItemCountCommand(self, count)


class GiveTargetsItemCountCommand(CommandArgument):
    pass
