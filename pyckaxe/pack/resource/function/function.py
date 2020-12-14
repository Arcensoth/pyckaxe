from dataclasses import dataclass
from typing import Iterable, List, Union

from pyckaxe.command.abc.command import Command
from pyckaxe.command.debug_command import DebugCommand
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
    async def serialize(self, production: bool = False, **options) -> str:
        lines = self.production_commands if production else self.lines
        return "\n".join(str(line) for line in lines)

    @property
    def commands(self) -> Iterable[Command]:
        for line in self.lines:
            if isinstance(line, Command):
                yield line

    @property
    def production_commands(self) -> Iterable[Command]:
        for command in self.commands:
            if not isinstance(command, DebugCommand):
                yield command
