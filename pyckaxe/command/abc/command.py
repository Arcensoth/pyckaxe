from abc import abstractmethod
from typing import Iterable

__all__ = ("Command",)


class Command:
    def __str__(self) -> str:
        return " ".join(token for token in self._command_tokens())

    @abstractmethod
    def _command_tokens(self) -> Iterable[str]:
        """ Yield stringified command tokens. """
