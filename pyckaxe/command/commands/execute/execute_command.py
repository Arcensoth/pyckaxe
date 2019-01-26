from pyckaxe.command.commands.execute.execute_command_mixin import ExecuteCommandMixin
from pyckaxe.command.abc.command import CommandLiteral


class ExecuteCommand(CommandLiteral, ExecuteCommandMixin):
    _LITERAL = "execute"
