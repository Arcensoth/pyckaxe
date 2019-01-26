from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.command.commands.execute.execute_command_mixin import ExecuteCommandMixin
from pyckaxe.types import CommandTarget


class ExecuteAsCommand(CommandLiteral):
    _LITERAL = "as"

    def __call__(self, targets: CommandTarget) -> "ExecuteAsTargetsCommand":
        return self.targets(targets)

    def targets(self, targets: CommandTarget) -> "ExecuteAsTargetsCommand":
        return ExecuteAsTargetsCommand(self, targets)


class ExecuteAsTargetsCommand(CommandArgument, ExecuteCommandMixin):
    pass
