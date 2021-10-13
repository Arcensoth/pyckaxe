from dataclasses import dataclass
from typing import AsyncIterable, Generic, Tuple, TypeVar

from pyckaxe.lib.pack.abc.resolution_context import ResolutionContext
from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.resource_link import ResourceLink

__all__ = ("ResourceCollection",)


RT = TypeVar("RT", bound=Resource)


@dataclass(frozen=True)
class ResourceCollection(Generic[RT]):
    """A collection of resources that can be resolved and iterated over on-demand."""

    _values: Tuple[ResourceLink[RT], ...]

    def __call__(self, ctx: ResolutionContext) -> AsyncIterable[RT]:
        """Resolve and iterate over the underlying resources."""
        return self._iterate(ctx)

    async def _iterate(self, ctx: ResolutionContext) -> AsyncIterable[RT]:
        for link in self._values:
            yield await link(ctx)
