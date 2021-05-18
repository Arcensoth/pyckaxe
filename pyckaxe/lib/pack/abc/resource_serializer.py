from typing import Protocol, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource

__all__ = ("ResourceSerializer",)


ResourceType = TypeVar("ResourceType", bound=Resource, contravariant=True)
RawType = TypeVar("RawType", covariant=True)


class ResourceSerializer(Protocol[ResourceType, RawType]):
    def __call__(self, resource: ResourceType) -> RawType:
        """Return the raw data representation of `resource`."""
