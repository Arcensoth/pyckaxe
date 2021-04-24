from dataclasses import dataclass, replace
from typing import Any, Generic, Tuple, Type, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.namespace import Namespace

__all__ = (
    "ClassifiedResourceLocation",
    "ResourceLocation",
)


SelfType = TypeVar("SelfType", bound="_ResourceLocationBase")


@dataclass
class _ResourceLocationBase:
    namespace: Namespace
    parts: Tuple[str, ...]

    @classmethod
    def from_string(cls: Type[SelfType], name: str) -> SelfType:
        namespace = Namespace(name.split(":")[0])
        parts: Tuple[str, ...] = tuple(name.split(":")[1].split("/"))
        return cls(namespace=namespace, parts=parts)

    def __str__(self) -> str:
        return self.name

    def __hash__(self) -> int:
        return hash(self.name)

    def extend(self: SelfType, *parts: str) -> SelfType:
        return replace(self, parts=(*self.parts, *parts))

    @property
    def trail(self) -> str:
        return "/".join(self.parts)

    @property
    def name(self) -> str:
        return f"{self.namespace}:{self.trail}"


ResourceType = TypeVar("ResourceType", bound=Resource)


@dataclass
class ClassifiedResourceLocation(_ResourceLocationBase, Generic[ResourceType]):
    """
    A resource location that is aware of the type of underlying resource.
    """

    resource_class: Type[ResourceType]


@dataclass
class ResourceLocation(_ResourceLocationBase):
    """ A relative resource location, independent of any physical location. """

    @classmethod
    def declassify(
        cls, classified: ClassifiedResourceLocation[Any]
    ) -> "ResourceLocation":
        return cls(classified.namespace, classified.parts)

    def __rmatmul__(
        self, other: Type[ResourceType]
    ) -> ClassifiedResourceLocation[ResourceType]:
        return self.classify(other)

    def classify(
        self, resource_class: Type[ResourceType]
    ) -> ClassifiedResourceLocation[ResourceType]:
        return ClassifiedResourceLocation(self.namespace, self.parts, resource_class)
