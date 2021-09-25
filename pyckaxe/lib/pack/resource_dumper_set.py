from collections.abc import MutableMapping
from dataclasses import dataclass, field
from typing import Coroutine, Dict, Iterator, Type, TypeVar, cast

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.physical_resource_location import PhysicalResourceLocation
from pyckaxe.lib.pack.resource_dumper.abc.resource_dumper import ResourceDumper

__all__ = ("ResourceDumperSet",)


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


RT = TypeVar("RT", bound=Resource)
RT_co = TypeVar("RT_co", bound=Resource, covariant=True)


@dataclass
class ResourceDumperSet(MutableMapping[Type[Resource], ResourceDumper[RT_co]]):
    """
    Delegates a `ResourceDumper` based on the type of `Resource`.
    """

    _dumpers: Dict[Type[Resource], ResourceDumper[RT_co]] = field(default_factory=dict)

    def __setitem__(self, key: Type[RT], value: ResourceDumper[RT_co]):
        self._dumpers[key] = value

    def __getitem__(self, key: Type[RT]) -> ResourceDumper[RT_co]:
        for cls in key.mro():
            if issubclass(cls, Resource):
                if (dumper := self._dumpers.get(cls)) is not None:
                    return dumper
        raise NoDumperAvailableError(key)

    def __delitem__(self, key: Type[RT]):
        del self._dumpers[key]

    def __len__(self):
        return len(self._dumpers)

    def __iter__(self) -> Iterator[Type[Resource]]:
        return iter(self._dumpers)

    def __call__(
        self, resource: Resource, location: PhysicalResourceLocation
    ) -> Coroutine[None, None, None]:
        return self.dump(resource, location)

    async def dump(self, resource: Resource, location: PhysicalResourceLocation):
        """Dump `resource` to `location`."""
        resource_type = type(resource)
        try:
            dumper = self[resource_type]
            dumper = cast(ResourceDumper[RT], dumper)
            await dumper(resource, location)
        except Exception as ex:
            raise FailedToDumpResourceError(resource, location) from ex
