from collections.abc import MutableMapping
from dataclasses import dataclass

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

    # @implements CommandToken
    def command_stringify(self) -> str:
        innards = ",".join(f"{k}={v}" for k, v in self._value.items())
        return f"[{innards}]"
