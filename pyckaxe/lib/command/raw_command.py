from typing import Iterator, Optional

from pyckaxe.lib.command.command import Command

__all__ = ("RawCommand",)


class RawCommand(Command):
    """
    A wrapper used to encapsulate an arbitrary, raw command string.

    This can be optionally attached to the end of another command via `parent`.
    """

    def __init__(self, raw_command: str, parent: Optional[Command] = None):
        self._raw_command: str = raw_command
        self._parent: Optional[Command] = parent

    # @implements Command
    def __iter__(self) -> Iterator[str]:
        if self._parent is not None:
            yield from self._parent
        yield self._raw_command
