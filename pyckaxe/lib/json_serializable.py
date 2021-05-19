from typing import Protocol, TypeVar

from pyckaxe.lib.types import JsonValue

__all__ = (
    "JsonSerializable",
    "JsonDeserializable",
)


SelfType = TypeVar("SelfType")


class JsonSerializable(Protocol):
    def serialize(self) -> JsonValue:
        ...


class JsonDeserializable(Protocol):
    @classmethod
    def deserialize(cls: SelfType, value: JsonValue) -> SelfType:
        ...
