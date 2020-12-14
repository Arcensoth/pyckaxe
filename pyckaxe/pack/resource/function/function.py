from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Optional, Union

from pyckaxe.command.abc.command import Command
from pyckaxe.pack.resource.abc.resource import RawResource


@dataclass
class Function(RawResource):
    lines: List[Union[Command, str]]

    _file_suffix = ".mcfunction"

    # @implements Resource
    @staticmethod
    async def deserialize(raw: str, **options) -> "Function":
        assert isinstance(raw, str)
        lines = raw.split("\n")
        return Function(lines=lines)

    # @implements Resource
    async def serialize(self, compact: bool = False, **options) -> str:
        lines = self.commands if compact else self.lines
        return "\n".join(str(line) for line in lines)

    @property
    def commands(self) -> Iterable[Command]:
        for line in self.lines:
            if isinstance(line, Command):
                yield line
