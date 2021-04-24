from dataclasses import dataclass
from typing import TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.located_resource import LocatedResource
from pyckaxe.lib.pack.physical_resource_location import PhysicalResourceLocation

__all__ = ("PhysicallyLocatedResource",)


ResourceType = TypeVar("ResourceType", bound=Resource)


@dataclass
class PhysicallyLocatedResource(LocatedResource[ResourceType]):
    """ Pairs a `Resource` with a `PhysicalResourceLocation`. """

    location: PhysicalResourceLocation
