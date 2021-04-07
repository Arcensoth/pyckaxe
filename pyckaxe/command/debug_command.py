from typing import Iterable

from pyckaxe.command.abc.command import Command

__all__ = ("DebugCommand",)


class DebugCommand(Command):
    """
    A wrapper used to signify that the underlying [Command] is ued for debugging and
    should not be included in a production build.
    """

    def __init__(self, command: Command):
        self._command: Command = command

    def command_tokens(self) -> Iterable[str]:
        yield from self._command.command_tokens()
