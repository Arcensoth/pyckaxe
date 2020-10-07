from abc import ABC, abstractmethod
from typing import Iterable


class CommandToken(ABC):
    @abstractmethod
    def command_stringify(self) -> Iterable[str]:
        """ Stringify the object into a command token. """
