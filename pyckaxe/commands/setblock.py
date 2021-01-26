from pyckaxe.any_block import AnyBlock
from pyckaxe.command.abc.command_node import CommandArgument, CommandLiteral
from pyckaxe.position import Position


class SetblockCommand(CommandLiteral):
    _LITERAL = "setblock"

    def __call__(self, position: Position.Thing, block: AnyBlock) -> "SetblockPositionBlockCommand":
        return self.position(position).block(block)

    def position(self, position: Position.Thing) -> "SetblockPositionCommand":
        return SetblockPositionCommand(self, position)


class SetblockPositionCommand(CommandArgument):
    _TYPE = Position

    def block(self, block: AnyBlock) -> "SetblockPositionBlockCommand":
        return SetblockPositionBlockCommand(self, block)


class SetblockPositionBlockCommand(CommandArgument):
    @property
    def destroy(self) -> "SetblockPositionBlockDestroyCommand":
        return SetblockPositionBlockDestroyCommand(self)

    @property
    def keep(self) -> "SetblockPositionBlockKeepCommand":
        return SetblockPositionBlockKeepCommand(self)

    @property
    def replace(self) -> "SetblockPositionBlockReplaceCommand":
        return SetblockPositionBlockReplaceCommand(self)


class SetblockPositionBlockDestroyCommand(CommandLiteral):
    _LITERAL = "destroy"


class SetblockPositionBlockKeepCommand(CommandLiteral):
    _LITERAL = "keep"


class SetblockPositionBlockReplaceCommand(CommandLiteral):
    _LITERAL = "replace"
