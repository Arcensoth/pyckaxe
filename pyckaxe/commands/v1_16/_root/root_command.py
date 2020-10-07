import typing

from pyckaxe.command.abc.command import CommandNode
from pyckaxe.commands.v1_16._root.root_command_mixin import RootCommandMixin


class RootCommand(CommandNode, RootCommandMixin):
    def __init__(self):
        super().__init__(None, None)

    def _tokens(self) -> typing.Iterable[typing.Any]:
        yield from ()
