from dataclasses import dataclass, field
from typing import AsyncIterable, Dict, Iterator, Tuple, Type, TypeVar, cast

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.physical_resource_location import PhysicalResourceLocation
from pyckaxe.lib.pack.resource_location import ResourceLocation
from pyckaxe.lib.pack.resource_resolver import ResourceResolver

__all__ = (
    "ResourceResolverError",
    "FailedToResolveResourceError",
    "NoResolverAvailableError",
    "WrongResourceResolvedError",
    "ResourceResolverSet",
)


ResourceType = TypeVar("ResourceType", bound=Resource)


class ResourceResolverError(Exception):
    pass


class FailedToResolveResourceError(ResourceResolverError):
    def __init__(self, location: ResourceLocation):
        super().__init__(f"Failed to resolve resource at: {location}")


class NoResolverAvailableError(ResourceResolverError):
    def __init__(self, resource_type: Type[Resource]):
        super().__init__(
            f"No resource resolver mapped for resource type {resource_type.__name__}"
        )


class WrongResourceResolvedError(ResourceResolverError):
    def __init__(
        self,
        resource_type: Type[Resource],
        resource: Resource,
    ):
        super().__init__(
            f"Expected to resolve resource type {resource_type.__name__}"
            f" but got {resource.__class__.__name__}"
        )


@dataclass
class ResourceResolverSet:
    """
    A group of `ResourceResolver`s for resolving several types of resources.

    This class helps manage inter-resource dependency by resolving and loading
    `ClassifiedResourceLocation`s into their respective `Resource`s using a
    configured set of `ResourceResolver`s.

    This class works similarly to `MutableMapping` but not identically.
    """

    _resolvers: Dict[Type[Resource], ResourceResolver[Resource]] = field(
        default_factory=dict
    )

    def __setitem__(
        self, key: Type[ResourceType], value: ResourceResolver[ResourceType]
    ):
        self._resolvers.__setitem__(key, value)

    def __getitem__(self, key: Type[ResourceType]) -> ResourceResolver[ResourceType]:
        for cls in key.mro():
            if resolver := self._resolvers.get(cls):
                return cast(ResourceResolver[ResourceType], resolver)
        raise NoResolverAvailableError(key)

    def __delitem__(self, key: Type[ResourceType]):
        self._resolvers.__delitem__(key)

    def __len__(self):
        return self._resolvers.__len__()

    def __iter__(self) -> Iterator[ResourceResolver[Resource]]:
        return self._resolvers.values().__iter__()

    async def resolve_resource(
        self, resource_type: Type[ResourceType], location: ResourceLocation
    ) -> ResourceType:
        """ Resolve `location` into a resource. """
        try:
            resolver = self[resource_type]
            resource = await resolver.resolve_resource(location)
            if isinstance(resource, resource_type):
                return resource
            raise WrongResourceResolvedError(resource_type, resource)
        except Exception as ex:
            raise FailedToResolveResourceError(location) from ex

    def scan(
        self,
        resource_type: Type[ResourceType],
        match: str = r"*",
    ) -> AsyncIterable[Tuple[ResourceType, PhysicalResourceLocation]]:
        """ Yield all matching (resource, location) pairs in the registry. """
        resolver = self[resource_type]
        return resolver.scan(match)
