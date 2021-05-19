from dataclasses import dataclass, replace
from typing import Tuple, TypeVar

from pyckaxe.lib.pack.namespace import Namespace

__all__ = ("RegistryLocation",)


SelfType = TypeVar("SelfType", bound="RegistryLocation")


@dataclass(frozen=True)
class RegistryLocation:
    """A relative registry location, independent of any physical location."""

    namespace: Namespace
    parts: Tuple[str, ...]

    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return str(self)

    def __truediv__(self: SelfType, other: str) -> SelfType:
        return self.extend(other)

    def extend(self: SelfType, *parts: str) -> SelfType:
        return replace(self, parts=(*self.parts, *parts))

    @property
    def name(self) -> str:
        parts_str = "/".join(self.parts)
        return f"{self.namespace}[{parts_str}]"
