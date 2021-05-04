from dataclasses import dataclass, field
from typing import Dict, Generic, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.abc.resource_resolver import ResourceResolver
from pyckaxe.lib.pack.resource_location import ResourceLocation
from pyckaxe.lib.pack.resource_or_location import ResourceOrLocation

__all__ = ("ResourceCache",)


ResourceType = TypeVar("ResourceType", bound=Resource)


@dataclass
class ResourceCache(Generic[ResourceType]):
    """
    Caches resources to help reduce the amount of hits.

    Attributes
    ----------
    resolver_set
        Resolves and loads other types of resources by reference.
    _cache
        The internal cache, mapping resource locations to resources.
    """

    resolver: ResourceResolver[ResourceType]

    # TODO Implement configurable cache size. #enhance
    _cache: Dict[ResourceLocation, ResourceType] = field(
        init=False, default_factory=dict
    )

    async def get(self, res_or_loc: ResourceOrLocation[ResourceType]) -> ResourceType:
        """
        Resolve and cache a resource for future use.

        If `res_or_loc` is an inline `Resource`, return it directly. Otherwise, it must
        be a `ResourceLocation` in which case we check whether it is already in our
        cache. If not, resolve and cache it before returning it.
        """
        if isinstance(res_or_loc.value, Resource):
            return res_or_loc.value
        assert isinstance(res_or_loc.value, ResourceLocation)
        location = res_or_loc.value
        resource = self._cache.get(location)
        if resource is None:
            resource = await self.resolver(location)
            self._cache[location] = resource
        return resource
