from dataclasses import dataclass
from typing import Generic, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.resource_location import ResourceLocation

__all__ = ("LocatedResource",)


ResourceType = TypeVar("ResourceType", bound=Resource)


@dataclass
class LocatedResource(Generic[ResourceType]):
    """ Pairs a `Resource` with a `ResourceLocation`. """

    resource: ResourceType
    location: ResourceLocation
