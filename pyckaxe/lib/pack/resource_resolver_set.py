from collections.abc import MutableMapping
from dataclasses import dataclass, field
from typing import Coroutine, Dict, Iterator, Type, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.abc.resource_resolver import ResourceResolver
from pyckaxe.lib.pack.resource_location import (
    ClassifiedResourceLocation,
    ResourceLocation,
)

__all__ = (
    "ResourceResolverError",
    "FailedToResolveResourceError",
    "NoResolverAvailableError",
    "WrongResourceResolvedError",
    "ResourceResolverSet",
)


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


RT = TypeVar("RT", bound=Resource)
RT_co = TypeVar("RT_co", bound=Resource, covariant=True)


@dataclass
class ResourceResolverSet(MutableMapping[Type[Resource], ResourceResolver[RT_co]]):
    """
    Delegates a `ResourceResolver` based on the type of `ClassifiedResourceLocation`.

    This class helps manage inter-resource dependency by resolving and loading
    `ClassifiedResourceLocation`s into their respective `Resource`s using a
    configured set of `ResourceResolver`s.
    """

    _resolvers: Dict[Type[Resource], ResourceResolver[RT_co]] = field(
        default_factory=dict
    )

    # @implements MutableMapping
    def __setitem__(self, key: Type[RT], value: ResourceResolver[RT_co]):
        self._resolvers[key] = value

    # @implements MutableMapping
    def __getitem__(self, key: Type[RT]) -> ResourceResolver[RT_co]:
        for cls in key.mro():
            if issubclass(cls, Resource):
                if (resolver := self._resolvers.get(cls)) is not None:
                    return resolver
        raise NoResolverAvailableError(key)

    # @implements MutableMapping
    def __delitem__(self, key: Type[RT]):
        del self._resolvers[key]

    # @implements MutableMapping
    def __len__(self):
        return len(self._resolvers)

    # @implements MutableMapping
    def __iter__(self) -> Iterator[Type[Resource]]:
        return iter(self._resolvers)

    def __call__(
        self, location: ClassifiedResourceLocation[RT_co]
    ) -> Coroutine[None, None, Resource]:
        return self.resolve(location)

    async def resolve(self, location: ClassifiedResourceLocation[RT_co]) -> RT_co:
        """Resolve a `Resource` from a `ClassifiedResourceLocation`."""
        resource_type = location.resource_class
        try:
            resolver = self[resource_type]
            resource = await resolver(location)
            if isinstance(resource, resource_type):
                return resource
            raise WrongResourceResolvedError(resource_type, resource)
        except Exception as ex:
            raise FailedToResolveResourceError(location) from ex
