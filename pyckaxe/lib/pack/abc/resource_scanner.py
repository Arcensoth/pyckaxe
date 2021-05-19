from typing import AsyncIterable, Protocol, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.resource_location import ClassifiedResourceLocation

__all__ = ("ResourceScanner",)


ResourceType = TypeVar("ResourceType", bound=Resource, covariant=True)


class ResourceScanner(Protocol[ResourceType]):
    def __call__(
        self, match: str = ...
    ) -> AsyncIterable[ClassifiedResourceLocation[ResourceType]]:
        """Scan for all of a certain type of matching resource."""
