from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, Iterable, Optional, Union

from pyckaxe.lib.block_state import BlockState
from pyckaxe.lib.nbt import NbtCompound, to_nbt
from pyckaxe.lib.types import JsonValue

__all__ = (
    "BlockConvertible",
    "Block",
)


BlockConvertible = Union[
    "Block",
    str,
    Dict[str, Any],
]


@dataclass
class Block:
    name: str
    state: Optional[BlockState] = None
    data: Optional[NbtCompound] = None

    @classmethod
    def convert(cls, value: BlockConvertible) -> Block:
        if isinstance(value, cls):
            return value
        if isinstance(value, str):
            return cls.from_string(value)
        assert isinstance(value, dict)
        return cls.from_json(value)

    @classmethod
    def from_string(cls, s: str) -> Block:
        return cls(name=s)

    @classmethod
    def from_json(cls, d: Dict[str, Any]) -> Block:
        # name
        name = d["block"]
        assert isinstance(name, str)
        # state
        raw_state = d.get("state")
        state = BlockState(raw_state) if raw_state is not None else None
        # data
        raw_data = d.get("data")
        data = to_nbt(raw_data) if raw_data is not None else None
        if data is not None:
            assert isinstance(data, NbtCompound)
        return cls(name=name, state=state, data=data)

    def __str__(self) -> str:
        return "".join(self._str_parts())

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, self.__class__)
            and (other.name == self.name)
            and (other.state == self.state)
            and (other.data == self.data)
        )

    def _str_parts(self) -> Iterable[str]:
        yield self.name
        if self.state is not None:
            yield self.state.to_command_token()
        if self.data is not None:
            yield str(self.data.snbt())

    # @implements JsonSerializable
    def to_json(self) -> JsonValue:
        data: Dict[str, JsonValue] = {"name": self.name}
        if self.state is not None:
            data["state"] = self.state.to_json()
        if self.data is not None:
            # TODO Serialize NBT into JSON. #enhance #nson
            data["data"] = self.data.snbt()
        return data
