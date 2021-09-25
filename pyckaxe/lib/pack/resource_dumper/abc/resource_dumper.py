from typing import Coroutine, Protocol, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.physical_resource_location import PhysicalResourceLocation

__all__ = ("ResourceDumper",)


RT = TypeVar("RT", bound=Resource, contravariant=True)


class ResourceDumper(Protocol[RT]):
    def __call__(
        self, resource: RT, location: PhysicalResourceLocation
    ) -> Coroutine[None, None, None]:
        """Dump `resource` to `location`."""
