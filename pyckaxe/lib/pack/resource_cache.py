from typing import TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.resource_location import ResourceLocation
from pyckaxe.utils.lru_cache import LRUCache

__all__ = ("ResourceCache",)


ResourceType = TypeVar("ResourceType", bound=Resource)


class ResourceCache(LRUCache[ResourceLocation, ResourceType]):
    pass
