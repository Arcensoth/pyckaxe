from dataclasses import dataclass
from typing import Iterable, Optional

from pyckaxe.block_state import BlockState
from pyckaxe.command.abc.command_token import CommandToken
from pyckaxe.data_tag import CompoundDataTag


@dataclass
class Block(CommandToken):
    name: str
    state: Optional[BlockState] = None
    data: Optional[CompoundDataTag] = None

    def _command_stringify(self) -> Iterable[str]:
        yield self.name
        if self.state is not None:
            yield self.state.command_stringify()
        if self.data is not None:
            yield self.data.command_stringify()

    # @implements CommandToken
    def command_stringify(self) -> str:
        return "".join(self._command_stringify())
