from dataclasses import dataclass
from typing import Coroutine, Generic, TypeVar, Union

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.resource_location import (
    ClassifiedResourceLocation,
    ResourceLocation,
)
from pyckaxe.lib.pack.resource_resolver_set import ResourceResolverSet

__all__ = ("ResourceProcessingContext",)


ResourceType = TypeVar("ResourceType", bound=Resource)
ResolveResourceType = TypeVar("ResolveResourceType", bound=Resource)


@dataclass(frozen=True)
class ResourceProcessingContext(Generic[ResourceType]):
    """
    Contains information that can be used to process a resource in different ways.

    This class pairs a `Resource` with a `ResourceLocation` while carrying a reference
    to a `ResourceResolverSet`, which keeps it grounded to an absolute context and
    allows it to resolve and load other types of resources.

    Attributes
    ----------
    resolver_set
        Resolves and loads other types of resources by reference.
    resource
        The input resource that is being transformed.
    location
        The location of the resource being processed.
    """

    resolver_set: ResourceResolverSet
    resource: ResourceType
    location: ResourceLocation

    def __getitem__(
        self,
        key: Union[
            ClassifiedResourceLocation[ResolveResourceType],
            ResolveResourceType,
        ],
    ) -> Coroutine[None, None, ResolveResourceType]:
        if isinstance(key, ClassifiedResourceLocation):
            return self.resolve_resource(key)
        assert isinstance(key, Resource)
        return self.return_resource(key)

    async def return_resource(
        self, resource: ResolveResourceType
    ) -> ResolveResourceType:
        return resource

    async def resolve_resource(
        self, location: ClassifiedResourceLocation[ResolveResourceType]
    ) -> ResolveResourceType:
        return await self.resolver_set(location)
