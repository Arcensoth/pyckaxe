from dataclasses import dataclass
from typing import Iterable, Optional

from nbtlib import tag

from pyckaxe.abc.serializable import Serializable
from pyckaxe.block_state import BlockState
from pyckaxe.command.abc.command_token import CommandToken
from pyckaxe.utils.nbt import to_nbt


@dataclass
class Block(CommandToken, Serializable):
    name: str
    state: Optional[BlockState] = None
    data: Optional[tag.Compound] = None

    @staticmethod
    def deserialize(raw: dict) -> "Block":
        assert isinstance(raw, dict)
        name = raw["block"]
        raw_state = raw.get("state")
        state = BlockState(raw_state) if raw_state is not None else None
        raw_data = raw.get("data")
        data = to_nbt(raw_data) if raw_data is not None else None
        return Block(name=name, state=state, data=data)

    # @implements Serializable
    def serialize(self) -> dict:
        # FIXME Shouldn't `data` be a dict as well?
        return {
            "name": self.name,
            "state": self.state.serialize(),
            "data": self.data.snbt(),
        }

    def _command_stringify(self) -> Iterable[str]:
        yield self.name
        if self.state is not None:
            yield self.state.command_stringify()
        if self.data is not None:
            yield str(self.data.snbt())

    # @implements CommandToken
    def command_stringify(self) -> str:
        return "".join(self._command_stringify())
