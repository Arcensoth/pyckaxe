from __future__ import annotations

from typing import Iterator, Optional

from pyckaxe.lib.command.command import Command
from pyckaxe.lib.command.debug_command import DebugCommand
from pyckaxe.lib.command.raw_command import RawCommand

__all__ = ("CommandNode",)


class CommandNode(Command):
    """A single node in the parent-child command hierarchy."""

    def __init__(self, parent: Optional[CommandNode]):
        self._parent: Optional[CommandNode] = parent

    def __add__(self, other: str) -> RawCommand:
        return RawCommand(other, parent=self)

    def __invert__(self) -> DebugCommand:
        return DebugCommand(self)

    # @implements Command
    def __iter__(self) -> Iterator[str]:
        if self._parent is not None:
            yield from self._parent
