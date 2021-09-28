from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Any, Generic, Tuple, Type, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.namespace import Namespace

__all__ = (
    "InvalidResourceLocation",
    "ResourceLocation",
    "ClassifiedResourceLocation",
)


ST = TypeVar("ST", bound="ResourceLocation")
RT = TypeVar("RT", bound=Resource)


class InvalidResourceLocation(Exception):
    def __init__(self, value: str):
        super().__init__(f"Invalid resource location: {value}")


@dataclass(frozen=True)
class ResourceLocation:
    """A relative resource location, independent of any physical location."""

    namespace: Namespace
    parts: Tuple[str, ...]

    @classmethod
    def from_string(cls: Type[ST], name: str) -> ST:
        try:
            namespace_str, _, parts_str = name.partition(":")
            namespace = Namespace(namespace_str)
            parts = tuple(parts_str.split("/"))
            return cls(namespace=namespace, parts=parts)
        except Exception as ex:
            raise InvalidResourceLocation(name) from ex

    @classmethod
    def declassify(
        cls, classified: ClassifiedResourceLocation[Any]
    ) -> "ResourceLocation":
        return cls(classified.namespace, classified.parts)

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return str(self)

    def __truediv__(self: ST, other: str) -> ST:
        return self.extend(other)

    def __rmatmul__(self, other: Type[RT]) -> ClassifiedResourceLocation[RT]:
        return self.classify(other)

    @property
    def trail(self) -> str:
        return "/".join(self.parts)

    @property
    def name(self) -> str:
        return f"{self.namespace}:{self.trail}"

    def extend(self: ST, *parts: str) -> ST:
        return replace(self, parts=(*self.parts, *parts))

    def classify(self, resource_class: Type[RT]) -> ClassifiedResourceLocation[RT]:
        return ClassifiedResourceLocation(self.namespace, self.parts, resource_class)


@dataclass(frozen=True)
class ClassifiedResourceLocation(ResourceLocation, Generic[RT]):
    """
    A resource location that is aware of the type of underlying resource.
    """

    resource_class: Type[RT]
