from pyckaxe.command.abc.command import CommandLiteral
from pyckaxe.commands.v1_16._root.root_command_mixin import RootCommandMixin

# NOTE This is maintained separately to avoid a circular import with the root command.


class ExecuteRunCommand(CommandLiteral, RootCommandMixin):
    _LITERAL = "run"
