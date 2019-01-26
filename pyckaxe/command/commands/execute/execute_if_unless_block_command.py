from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.command.commands.execute.execute_command_mixin import ExecuteCommandMixin
from pyckaxe.types import BlockPredicate, Position


class ExecuteIfUnlessBlockCommand(CommandLiteral):
    _LITERAL = "block"

    def __call__(
        self, position: Position, block: BlockPredicate
    ) -> "ExecuteIfUnlessBlockPositionBlockCommand":
        return self.position(position).block(block)

    def position(self, position: Position) -> "ExecuteIfUnlessBlockPositionCommand":
        return ExecuteIfUnlessBlockPositionCommand(self, position)


class ExecuteIfUnlessBlockPositionCommand(CommandArgument):
    def block(
        self, block: BlockPredicate
    ) -> "ExecuteIfUnlessBlockPositionBlockCommand":
        return ExecuteIfUnlessBlockPositionBlockCommand(self, block)


class ExecuteIfUnlessBlockPositionBlockCommand(CommandArgument, ExecuteCommandMixin):
    pass
