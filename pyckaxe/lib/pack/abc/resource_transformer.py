from typing import AsyncIterable, Protocol, Tuple, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.resource_location import ResourceLocation
from pyckaxe.lib.pack.resource_processing_context import ResourceProcessingContext

__all__ = ("ResourceTransformer",)


RT = TypeVar("RT", bound=Resource)


class ResourceTransformer(Protocol[RT]):
    def __call__(
        self, ctx: ResourceProcessingContext[RT]
    ) -> AsyncIterable[Tuple[Resource, ResourceLocation]]:
        """Turn the input resource into any number of output resources."""
