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


RT = TypeVar("RT", bound=Resource)


class ResourceCache(Cache[ResourceLocation, RT], Protocol[RT]):
    """An in-memory cache of resources to reduce the number of loads."""


# @implements ResourceCache
class UnboundedResourceCache(UnboundedCache[ResourceLocation, RT]):
    pass


# @implements ResourceCache
class StaticResourceCache(StaticCache[ResourceLocation, RT]):
    pass


# @implements ResourceCache
class LRUResourceCache(LRUCache[ResourceLocation, RT]):
    pass
