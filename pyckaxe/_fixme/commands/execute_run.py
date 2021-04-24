from pyckaxe.command.abc.command_node import CommandLiteral
from pyckaxe.commands._root.root_command_mixin import RootCommandMixin

# NOTE This is maintained separately to avoid a circular import with the root command.


class ExecuteRunCommand(CommandLiteral, RootCommandMixin):
    _LITERAL = "run"
