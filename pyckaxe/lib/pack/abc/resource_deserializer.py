from typing import Protocol, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource

__all__ = ("ResourceDeserializer",)


ResourceType = TypeVar("ResourceType", bound=Resource, covariant=True)
RawType = TypeVar("RawType", contravariant=True)


class ResourceDeserializer(Protocol[ResourceType, RawType]):
    def __call__(self, raw: RawType) -> ResourceType:
        """Return a `Resource` created from the given `raw` data."""
