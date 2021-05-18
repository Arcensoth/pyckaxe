from abc import abstractmethod
from typing import Iterable, Iterator

__all__ = ("Command",)


class Command(Iterable[str]):
    def __str__(self) -> str:
        return " ".join(token for token in self)

    @abstractmethod
    def __iter__(self) -> Iterator[str]:
        """Yield stringified command tokens."""
