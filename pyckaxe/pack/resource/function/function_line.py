from dataclasses import dataclass
from typing import Union

from pyckaxe.command.abc.command import Command


@dataclass
class FunctionLine:
    content: Union[Command, str]

    def __str__(self) -> str:
        return str(self.content)
