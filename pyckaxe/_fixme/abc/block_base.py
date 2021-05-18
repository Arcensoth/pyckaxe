from abc import abstractmethod
from typing import Any, Iterable, Tuple

from pyckaxe.block_state import BlockState
from pyckaxe.command.abc.command_token import CommandToken


# TODO Can we consolidate Block and BlockBase?
class BlockBase(CommandToken):
    @abstractmethod
    def _properties(self) -> Iterable[Tuple[str, Any]]:
        ...

    def state(self) -> BlockState:
        return BlockState({k: v for k, v in self._properties()})

    def _command_parts(self) -> Iterable[str]:
        yield self.NAME
        if state := self.state():
            yield state.command_tokenize()
        if self.data is not None:
            yield self.data.command_tokenize()

    # @implements CommandToken
    def command_tokenize(self) -> str:
        return "".join(self._command_parts())
