from dataclasses import dataclass
from typing import Any, Coroutine, Generic, Type, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.resource_location import (
    ClassifiedResourceLocation,
    ResourceLocation,
)
from pyckaxe.lib.pack.resource_resolver_set import ResourceResolverSet

__all__ = ("ResourceBuildContext",)


ResourceType = TypeVar("ResourceType", bound=Resource)
OptionsType = TypeVar("OptionsType")

ResolveResourceType = TypeVar("ResolveResourceType", bound=Resource)


@dataclass
class ResourceBuildContext(Generic[ResourceType, OptionsType]):
    """
    Contains information used to build a `Resource` in a particular way.

    Attributes
    ----------
    resolver_set
        Resolves and loads other types of resources.
    options
        Arbitrary build options.
    resource
        The resource being processed.
    location
        The location of the resource being processed.
    """

    resolver_set: ResourceResolverSet
    options: OptionsType
    resource: ResourceType
    location: ResourceLocation

    # DELETEME is this used anywhere?
    # inline_index: Optional[int] = None

    # DELETEME is this used anywhere?
    # @property
    # def is_inline(self) -> bool:
    #     return self.inline_index is not None

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
