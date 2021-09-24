from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Iterable, List, Optional, Union

from pyckaxe.lib.block_state import BlockState
from pyckaxe.lib.nbt import NbtCompound
from pyckaxe.lib.types import JsonValue
from pyckaxe.utils.utils import is_submapping

__all__ = (
    "BlockConvertible",
    "Block",
)


BlockConvertible = Union["Block", str]


@dataclass
class Block:
    name: str
    state: Optional[BlockState] = None
    data: Optional[NbtCompound] = None

    @classmethod
    def convert(cls, value: BlockConvertible) -> Block:
        if isinstance(value, cls):
            return value
        assert isinstance(value, str)
        return cls.from_string(value)

    @classmethod
    def from_string(cls, s: str) -> Block:
        return cls(name=s)

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return "".join(self._str_parts())

    def __hash__(self) -> int:
        return hash(str(self))

    def _str_parts(self) -> Iterable[str]:
        yield self.name
        if self.state is not None:
            yield str(self.state)
        if self.data is not None:
            yield str(self.data.snbt())

    def matches(self, other: Block) -> bool:
        """Check whether this `Block` is a subset of another."""
        if self.name != other.name:
            return False
        if other.state is not None:
            if self.state is not None:
                return self.state.matches(other.state)
            return False
        if other.data is not None:
            if self.data is not None:
                return is_submapping(self.data, other.data)
            return False
        return True

    def matches_any_of(self, others: List[Block]) -> bool:
        """Check whether this `Block` is a subset of any others."""
        return any(self.matches(other) for other in others)

    def matches_all_of(self, others: List[Block]) -> bool:
        """Check whether this `Block` is a subset of all others."""
        return all(self.matches(other) for other in others)

    # @implements JsonSerializable
    def to_json(self) -> JsonValue:
        data: Dict[str, JsonValue] = {"name": self.name}
        if self.state is not None:
            data["state"] = self.state.to_json()
        if self.data is not None:
            # TODO Serialize NBT into JSON. #enhance #nson
            data["data"] = self.data.snbt()
        return data
