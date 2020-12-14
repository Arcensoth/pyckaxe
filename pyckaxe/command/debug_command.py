from typing import Any, Iterable

from pyckaxe.command.abc.command import Command


class DebugCommand(Command):
    """
    A wrapper used to signify that the underlying [Command] is ued for debugging and should not be
    included in a production build.
    """

    def __init__(self, command: Command):
        self._command: Command = command

    def _tokens(self) -> Iterable[Any]:
        yield from self._command
