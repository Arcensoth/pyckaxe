from abc import ABC, abstractmethod
from typing import Any, Iterable

from pyckaxe.command.abc.command_token import CommandToken
from pyckaxe.nbt import NbtBase, NbtPath


class Command(ABC):
    """ A printable command that can be iterated over to retrieve its space-delimited tokens. """

    def __str__(self):
        return " ".join(self._convert(token) for token in self._tokens())

    def __iter__(self):
        return self._tokens()

    @staticmethod
    def _convert(token) -> str:
        if isinstance(token, CommandToken):
            return token.command_stringify()
        if isinstance(token, NbtBase):
            return str(token.snbt())
        if isinstance(token, NbtPath):
            return str(token)
        if isinstance(token, bool):
            return "true" if token else "false"
        if token is None:
            raise ValueError("Cannot stringify None into a command token")
        return str(token)

    @abstractmethod
    def _tokens(self) -> Iterable[Any]:
        """ Yield command tokens as literals or arguments. """
