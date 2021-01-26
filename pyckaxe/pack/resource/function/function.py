from dataclasses import dataclass
from typing import Iterable, List

from pyckaxe.command.abc.command import Command
from pyckaxe.command.debug_command import DebugCommand
from pyckaxe.pack.resource.abc.resource import RawResource
from pyckaxe.pack.resource.function.function_line import FunctionLine


@dataclass
class Function(RawResource):
    lines: List[FunctionLine]

    _file_suffix = ".mcfunction"

    # @implements Resource
    @staticmethod
    async def deserialize(raw: str, **options) -> "Function":
        assert isinstance(raw, str)
        raw_lines = raw.split("\n")
        function_lines = [FunctionLine(line) for line in raw_lines]
        return Function(lines=function_lines)

    # @implements Resource
    async def serialize(self, production: bool = False, **options) -> str:
        lines = self.production_commands if production else self.lines
        return "\n".join(str(line) for line in lines)

    @property
    def commands(self) -> Iterable[Command]:
        for line in self.lines:
            content = line.content
            if isinstance(content, Command):
                yield content

    @property
    def production_commands(self) -> Iterable[Command]:
        for command in self.commands:
            if not isinstance(command, DebugCommand):
                yield command
