from dataclasses import dataclass
from typing import Iterable, List, Union

from pyckaxe.command.abc.command import Command
from pyckaxe.pack.resource.abc.resource import RawResource


@dataclass
class Function(RawResource):
    lines: List[Union[Command, str]]

    _file_suffix = ".mcfunction"

    # @implements Resource
    @staticmethod
    async def deserialize(raw: str) -> "Function":
        assert isinstance(raw, str)
        lines = raw.split("\n")
        return Function(lines=lines)

    # @implements Resource
    async def serialize(self) -> str:
        return "\n".join(str(line) for line in self.lines)

    @property
    def commands(self) -> Iterable[Command]:
        for line in self.lines:
            if isinstance(line, Command):
                yield line
