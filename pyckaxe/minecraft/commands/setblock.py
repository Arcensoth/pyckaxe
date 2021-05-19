from __future__ import annotations

from pyckaxe.lib import (
    Block,
    BlockConvertible,
    CommandArgument,
    CommandLiteral,
    Position,
    PositionConvertible,
    command_argument,
    command_literal,
)


@command_literal("setblock")
class SetblockCommand(CommandLiteral):
    def __call__(
        self, position: PositionConvertible, block: BlockConvertible
    ) -> SetblockPositionBlockCommand:
        return self.position(position).block(block)

    def position(self, position: PositionConvertible) -> SetblockPositionCommand:
        return SetblockPositionCommand(self, Position.convert(position))


@command_argument(Position)
class SetblockPositionCommand(CommandArgument[Position]):
    def __call__(self, block: BlockConvertible) -> SetblockPositionBlockCommand:
        return self.block(block)

    def block(self, block: BlockConvertible) -> SetblockPositionBlockCommand:
        return SetblockPositionBlockCommand(self, Block.convert(block))


@command_argument(Block)
class SetblockPositionBlockCommand(CommandArgument[Block]):
    @property
    def destroy(self) -> SetblockPositionBlockDestroyCommand:
        return SetblockPositionBlockDestroyCommand(self)

    @property
    def keep(self) -> SetblockPositionBlockKeepCommand:
        return SetblockPositionBlockKeepCommand(self)

    @property
    def replace(self) -> SetblockPositionBlockReplaceCommand:
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
