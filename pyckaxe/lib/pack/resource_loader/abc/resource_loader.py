from typing import Coroutine, Protocol, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.physical_resource_location import PhysicalResourceLocation

__all__ = ("ResourceLoader",)


ResourceType = TypeVar("ResourceType", bound=Resource, covariant=True)


class ResourceLoader(Protocol[ResourceType]):
    def __call__(
        self, location: PhysicalResourceLocation
    ) -> Coroutine[None, None, ResourceType]:
        """Load a `Resource` from `location`."""
