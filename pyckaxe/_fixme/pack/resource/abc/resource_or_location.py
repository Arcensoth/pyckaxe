from typing import Any, Coroutine, Generic, Iterable, List, Optional, Type, TypeVar

from pyckaxe.pack.pack_context import PackContext
from pyckaxe.pack.resource.abc.located_resource import LocatedResource
from pyckaxe.pack.resource.abc.resource import Resource
from pyckaxe.pack.resource.abc.resource_location import ResourceLocation
from pyckaxe.utils.fields import DEFAULT, get_field

ResourceOrLocationType = TypeVar(
    "ResourceOrLocationType", bound="ResourceOrLocation[Any, Any]"
)
ResourceLocationType = TypeVar("ResourceLocationType", bound=ResourceLocation[Any])
ResourceType = TypeVar("ResourceType", bound=Resource[Any])


class ResourceOrLocation(Generic[ResourceType, ResourceLocationType]):
    resource_class: Type[Resource[Any]] = Resource
    resource_location_class: Type[ResourceLocation[Any]] = ResourceLocation

    @classmethod
    async def deserialize_resource_location(
        cls: Type[ResourceOrLocationType], raw: str
    ) -> ResourceOrLocationType:
        resource_location = cls.resource_location_class.from_string(raw)
        resource_or_location = cls(resource_location=resource_location)
        return resource_or_location

    @classmethod
    async def deserialize_resource(
        cls: Type[ResourceOrLocationType], raw: Any
    ) -> ResourceOrLocationType:
        resource = await cls.resource_class.deserialize(raw)
        resource_or_location = cls(resource=resource)
        return resource_or_location

    @classmethod
    async def deserialize(
        cls: Type[ResourceOrLocationType], raw: Any
    ) -> ResourceOrLocationType:
        # A string is assumed to be a resource location.
        if isinstance(raw, str):
            return await cls.deserialize_resource_location(raw)
        # Anything else is assumed to be a serialized resource.
        return await cls.deserialize_resource(raw)

    @classmethod
    async def deserialize_many(
        cls: Type[ResourceOrLocationType], raw: Iterable[Any]
    ) -> List[ResourceOrLocationType]:
        return [await cls.des(raw_elem) for raw_elem in raw]

    @classmethod
    async def from_field(
        cls: Type[ResourceOrLocationType], raw: dict, field: str
    ) -> ResourceOrLocationType:
        # Extract the field from the raw data.
        raw_value = get_field(raw, field)
        # If it's non-null, then attempt to deserialize it.
        if raw_value is not None:
            return await cls.deserialize(raw_value)

    @classmethod
    async def from_field_optional(
        cls: Type[ResourceOrLocationType], raw: dict, field: str
    ) -> Optional[ResourceOrLocationType]:
        # Extract the field from the raw data.
        raw_value = get_field(raw, field, default=None)
        # If it's non-null, then attempt to deserialize it.
        if raw_value is not None:
            return await cls.deserialize(raw_value)

    @classmethod
    async def many_from_field(
        cls: Type[ResourceOrLocationType], raw: dict, field: str, default=DEFAULT
    ) -> Optional[List[ResourceOrLocationType]]:
        raw_elems = get_field(raw, field, default=default)
        if raw_elems is not None:
            return await cls.deserialize_many(raw_elems)

    def __init__(
        self,
        resource: Optional[ResourceType] = None,
        resource_location: Optional[ResourceLocationType] = None,
    ):
        # At least one of the values must be provided.
        assert (resource is not None) or (resource_location is not None)
        # Values must either be null or the correct type.
        if resource is not None:
            assert isinstance(resource, self.resource_class)
        if resource_location is not None:
            assert isinstance(resource_location, self.resource_location_class)
        # Remember these values, internally, and resolve them on-demand.
        self.resource: Optional[ResourceType] = resource
        self.resource_location: Optional[ResourceLocationType] = resource_location

    def __call__(self, pack_context: PackContext) -> Coroutine[Any, Any, ResourceType]:
        """ Mimics the call resolution of [ResourceLocation] to be used in the same way. """
        return self.resolve_resource(pack_context)

    async def resolve_resource(self, pack_context: PackContext) -> ResourceType:
        """
        Returns the resolved [Resource], be it inline or referred.

        If this [ResourceOrLocation] contains a [Resource], it is returned directly.

        Otherwise this [ResourceOrLocation] contains a [ResourceLocation], in which case it is
        asynchronously resolved and returned.
        """
        if self.resource is not None:
            return self.resource
        assert self.resource_location is not None
        resource = await self.resource_location.resolve_resource(pack_context)
        return resource

    def location_or_inline(
        self, inline_location: ResourceLocationType
    ) -> ResourceLocationType:
        """
        Returns either the contained [ResourceLocaton] or the given [inline_location].

        If this [ResourceOrLocation] contains a [Resource], the given `inline_location` is returned.

        Otherwise this [ResourceOrLocation] contains a [ResourceLocation], in which case this is
        returned instead.

        Use this to replace code segments that need to check whether to produce an inline resource.
        """
        if self.resource is not None:
            return inline_location
        assert self.resource_location is not None
        return self.resource_location

    async def resolve_and_locate_resource(
        self, ctx: PackContext, inline_location: ResourceLocationType
    ) -> LocatedResource[ResourceType, ResourceLocationType]:
        """
        Returns a [LocatedResource] with the resolved [Resource].

        If this [ResourceOrLocation] contains a [Resource], it is paired with the given
        [inline_location].

        Otherwise this [ResourceOrLocation] contains a [ResourceLocation], in which case it is
        paired with its own asynchronous resolution.
        """
        if self.resource is not None:
            return LocatedResource(self.resource, inline_location)
        assert self.resource_location is not None
        resolved_resource = await self.resource_location(ctx)
        return LocatedResource(resolved_resource, self.resource_location)
