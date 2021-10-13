from dataclasses import dataclass
from typing import Coroutine, Generic, TypeVar, Union

from pyckaxe.lib.pack.abc.resolution_context import ResolutionContext
from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.resource_location import ClassifiedResourceLocation

__all__ = ("ResourceLink",)


RT = TypeVar("RT", bound=Resource)


# @implements ResourceResolvable[RT]
@dataclass(frozen=True)
class ResourceLink(Generic[RT]):
    """
    A reference to a resource that can be resolved on-demand.

    This is an abstraction that internally contains either:
    1. a resource location that can be used to resolve the resource; or
    2. a direct, in-memory representation of the resource.
    """

    _value: Union[ClassifiedResourceLocation[RT], RT]

    # @implements ResourceResolvable
    def __call__(self, ctx: ResolutionContext) -> Coroutine[None, None, RT]:
        """
        Resolve the underlying resource.

        If the value is a `ClassifiedResourceLocation`, it first needs to be resolved.

        If the value is itself a `Resource`, it can be immediately returned. Note that
        this variation exists to support inline resources using the same interface.
        """
        if isinstance(self._value, ClassifiedResourceLocation):
            return ctx(self._value)
        return self._return_resource(self._value)

    async def _return_resource(self, resource: RT) -> RT:
        return resource
