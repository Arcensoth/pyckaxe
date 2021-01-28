from pathlib import Path
from typing import AsyncIterable, Generic, Tuple, Type, TypeVar

from pyckaxe.pack.readable_registry_node import ReadableRegistryNode
from pyckaxe.pack.registry_location import RegistryLocation
from pyckaxe.pack.resource.abc.resource import Resource
from pyckaxe.pack.resource.abc.resource_location import ResourceLocation

ResourceType = TypeVar("ResourceType", bound=Resource)
ResourceLocationType = TypeVar("ResourceLocationType", bound=ResourceLocation)


class ReadableResourceRegistry(
    ReadableRegistryNode, Generic[ResourceType, ResourceLocationType]
):
    """ A registry with a physical, readable directory and resource files. """

    # NOTE Apparently this nested type alias only works from within the class?
    ResourceTriplet = Tuple[ResourceType, ResourceLocationType, Path]

    def __init__(
        self,
        registry_location: RegistryLocation,
        path: Path,
        resource_class: Type[ResourceType],
        resource_location_class: Type[ResourceLocationType],
    ):
        super().__init__(registry_location, path)
        assert isinstance(resource_class, type)
        assert isinstance(resource_location_class, type)
        self.resource_class: Type[ResourceType] = resource_class
        self.resource_location_class: Type[
            ResourceLocationType
        ] = resource_location_class

    async def iter_all(self) -> AsyncIterable[ResourceTriplet]:
        for path in self.path.rglob(r"[!!]*"):
            if path.is_file():
                rel_path = path.relative_to(self.path)
                parts_without_ext = (*(rel_path.parts[:-1]), rel_path.stem)
                resource_location = self.resource_location_class(
                    self.registry_location.namespace, parts_without_ext
                )
                partial_path = path.with_suffix("")
                resource = await self.resource_class.load(partial_path)
                yield resource, resource_location, path
