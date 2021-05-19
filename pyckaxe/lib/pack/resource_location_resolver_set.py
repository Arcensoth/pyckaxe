from dataclasses import dataclass, field
from typing import Dict, Iterator, Type

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.abc.resource_location_resolver import ResourceLocationResolver
from pyckaxe.lib.pack.physical_resource_location import PhysicalResourceLocation
from pyckaxe.lib.pack.resource_location import (
    ClassifiedResourceLocation,
    ResourceLocation,
)

__all__ = (
    "ResourceLocationResolverError",
    "FailedToResolveResourceLocationError",
    "NoLocationResolverAvailableError",
    "ResourceLocationResolverSet",
)


class ResourceLocationResolverError(Exception):
    pass


class FailedToResolveResourceLocationError(ResourceLocationResolverError):
    def __init__(self, location: ResourceLocation):
        super().__init__(f"Failed to resolve resource location at: {location}")


class NoLocationResolverAvailableError(ResourceLocationResolverError):
    def __init__(self, resource_type: Type[Resource]):
        super().__init__(
            f"No resource location resolver mapped for resource type {resource_type.__name__}"
        )


@dataclass
class ResourceLocationResolverSet:
    """Resolves different types of absolute resource locations from relative ones."""

    _location_resolvers: Dict[Type[Resource], ResourceLocationResolver] = field(
        default_factory=dict
    )

    def __setitem__(self, key: Type[Resource], value: ResourceLocationResolver):
        self._location_resolvers.__setitem__(key, value)

    def __getitem__(self, key: Type[Resource]) -> ResourceLocationResolver:
        for cls in key.mro():
            if resolver := self._location_resolvers.get(cls):
                return resolver
        raise NoLocationResolverAvailableError(key)

    def __delitem__(self, key: Type[Resource]):
        self._location_resolvers.__delitem__(key)

    def __len__(self):
        return self._location_resolvers.__len__()

    def __iter__(self) -> Iterator[ResourceLocationResolver]:
        return self._location_resolvers.values().__iter__()

    def __call__(
        self, location: ClassifiedResourceLocation[Resource]
    ) -> PhysicalResourceLocation:
        return self.resolve(location)

    def resolve(
        self, location: ClassifiedResourceLocation[Resource]
    ) -> PhysicalResourceLocation:
        """Resolve an absolute resource location from a relative one."""
        resource_type = location.resource_class
        try:
            resolver = self[resource_type]
            return resolver(location)
        except Exception as ex:
            raise FailedToResolveResourceLocationError(location) from ex
