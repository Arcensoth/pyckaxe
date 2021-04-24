from typing import Protocol, TypeVar

from pyckaxe.lib.nbt import NbtConvertible

__all__ = (
    "NbtSerializable",
    "NbtDeserializable",
)

SelfType = TypeVar("SelfType")


class NbtSerializable(Protocol):
    def to_nbt(self) -> NbtConvertible:
        ...


class NbtDeserializable(Protocol):
    @classmethod
    def from_nbt(cls: SelfType, value: NbtConvertible) -> SelfType:
        ...
