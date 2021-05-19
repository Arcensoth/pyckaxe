from typing import Coroutine, Protocol, TypeVar, Union

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.resource_location import ClassifiedResourceLocation

__all__ = ("ResolutionContext",)


ResourceType = TypeVar("ResourceType", bound=Resource)


class ResolutionContext(Protocol):
    """Minimal interface supporting resource resolution."""

    def __getitem__(
        self, key: Union[ClassifiedResourceLocation[ResourceType], ResourceType]
    ) -> Coroutine[None, None, ResourceType]:
        """
        Resolve and return a `Resource` from `key`.

        If `key` is a `ClassifiedResourceLocation`, it first needs to be resolved.

        If `key` is itself a `Resource`, it can be immediately returned. Note that this
        variation exists to support inline resources using the same interface.
        """
