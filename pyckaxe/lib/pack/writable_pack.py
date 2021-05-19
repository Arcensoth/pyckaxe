from dataclasses import dataclass
from pathlib import Path

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.physical_pack import PhysicalPack
from pyckaxe.lib.pack.physical_resource_location import PhysicalResourceLocation
from pyckaxe.lib.pack.resource_dumper_set import ResourceDumperSet
from pyckaxe.lib.pack.resource_location import ResourceLocation
from pyckaxe.lib.pack.resource_location_resolver_set import ResourceLocationResolverSet

__all__ = (
    "RogueResource",
    "WritablePack",
)


class RogueResource(Exception):
    def __init__(
        self,
        pack_path: Path,
        physical_location: PhysicalResourceLocation,
        resource: Resource,
    ):
        self.pack_oath: Path = pack_path
        self.physical_location: PhysicalResourceLocation = physical_location
        self.resource: Resource = resource
        super().__init__(
            f"Attempted to dump a resource to `{physical_location.path}`,"
            + f" which is outside of the pack at `{pack_path}`"
        )


@dataclass
class WritablePack(PhysicalPack):
    """
    A pack that has a physical, writable directory associated with it.

    Attributes
    ----------
    path
        The path to the root of the pack.
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
        if self.path not in physical_location.path.parents:
            raise RogueResource(self.path, physical_location, resource)
        await self.dumpers(resource, physical_location)
