from dataclasses import dataclass
from typing import Iterable, Optional

from nbtlib import tag

from pyckaxe.block_state import BlockState
from pyckaxe.command.abc.command_token import CommandToken


@dataclass
class Block(CommandToken):
    name: str
    state: Optional[BlockState] = None
    data: Optional[tag.Compound] = None

    def _command_stringify(self) -> Iterable[str]:
        yield self.name
        if self.state is not None:
            yield self.state.command_stringify()
        if self.data is not None:
            yield str(self.data.snbt())

    # @implements CommandToken
    def command_stringify(self) -> str:
        return "".join(self._command_stringify())
