from dataclasses import dataclass
from pathlib import Path
from typing import Any, Coroutine, Generic, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.physical_namespace import PhysicalNamespace
from pyckaxe.lib.pack.physical_registry_location import PhysicalRegistryLocation
from pyckaxe.lib.pack.physical_resource_location import PhysicalResourceLocation
from pyckaxe.lib.pack.resource_loader.abc.resource_loader import ResourceLoader
from pyckaxe.lib.pack.resource_location import ResourceLocation

__all__ = ("CommonResourceResolver",)


ResourceType = TypeVar("ResourceType", bound=Resource)


# @implements ResourceResolver
@dataclass
class CommonResourceResolver(Generic[ResourceType]):
    """
    Resolves and loads a resource from a resource location.

    This class is responsible for resolving a resource location (`ResourceLocation`)
    into absolute form (`PhysicalResourceLocation`) using the absolute registry location
    `registry_location`.

    Once the absolute resource location is attained, this class simply invokes the
    resource loader `loader` to load and return a resource from it.

    Attributes
    ----------
    registry_location
        An absolute registry location used to resolve relative resource locations into
        absolute form.
    loader
        Loads and returns a resource, given an absolute resource location.
    """

    registry_location: PhysicalRegistryLocation
    loader: ResourceLoader[ResourceType]

    # @implements ResourceResolver
    def __call__(self, location: ResourceLocation) -> Coroutine[ResourceType, Any, Any]:
        return self.resolve_resource(location)

    @property
    def namespace(self) -> PhysicalNamespace:
        return self.registry_location.namespace

    @property
    def path(self) -> Path:
        return self.registry_location.path

    def resolve_location(self, location: ResourceLocation) -> PhysicalResourceLocation:
        """ Resolve `location` into absolute form. """
        if isinstance(location, PhysicalResourceLocation):
            return location
        physical_location = PhysicalResourceLocation(
            namespace=self.registry_location.namespace,
            parts=location.parts,
            registry_location=self.registry_location,
        )
        return physical_location

    async def resolve_resource(self, location: ResourceLocation) -> ResourceType:
        """ Resolve `location` into a resource. """
        physical_location = self.resolve_location(location)
        resource = await self.loader(physical_location)
        return resource
