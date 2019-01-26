from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.command.commands.execute.execute_command_mixin import ExecuteCommandMixin
from pyckaxe.types import CommandTarget


class ExecuteAtCommand(CommandLiteral):
    _LITERAL = "at"

    def __call__(self, targets: CommandTarget) -> "ExecuteAtTargetsCommand":
        return self.targets(targets)

    def targets(self, targets: CommandTarget) -> "ExecuteAtTargetsCommand":
        return ExecuteAtTargetsCommand(self, targets)


class ExecuteAtTargetsCommand(CommandArgument, ExecuteCommandMixin):
    pass
