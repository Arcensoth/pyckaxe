from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.types import CommandTarget, EntityTag


class TagTargetsAddRemoveCommandMixin:
    def __call__(self, tag: EntityTag) -> "TagTargetsAddRemoveTagCommand":
        return self.tag(tag)

    def tag(self, tag: EntityTag) -> "TagTargetsAddRemoveTagCommand":
        return TagTargetsAddRemoveTagCommand(self, tag)


class TagCommand(CommandLiteral):
    _LITERAL = "tag"

    def __call__(self, targets: CommandTarget) -> "TagTargetsCommand":
        return self.targets(targets)

    def targets(self, targets: CommandTarget) -> "TagTargetsCommand":
        return TagTargetsCommand(self, targets)


class TagTargetsCommand(CommandArgument):
    @property
    def add(self) -> "TagTargetsAddCommand":
        return TagTargetsAddCommand(self)

    @property
    def remove(self) -> "TagTargetsRemoveCommand":
        return TagTargetsRemoveCommand(self)

    @property
    def list(self) -> "TagTargetsListCommand":
        return TagTargetsListCommand(self)


class TagTargetsAddCommand(CommandLiteral, TagTargetsAddRemoveCommandMixin):
    _LITERAL = "add"


class TagTargetsRemoveCommand(CommandLiteral, TagTargetsAddRemoveCommandMixin):
    _LITERAL = "remove"


class TagTargetsListCommand(CommandLiteral):
    _LITERAL = "list"


class TagTargetsAddRemoveTagCommand(CommandArgument):
    pass
