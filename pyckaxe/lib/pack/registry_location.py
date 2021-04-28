from dataclasses import dataclass, replace
from typing import Tuple, TypeVar

from pyckaxe.lib.pack.namespace import Namespace

__all__ = ("RegistryLocation",)


SelfType = TypeVar("SelfType", bound="RegistryLocation")


@dataclass
class RegistryLocation:
    """ A relative registry location, independent of any physical location. """

    namespace: Namespace
    parts: Tuple[str, ...]

    def __str__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name)

    def __truediv__(self: SelfType, other: str) -> SelfType:
        return self.extend(other)

    def extend(self: SelfType, *parts: str) -> SelfType:
        return replace(self, parts=(*self.parts, *parts))

    # DELETEME still used?
    # def resolve_path(self, pack_context: PackContext) -> Path:
    #     namespace_path = self.namespace.resolve_path(pack_context)
    #     return Path(namespace_path.joinpath(*self.parts))

    @property
    def name(self) -> str:
        parts_str = "/".join(self.parts)
        return f"{self.namespace}[{parts_str}]"
