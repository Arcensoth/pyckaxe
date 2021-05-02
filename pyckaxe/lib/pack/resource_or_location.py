from dataclasses import dataclass
from typing import Generic, TypeVar, Union

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.resource_location import ClassifiedResourceLocation

__all__ = ("ResourceOrLocation",)


ResourceType = TypeVar("ResourceType", bound=Resource)


@dataclass
class ResourceOrLocation(Generic[ResourceType]):
    """ Contains a value that is either a `Resource` or a `ResourceLocation`. """

    value: Union[ResourceType, ClassifiedResourceLocation[ResourceType]]
