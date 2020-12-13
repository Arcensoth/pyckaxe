from pyckaxe.block import Block
from pyckaxe.block_predicate import BlockPredicate
from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.position import Position


class FillCommand(CommandLiteral):
    _LITERAL = "fill"

    def __call__(
        self, from_: Position.Thing, to: Position.Thing, block: Block
    ) -> "FillFromToBlockCommand":
        return self.from_(from_).to(to).block(block)

    def from_(self, from_: Position.Thing) -> "FillFromCommand":
        return FillFromCommand(self, from_)


class FillFromCommand(CommandArgument):
    _TYPE = Position

    def to(self, to: Position.Thing) -> "FillFromToCommand":
        return FillFromToCommand(self, to)


class FillFromToCommand(CommandArgument):
    _TYPE = Position

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

    def __call__(self, filter_: BlockPredicate) -> "FillFromToBlockReplaceFilterCommand":
        return self.filter(filter_)

    def filter(self, filter_: BlockPredicate) -> "FillFromToBlockReplaceFilterCommand":
        return FillFromToBlockReplaceFilterCommand(self, filter_)


class FillFromToBlockReplaceFilterCommand(CommandArgument):
    pass
