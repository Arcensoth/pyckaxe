from typing import Protocol

from pyckaxe.lib.pack.physical_resource_location import PhysicalResourceLocation
from pyckaxe.lib.pack.resource_location import ResourceLocation

__all__ = ("ResourceLocationResolver",)


class ResourceLocationResolver(Protocol):
    def __call__(self, location: ResourceLocation) -> PhysicalResourceLocation:
        """Resolve an absolute resource location from a relative one."""
