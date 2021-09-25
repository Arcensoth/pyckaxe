from typing import Coroutine, Protocol, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.resource_location import ResourceLocation

__all__ = ("ResourceResolver",)


RT_co = TypeVar("RT_co", bound=Resource, covariant=True)


class ResourceResolver(Protocol[RT_co]):
    def __call__(self, location: ResourceLocation) -> Coroutine[None, None, RT_co]:
        """Resolve a resource from a resource location."""
