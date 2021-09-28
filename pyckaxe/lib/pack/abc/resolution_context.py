from typing import Coroutine, Protocol, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.resource_location import ClassifiedResourceLocation

__all__ = ("ResolutionContext",)


RT = TypeVar("RT", bound=Resource)


class ResolutionContext(Protocol):
    """Minimal interface supporting resource resolution."""

    def __call__(
        self, location: ClassifiedResourceLocation[RT]
    ) -> Coroutine[None, None, RT]:
        """Resolve and return a `Resource` from `location`."""
