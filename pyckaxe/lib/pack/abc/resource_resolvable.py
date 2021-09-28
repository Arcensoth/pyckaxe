from typing import Coroutine, Protocol, TypeVar

from pyckaxe.lib.pack.abc.resolution_context import ResolutionContext
from pyckaxe.lib.pack.abc.resource import Resource

__all__ = ("ResourceResolvable",)


RT = TypeVar("RT", bound=Resource, covariant=True)


class ResourceResolvable(Protocol[RT]):
    """Something that can be resolved into a resource."""

    def __call__(self, ctx: ResolutionContext) -> Coroutine[None, None, RT]:
        """Resolve and return a `Resource` using `ctx`."""
