from typing import Any, Coroutine, Generic, Optional, Type, TypeVar

from pyckaxe.pack.pack_context import PackContext
from pyckaxe.pack.resource.abc.resource import Resource
from pyckaxe.pack.resource.abc.resource_location import ResourceLocation
from pyckaxe.utils.fields import DEFAULT, get_field

ResourceOrLocationType = TypeVar("ResourceOrLocationType", bound="ResourceOrLocation")
ResourceLocationType = TypeVar("ResourceLocationType", bound=ResourceLocation)
ResourceType = TypeVar("ResourceType", bound=Resource)


class ResourceOrLocation(Generic[ResourceType, ResourceLocationType]):
    class Meta:
        resource_class: Type[Resource] = Resource
        resource_location_class: Type[ResourceLocation] = ResourceLocation

    @classmethod
    async def from_field(
        cls: Type[ResourceOrLocationType], raw: dict, field: str, default=DEFAULT
    ) -> ResourceOrLocationType:
        # Extract the field from the raw data.
        raw_resource_or_location = get_field(raw, field, default=default)
        # A string is assumed to be a resource location.
        if isinstance(raw_resource_or_location, str):
            resource_location = cls.Meta.resource_location_class.from_string(
                raw_resource_or_location
            )
            resource_or_location = cls(resource_location=resource_location)
        # Anything else is assumed to be a serialized resource.
        else:
            resource = await cls.Meta.resource_class.deserialize(raw_resource_or_location)
            resource_or_location = cls(resource=resource)
        return resource_or_location

    def __init__(
        self,
        resource: Optional[ResourceType] = None,
        resource_location: Optional[ResourceLocationType] = None,
    ):
        # At least one of the values must be provided.
        assert (resource is not None) or (resource_location is not None)
        # Values must either be null or the correct type.
        if resource is not None:
            assert isinstance(resource, self.Meta.resource_class)
        if resource_location is not None:
            assert isinstance(resource_location, self.Meta.resource_location_class)
        # Remember these values, internally, and resolve them on-demand.
        self.resource: Optional[ResourceType] = resource
        self.resource_location: Optional[ResourceLocationType] = resource_location

    def __call__(self, pack_context: PackContext) -> Coroutine[Any, Any, ResourceType]:
        """
        Mimics the call resolution of `ResourceLocation` so that `ResourceOrLocation` can be used
        in the same way.
        """
        return self.resolve_resource(pack_context)

    async def resolve_resource(self, pack_context: PackContext) -> ResourceType:
        """
        Returns the contained `ResourceType`, if available. Otherwise, resolves the contained
        `ResourceLocationType` into a `ResourceType` and returns that.
        """
        # If we already have a `Resource`, just return that.
        if self.resource is not None:
            return self.resource
        # Otherwise we must have a `ResourceLocation` that needs to be resolved.
        resource = await self.resource_location.resolve_resource(pack_context)
        return resource
