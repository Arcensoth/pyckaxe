from dataclasses import dataclass, field
from typing import Any, Dict, MutableMapping, Union, cast

from pyckaxe.lib.nbt import NbtCompound, NbtString
from pyckaxe.lib.types import JsonValue

__all__ = (
    "BlockStateValue",
    "InvalidBlockStateValue",
    "BlockState",
)

BlockStateValue = Union[bool, int, str]


class InvalidBlockStateValue(Exception):
    def __init__(self, value: Any):
        super().__init__(f"Invalid block state value: {value}")


@dataclass
class BlockState(MutableMapping[str, BlockStateValue]):
    _map: Dict[str, BlockStateValue] = field(init=False)

    def __init__(self, **state: BlockStateValue):
        self._map = {}
        for k, v in state.items():
            self[k] = v

    def __str__(self) -> str:
        innards = ",".join(f"{k}={v}" for k, v in self._map.items())
        return f"[{innards}]"

    # @implements MutableMapping
    def __setitem__(self, key: str, value: BlockStateValue):
        if not isinstance(value, (bool, int, str)):
            raise InvalidBlockStateValue(value)
        self._map.__setitem__(key, value)

    # @implements MutableMapping
    def __getitem__(self, key: str) -> BlockStateValue:
        return self._map.__getitem__(key)

    # @implements MutableMapping
    def __delitem__(self, key: str):
        self._map.__delitem__(key)

    # @implements MutableMapping
    def __len__(self):
        return self._map.__len__()

    # @implements MutableMapping
    def __iter__(self):
        return self._map.__iter__()

    def _stringify_value(self, value: BlockStateValue) -> str:
        if isinstance(value, bool):
            return "true" if value else "false"
        return str(value)

    # @implements JsonSerializable
    def to_json(self) -> JsonValue:
        return cast(JsonValue, self._map)

    # @implements NbtSerializable
    def to_nbt(self) -> NbtCompound:
        nbt_compound = NbtCompound()
        for key, value in self.items():
            # NOTE All block state property values are encoded as strings in NBT.
            stringified_value = self._stringify_value(value)
            nbt_compound[key] = NbtString(stringified_value)
        return nbt_compound
