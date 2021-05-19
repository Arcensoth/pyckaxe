from dataclasses import dataclass
from typing import Coroutine, Generic, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.abc.resource_location_resolver import ResourceLocationResolver
from pyckaxe.lib.pack.physical_resource_location import PhysicalResourceLocation
from pyckaxe.lib.pack.resource_cache import ResourceCache
from pyckaxe.lib.pack.resource_loader.abc.resource_loader import ResourceLoader
from pyckaxe.lib.pack.resource_location import ResourceLocation

__all__ = ("CommonResourceResolver",)


ResourceType = TypeVar("ResourceType", bound=Resource)


# @implements ResourceResolver
@dataclass
class CommonResourceResolver(Generic[ResourceType]):
    """
    Resolves and loads a resource from a resource location.

    This class uses `location_resolver` to resolve absolute resource locations from
    relative ones, and uses `loader` to load resources from the resolved locations. If a
    cache is present and already contains the resource, it bypasses `loader` and returns
    the cached resource directly.

    Attributes
    ----------
    location_resolver
        Resolves absolute resource locations from relative ones.
    loader
        Loads and returns a resource, given an absolute resource location.
    cache
        An in-memory cache of resources to reduce the number of loads.
    """

    location_resolver: ResourceLocationResolver
    loader: ResourceLoader[ResourceType]
    cache: ResourceCache[ResourceType]

    # @implements ResourceResolver
    def __call__(
        self, location: ResourceLocation
    ) -> Coroutine[None, None, ResourceType]:
        return self.resolve(location)

    async def _reload_resource(
        self, location: PhysicalResourceLocation
    ) -> ResourceType:
        """Load a resource regardless of the state of the cache."""
        # Load the resource.
        resource = await self.loader(location)
        # Add the newly-loaded resource to the cache.
        self.cache[location] = resource
        # Return the newly-loaded resource.
        return resource

    async def resolve(self, location: ResourceLocation) -> ResourceType:
        """Resolve `location` into a resource."""
        # Resolve the (possibly relative) resource location into an absolute one.
        physical_location = self.location_resolver(location)
        # If this resource is already cached, return it.
        if (cached := self.cache.get(physical_location)) is not None:
            return cached
        # Otherwise, reload the resource.
        return await self._reload_resource(physical_location)
