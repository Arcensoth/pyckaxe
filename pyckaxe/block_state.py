from collections.abc import MutableMapping
from dataclasses import dataclass

from nbtlib import tag

from pyckaxe.abc.nbt_serializable import NbtSerializable
from pyckaxe.abc.serializable import Serializable
from pyckaxe.command.abc.command_token import CommandToken


@dataclass
class BlockState(MutableMapping, CommandToken, Serializable):
    _value: dict

    # @implements MutableMapping
    def __setitem__(self, k, v):
        if not isinstance(v, (str, float, int, bool)):
            raise ValueError(
                f"Invalid value type for {self.__class__.__name__}: {k.__class__.__name__}"
            )
        self._value.__setitem__(k, v)

    # @implements MutableMapping
    def __getitem__(self, k):
        return self._value.__getitem__(k)

    # @implements MutableMapping
    def __delitem__(self, v):
        self._value.__delitem__(v)

    # @implements MutableMapping
    def __len__(self):
        return self._value.__len__()

    # @implements MutableMapping
    def __iter__(self):
        return self._value.__iter__()

    # @implements Serializable
    def serialize(self) -> dict:
        return self._value

    # @implements NbtSerializable
    def to_nbt(self) -> tag.Compound:
        # NOTE All block state property values are encoded as strings in NBT.
        c = tag.Compound()
        for k, v in self.items():
            if isinstance(v, bool):
                v = "true" if v else "false"
            elif isinstance(v, (int, float, str)):
                v = str(v)
            else:
                raise ValueError(f"Invalid block state value: {v}")
            c[k] = tag.String(v)
        return c

    # @implements CommandToken
    def command_stringify(self) -> str:
        innards = ",".join(f"{k}={v}" for k, v in self._value.items())
        return f"[{innards}]"
