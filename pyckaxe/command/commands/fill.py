from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.types import Block, BlockPredicate, Position


class FillCommand(CommandLiteral):
    _LITERAL = "fill"

    def __call__(
        self, from_: Position, to: Position, block: Block
    ) -> "FillFromToBlockCommand":
        return self.from_(from_).to(to).block(block)

    def from_(self, from_: Position) -> "FillFromCommand":
        return FillFromCommand(self, from_)


class FillFromCommand(CommandArgument):
    def to(self, to: Position) -> "FillFromToCommand":
        return FillFromToCommand(self, to)


class FillFromToCommand(CommandArgument):
    def block(self, block: Block) -> "FillFromToBlockCommand":
        return FillFromToBlockCommand(self, block)


class FillFromToBlockCommand(CommandArgument):
    @property
    def destroy(self) -> "FillFromToBlockDestroyCommand":
        return FillFromToBlockDestroyCommand(self)

    @property
    def hollow(self) -> "FillFromToBlockHollowCommand":
        return FillFromToBlockHollowCommand(self)

    @property
    def keep(self) -> "FillFromToBlockKeepCommand":
        return FillFromToBlockKeepCommand(self)

    @property
    def outline(self) -> "FillFromToBlockOutlineCommand":
        return FillFromToBlockOutlineCommand(self)

    @property
    def replace(self) -> "FillFromToBlockReplaceCommand":
        return FillFromToBlockReplaceCommand(self)


class FillFromToBlockDestroyCommand(CommandLiteral):
    _LITERAL = "destroy"


class FillFromToBlockHollowCommand(CommandLiteral):
    _LITERAL = "hollow"


class FillFromToBlockKeepCommand(CommandLiteral):
    _LITERAL = "keep"


class FillFromToBlockOutlineCommand(CommandLiteral):
    _LITERAL = "outline"


class FillFromToBlockReplaceCommand(CommandLiteral):
    _LITERAL = "replace"

    def __call__(self, filter: BlockPredicate) -> "FillFromToBlockReplaceFilterCommand":
        return self.filter(filter)

    def filter(self, filter: BlockPredicate) -> "FillFromToBlockReplaceFilterCommand":
        return FillFromToBlockReplaceFilterCommand(self, filter)


class FillFromToBlockReplaceFilterCommand(CommandArgument):
    pass
