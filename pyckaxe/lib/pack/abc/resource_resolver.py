from typing import Coroutine, Protocol, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.resource_location import ResourceLocation

__all__ = ("ResourceResolver",)


ResourceType = TypeVar("ResourceType", bound=Resource, covariant=True)


class ResourceResolver(Protocol[ResourceType]):
    def __call__(
        self, location: ResourceLocation
    ) -> Coroutine[None, None, ResourceType]:
        """Resolve a resource from a resource location."""
