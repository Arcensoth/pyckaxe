from dataclasses import dataclass, field
from typing import Coroutine, Dict, Iterator, Type, TypeVar, cast

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.physical_resource_location import PhysicalResourceLocation
from pyckaxe.lib.pack.resource_dumper.abc.resource_dumper import ResourceDumper

__all__ = ("ResourceDumperSet",)


ResourceType = TypeVar("ResourceType", bound=Resource)


class ResourceDumperError(Exception):
    pass


class FailedToDumpResourceError(ResourceDumperError):
    def __init__(self, resource: Resource, location: PhysicalResourceLocation):
        self.resource: Resource = resource
        self.location: PhysicalResourceLocation = location
        super().__init__(f"Failed to dump resource to: {location}")


class NoDumperAvailableError(ResourceDumperError):
    def __init__(self, resource_type: Type[Resource]):
        super().__init__(
            f"No resource dumper mapped for resource type {resource_type.__name__}"
        )


@dataclass
class ResourceDumperSet:
    """
    Delegates a `ResourceDumper` based on the type of `Resource`.
    """

    _dumpers: Dict[Type[Resource], ResourceDumper[Resource]] = field(
        default_factory=dict
    )

    def __setitem__(self, key: Type[ResourceType], value: ResourceDumper[ResourceType]):
        self._dumpers[key] = cast(ResourceDumper[Resource], value)

    def __getitem__(self, key: Type[ResourceType]) -> ResourceDumper[ResourceType]:
        for cls in key.mro():
            if dumper := self._dumpers.get(cls):
                return dumper
        raise NoDumperAvailableError(key)

    def __delitem__(self, key: Type[ResourceType]):
        self._dumpers.__delitem__(key)

    def __len__(self):
        return self._dumpers.__len__()

    def __iter__(self) -> Iterator[ResourceDumper[Resource]]:
        return self._dumpers.values().__iter__()

    def __call__(
        self, resource: Resource, location: PhysicalResourceLocation
    ) -> Coroutine[None, None, None]:
        return self.dump(resource, location)

    async def dump(self, resource: Resource, location: PhysicalResourceLocation):
        """Dump `resource` to `location`."""
        resource_type = type(resource)
        try:
            dumper = self[resource_type]
            await dumper(resource, location)
        except Exception as ex:
            raise FailedToDumpResourceError(resource, location) from ex
