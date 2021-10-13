from dataclasses import dataclass
from typing import Any, Coroutine, Generic, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.resource_location import (
    ClassifiedResourceLocation,
    ResourceLocation,
)
from pyckaxe.lib.pack.resource_resolver_set import ResourceResolverSet

__all__ = ("ResourceProcessingContext",)


PT = TypeVar("PT", bound=Resource)
RT = TypeVar("RT", bound=Resource)


# @implements ResolutionContext
@dataclass(frozen=True)
class ResourceProcessingContext(Generic[PT]):
    """
    Contains information that can be used to process a resource in different ways.

    This class pairs a `Resource` with a `ResourceLocation` while carrying a reference
    to a `ResourceResolverSet`, which keeps it grounded to an absolute context and
    allows it to resolve other resources.

    Attributes
    ----------
    resolver_set
        Resolves and loads other resources.
    resource
        The resource being processed.
    location
        The location of the resource being processed.
    meta
        Optional, arbitrary metadata attached to the context.
    """

    resolver_set: ResourceResolverSet
    resource: PT
    location: ResourceLocation

    meta: Any = None

    # @implements ResolutionContext
    def __call__(
        self, location: ClassifiedResourceLocation[RT]
    ) -> Coroutine[None, None, RT]:
        """Resolve and return a `Resource` from `location`."""
        return self.resolver_set(location)
