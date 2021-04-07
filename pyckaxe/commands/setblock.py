from typing import Any, Optional

from pyckaxe.block import Block, BlockConvertible, to_block
from pyckaxe.command import (
    CommandArgument,
    CommandLiteral,
    command_argument,
    command_literal,
)
from pyckaxe.position import Position, PositionConvertible, to_position


class SetblockDescriptor:
    def __get__(self, obj: Any, objtype: Optional[type] = None) -> "SetblockCommand":
        return SetblockCommand(None)


@command_literal("setblock")
class SetblockCommand(CommandLiteral):
    def __call__(
        self, position: PositionConvertible, block: BlockConvertible
    ) -> "SetblockPositionBlockCommand":
        # return self.position(position).block(block)
        return SetblockPositionCommand(self, to_position(position))(block)

    # def position(self, position: PositionConvertible) -> "SetblockPosition":
    #     return SetblockPosition(self, Position.from_thing(position))


@command_argument(Position)
class SetblockPositionCommand(CommandArgument[Position]):
    def __call__(self, block: BlockConvertible) -> "SetblockPositionBlockCommand":
        return SetblockPositionBlockCommand(self, to_block(block))

    # def block(self, block: BlockConvertible) -> "SetblockPositionBlock":
    #     return SetblockPositionBlock(self, thing_to_block(block))


@command_argument(Block)
class SetblockPositionBlockCommand(CommandArgument[Block]):
    @property
    def destroy(self) -> "SetblockPositionBlockDestroyCommand":
        return SetblockPositionBlockDestroyCommand(self)

    @property
    def keep(self) -> "SetblockPositionBlockKeepCommand":
        return SetblockPositionBlockKeepCommand(self)

    @property
    def replace(self) -> "SetblockPositionBlockReplaceCommand":
        return SetblockPositionBlockReplaceCommand(self)


@command_literal("destroy")
class SetblockPositionBlockDestroyCommand(CommandLiteral):
    pass


@command_literal("keep")
class SetblockPositionBlockKeepCommand(CommandLiteral):
    pass


@command_literal("replace")
class SetblockPositionBlockReplaceCommand(CommandLiteral):
    pass
