from dataclasses import dataclass

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.physical_pack import PhysicalPack
from pyckaxe.lib.pack.resource_dumper_set import ResourceDumperSet
from pyckaxe.lib.pack.resource_location import ResourceLocation
from pyckaxe.lib.pack.resource_location_resolver_set import ResourceLocationResolverSet

__all__ = ("WritablePack",)


@dataclass
class WritablePack(PhysicalPack):
    """
    A pack that has a physical, writable directory associated with it.

    Attributes
    ----------
    location_resolvers
        Resolves different types of absolute resource locations from relative ones.
    dumpers
        Delegates to a different `ResourceDumper` based on the type of `Resource`.
    """

    location_resolvers: ResourceLocationResolverSet
    dumpers: ResourceDumperSet

    async def dump(self, resource: Resource, location: ResourceLocation):
        resource_type = type(resource)
        classified_location = resource_type @ location
        physical_location = self.location_resolvers(classified_location)
        await self.dumpers(resource, physical_location)
