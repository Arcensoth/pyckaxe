from pyckaxe.command.abc.command import CommandLiteral
from pyckaxe.command.commands._root.root_command_mixin import RootCommandMixin


class ExecuteRunCommand(CommandLiteral, RootCommandMixin):
    _LITERAL = "run"
