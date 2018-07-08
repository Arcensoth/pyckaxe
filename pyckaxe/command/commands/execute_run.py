from pyckaxe.command.abc.command import CommandLiteral
from pyckaxe.command.commands.root import RootCommandMixin


class ExecuteRunCommand(CommandLiteral, RootCommandMixin):
    _LITERAL = 'run'
