from dataclasses import dataclass, field
from typing import AsyncIterable, Dict, Tuple, Type, TypeVar, cast

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
    """ A group of `ResourceResolver`s for resolving several types of resources. """

    resolvers: Dict[Type[Resource], ResourceResolver[Resource]] = field(
        default_factory=dict
    )

    def get_resolver_or_error(
        self, resource_type: Type[ResourceType]
    ) -> ResourceResolver[ResourceType]:
        resolver = self.resolvers.get(resource_type)
        if resolver is not None:
            # NOTE Apparently isinstance isn't good enough for the type-checker?
            resolver = cast(ResourceResolver[ResourceType], resolver)
            return resolver
        raise NoResolverAvailableError(resource_type)

    async def resolve_resource(
        self, resource_type: Type[ResourceType], location: ResourceLocation
    ) -> ResourceType:
        """ Resolve `location` into a resource. """
        try:
            resolver = self.get_resolver_or_error(resource_type)
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
        resolver = self.get_resolver_or_error(resource_type)
        return resolver.scan(match)
