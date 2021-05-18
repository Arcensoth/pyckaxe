from dataclasses import dataclass
from typing import Generic, TypeVar

from pyckaxe.pack.resource.abc.resource import Resource
from pyckaxe.pack.resource.abc.resource_location import ResourceLocation

ResourceType = TypeVar("ResourceType", bound=Resource)
ResourceLocationType = TypeVar("ResourceLocationType", bound=ResourceLocation)


@dataclass
class LocatedResource(Generic[ResourceType, ResourceLocationType]):
    """Simply pairs a [Resource] with a [ResourceLocation]."""

    resource: ResourceType
    location: ResourceLocationType
