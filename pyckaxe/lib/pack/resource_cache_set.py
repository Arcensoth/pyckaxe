from collections.abc import MutableMapping
from dataclasses import dataclass, field
from typing import Dict, Iterator, Optional, Type, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.abc.resource_cache import ResourceCache
from pyckaxe.lib.pack.resource_location import (
    ClassifiedResourceLocation,
    ResourceLocation,
)

__all__ = (
    "ResourceCacheError",
    "FailedToGetResourceError",
    "NoCacheAvailableError",
    "WrongResourceGotError",
    "ResourceCacheSet",
)


class ResourceCacheError(Exception):
    pass


class FailedToGetResourceError(ResourceCacheError):
    def __init__(self, location: ResourceLocation):
        super().__init__(f"Failed to get resource at: {location}")


class NoCacheAvailableError(ResourceCacheError):
    def __init__(self, resource_type: Type[Resource]):
        super().__init__(
            f"No resource cache mapped for resource type {resource_type.__name__}"
        )


class WrongResourceGotError(ResourceCacheError):
    def __init__(
        self,
        resource_type: Type[Resource],
        resource: Resource,
    ):
        super().__init__(
            f"Expected to get resource type {resource_type.__name__}"
            f" but got {resource.__class__.__name__}"
        )


RT = TypeVar("RT", bound=Resource)
RT_co = TypeVar("RT_co", bound=Resource, covariant=True)


@dataclass
class ResourceCacheSet(MutableMapping[Type[Resource], ResourceCache[RT_co]]):
    """
    Delegates a `ResourceCache` based on the type of `ClassifiedResourceLocation`.
    """

    _caches: Dict[Type[Resource], ResourceCache[RT_co]] = field(default_factory=dict)

    # @implements MutableMapping
    def __setitem__(self, key: Type[RT], value: ResourceCache[RT_co]):
        self._caches[key] = value

    # @implements MutableMapping
    def __getitem__(self, key: Type[RT]) -> ResourceCache[RT_co]:
        for cls in key.mro():
            if issubclass(cls, Resource):
                if (cache := self._caches.get(cls)) is not None:
                    return cache
        raise NoCacheAvailableError(key)

    # @implements MutableMapping
    def __delitem__(self, key: Type[RT]):
        del self._caches[key]

    # @implements MutableMapping
    def __len__(self):
        return len(self._caches)

    # @implements MutableMapping
    def __iter__(self) -> Iterator[Type[Resource]]:
        return iter(self._caches)

    def get(self, location: ClassifiedResourceLocation[RT]) -> Optional[RT]:
        """Get a `Resource` from a `ClassifiedResourceLocation` if cached."""
        resource_type = location.resource_class
        try:
            cache = self[resource_type]
            resource = cache.get(location)
            if (resource is None) or isinstance(resource, resource_type):
                return resource
            raise WrongResourceGotError(resource_type, resource)
        except Exception as ex:
            raise FailedToGetResourceError(location) from ex
