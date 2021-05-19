from typing import Protocol, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.resource_location import ResourceLocation
from pyckaxe.utils import LRUCache, StaticCache, UnboundedCache
from pyckaxe.utils.cache.abc.cache import Cache

__all__ = (
    "ResourceCache",
    "UnboundedResourceCache",
    "StaticResourceCache",
    "LRUResourceCache",
)


ResourceType = TypeVar("ResourceType", bound=Resource)


class ResourceCache(Cache[ResourceLocation, ResourceType], Protocol[ResourceType]):
    """An in-memory cache of resources to reduce the number of loads."""


# @implements ResourceCache
class UnboundedResourceCache(UnboundedCache[ResourceLocation, ResourceType]):
    pass


# @implements ResourceCache
class StaticResourceCache(StaticCache[ResourceLocation, ResourceType]):
    pass


# @implements ResourceCache
class LRUResourceCache(LRUCache[ResourceLocation, ResourceType]):
    pass
