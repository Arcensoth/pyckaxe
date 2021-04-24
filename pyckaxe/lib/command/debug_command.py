from typing import Iterator

from pyckaxe.lib.command.command import Command

__all__ = ("DebugCommand",)


class DebugCommand(Command):
    """
    A wrapper used to signify that the underlying [Command] is used for debugging and
    should not be included in a production build.
    """

    def __init__(self, command: Command):
        self._command: Command = command

    # @implements Command
    def __iter__(self) -> Iterator[str]:
        yield from self._command
