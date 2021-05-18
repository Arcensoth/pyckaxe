from typing import Coroutine, Protocol, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.physical_resource_location import PhysicalResourceLocation

__all__ = ("ResourceDumper",)


ResourceType = TypeVar("ResourceType", bound=Resource, contravariant=True)


class ResourceDumper(Protocol[ResourceType]):
    def __call__(
        self, resource: ResourceType, location: PhysicalResourceLocation
    ) -> Coroutine[None, None, None]:
        """Dump `resource` to `location`."""
