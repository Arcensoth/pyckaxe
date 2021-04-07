from typing import Iterable, Optional

from pyckaxe.command.abc.command import Command

__all__ = ("RawCommand",)


class RawCommand(Command):
    """
    A wrapper used to encapsulate an arbitrary, raw command string that can be
    optionally attached to the end of another command.
    """

    def __init__(self, raw_command: str, parent: Optional[Command] = None):
        self._raw_command: str = raw_command
        self._parent: Optional[Command] = parent

    def command_tokens(self) -> Iterable[str]:
        if self._parent is not None:
            yield from self._parent.command_tokens()
        yield self._raw_command
