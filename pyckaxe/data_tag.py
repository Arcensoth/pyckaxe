import re
from collections.abc import MutableMapping
from typing import Any, List, Mapping, MutableSequence

from pyckaxe.command.abc.command_token import CommandToken

BYTE_PATTERN = re.compile(r"^(-?\d)b$")


class DataTag(CommandToken):
    pass


class CompoundDataTag(DataTag, MutableMapping):
    def __init__(self, value: dict):
        self._map: Mapping[str, DataTag] = {}
        for k, v in value.items():
            self[k] = v

    # @implements MutableMapping
    def __setitem__(self, k, v):
        self._map.__setitem__(k, data_taggify(v))

    # @implements MutableMapping
    def __getitem__(self, k):
        return self._map.__getitem__(k)

    # @implements MutableMapping
    def __delitem__(self, v):
        self._map.__delitem__(v)

    # @implements MutableMapping
    def __len__(self):
        return self._map.__len__()

    # @implements MutableMapping
    def __iter__(self):
        return self._map.__iter__()

    # @implements CommandToken
    def command_stringify(self) -> str:
        innards = ", ".join(f"{k}: {v.command_stringify()}" for k, v in self._map.items())
        return f"{{{innards}}}"


class ListDataTag(MutableSequence):
    def __init__(self, value: list):
        self._items: List[DataTag] = []
        for item in value:
            self.append(item)

    # @implements MutableSequence
    def __setitem__(self, k, v):
        self._items.__setitem__(k, data_taggify(v))

    # @implements MutableSequence
    def __getitem__(self, k):
        return self._items.__getitem__(k)

    # @implements MutableSequence
    def __delitem__(self, v):
        self._items.__delitem__(v)

    # @implements MutableSequence
    def __len__(self):
        return self._items.__len__()

    # @implements MutableSequence
    def insert(self, k, v):
        self._items.insert(k, data_taggify(v))

    # @implements CommandToken
    def command_stringify(self) -> str:
        innards = ", ".join(v.command_stringify() for v in self._items)
        return f"[{innards}]"


class StringDataTag(DataTag):
    def __init__(self, value: str):
        self._value: str = str(value)

    # @implements CommandToken
    def command_stringify(self) -> str:
        return f"{self._value!r}"


class ByteDataTag(DataTag):
    def __init__(self, value: int):
        self._value: int = int(value)

    # @implements CommandToken
    def command_stringify(self) -> str:
        return f"{self._value}b"


class ShortDataTag(DataTag):
    def __init__(self, value: int):
        self._value: int = int(value)

    # @implements CommandToken
    def command_stringify(self) -> str:
        return f"{self._value}s"


class IntDataTag(DataTag):
    def __init__(self, value: int):
        self._value: int = int(value)

    # @implements CommandToken
    def command_stringify(self) -> str:
        return f"{self._value}"


class LongDataTag(DataTag):
    def __init__(self, value: int):
        self._value: int = int(value)

    # @implements CommandToken
    def command_stringify(self) -> str:
        return f"{self._value}l"


class FloatDataTag(DataTag):
    def __init__(self, value: float):
        self._value: float = float(value)

    # @implements CommandToken
    def command_stringify(self) -> str:
        return f"{self._value}f"


class DoubleDataTag(DataTag):
    def __init__(self, value: float):
        self._value: float = float(value)

    # @implements CommandToken
    def command_stringify(self) -> str:
        return f"{self._value}d"


def data_taggify(value: Any) -> DataTag:
    if isinstance(value, str):
        if (match := BYTE_PATTERN.match(value)) :
            return ByteDataTag(int(match.groups()[0]))
        return StringDataTag(value)
    if isinstance(value, int):
        return IntDataTag(value)
    if isinstance(value, float):
        return FloatDataTag(value)
    if isinstance(value, dict):
        return CompoundDataTag(value)
    if isinstance(value, list):
        return ListDataTag(value)
    raise ValueError(
        f"Cannot convert value of type {value.__class__.__name__} to data tag: {value}"
    )
