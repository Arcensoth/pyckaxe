from dataclasses import dataclass
from typing import Iterable, List, Union

from pyckaxe.command.abc.command import Command
from pyckaxe.pack.resource.abc.resource import RawResource


@dataclass
class Function(RawResource):
    lines: List[Union[Command, str]]

    # @implements Resource
    @staticmethod
    async def from_raw(raw: str) -> "Function":
        assert isinstance(raw, str)
        lines = raw.split("\n")
        return Function(lines=lines)

    @property
    def commands(self) -> Iterable[Command]:
        for line in self.lines:
            if isinstance(line, Command):
                yield line
