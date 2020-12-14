from typing import Any, Iterable, Optional, Tuple

from pyckaxe.command.abc.command import Command


class RawCommand(Command):
    """
    A wrapper used to encapsulate an arbitrary, raw command string that can be optionally attached
    to the end of another command.
    """

    def __init__(self, *tokens: str, parent: "Command" = None):
        self._tokens_tuple: Tuple[Any] = tuple(tokens)
        self._parent: Optional[Command] = parent

    def _tokens(self) -> Iterable[Any]:
        yield from self._parent or ()
        yield from self._tokens_tuple
