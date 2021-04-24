from dataclasses import dataclass
from typing import Dict, MutableMapping, Union, cast

from pyckaxe.lib.nbt import NbtCompound, NbtString
from pyckaxe.lib.types import JsonValue

__all__ = (
    "BlockState",
    "BlockStateValue",
)

BlockStateValue = Union[bool, int, float, str]


@dataclass
class BlockState(MutableMapping[str, BlockStateValue]):
    _map: Dict[str, BlockStateValue]

    def __str__(self) -> str:
        innards = ",".join(f"{k}={v}" for k, v in self._map.items())
        return f"[{innards}]"

    # @implements MutableMapping
    def __setitem__(self, key: str, value: BlockStateValue):
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

    # @implements JsonSerializable
    def to_json(self) -> JsonValue:
        return cast(JsonValue, self._map)

    # @implements NbtSerializable
    def to_nbt(self) -> NbtCompound:
        # NOTE All block state property values are encoded as strings in NBT.
        nbt_compound = NbtCompound()
        for key, value in self.items():
            if isinstance(value, bool):
                value = "true" if value else "false"
            assert isinstance(value, (int, float, str))
            nbt_compound[key] = NbtString(str(value))
        return nbt_compound
