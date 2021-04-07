from dataclasses import dataclass
from typing import Any, Dict, Iterable, Optional, Union

from pyckaxe.block_state import BlockState
from pyckaxe.nbt import NbtCompound, to_nbt

__all__ = (
    "BlockConvertible",
    "to_block",
    "Block",
)


BlockConvertible = Union[
    "Block",
    str,
    Dict[str, Any],
]


def to_block(value: BlockConvertible) -> "Block":
    if isinstance(value, Block):
        return value
    if isinstance(value, str):
        return Block.from_string(value)
    assert isinstance(value, dict)
    return Block.from_dict(value)


@dataclass
class Block:
    name: str
    state: Optional[BlockState] = None
    data: Optional[NbtCompound] = None

    @classmethod
    def from_string(cls, s: str) -> "Block":
        return cls(name=s)

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Block":
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
            yield self.state.command_tokenize()
        if self.data is not None:
            yield str(self.data.snbt())

    def to_dict(self) -> Dict[str, Any]:
        # FIXME Shouldn't `data` be a dict as well?
        d: Dict[str, Any] = {"name": self.name}
        if self.state is not None:
            d["state"] = self.state.serialize()
        if self.data is not None:
            d["data"] = self.data.snbt()
        return d
