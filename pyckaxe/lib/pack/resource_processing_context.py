from dataclasses import dataclass
from typing import Any, Coroutine, Generic, Type, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.resource_location import (
    ClassifiedResourceLocation,
    ResourceLocation,
)
from pyckaxe.lib.pack.resource_resolver_set import ResourceResolverSet

__all__ = ("ResourceProcessingContext",)


ResourceType = TypeVar("ResourceType", bound=Resource)
ResolveResourceType = TypeVar("ResolveResourceType", bound=Resource)


@dataclass
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
        self, key: ClassifiedResourceLocation[ResolveResourceType]
    ) -> Coroutine[Any, Any, ResolveResourceType]:
        resource_class = key.resource_class
        location = ResourceLocation.declassify(key)
        return self.resolve_resource(resource_class, location)

    async def resolve_resource(
        self, resource_class: Type[ResolveResourceType], location: ResourceLocation
    ) -> ResolveResourceType:
        return await self.resolver_set.resolve_resource(resource_class, location)