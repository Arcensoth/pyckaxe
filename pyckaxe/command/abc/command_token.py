from abc import ABC, abstractmethod

__all__ = ("CommandToken",)


class CommandToken(ABC):
    @abstractmethod
    def command_tokenize(self) -> str:
        """ Stringify the object into a command token. """
