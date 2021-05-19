from dataclasses import dataclass
from pathlib import Path
from typing import AsyncIterable, Generic, Type, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.physical_namespace import PhysicalNamespace
from pyckaxe.lib.pack.physical_registry_location import PhysicalRegistryLocation
from pyckaxe.lib.pack.resource_location import ClassifiedResourceLocation

__all__ = ("CommonResourceScanner",)


ResourceType = TypeVar("ResourceType", bound=Resource)


# @implements ResourceScanner
@dataclass
class CommonResourceScanner(Generic[ResourceType]):
    """
    Scans for all of a certain type of matching resource.

    Attributes
    ----------
    registry_location
        An absolute registry location used to scan for resources.
    """

    registry_location: PhysicalRegistryLocation
    resource_class: Type[ResourceType]

    def __str__(self) -> str:
        return f"{self.registry_location}"

    # @implements ResourceScanner
    def __call__(
        self, match: str = "*"
    ) -> AsyncIterable[ClassifiedResourceLocation[ResourceType]]:
        return self.scan(match)

    @property
    def namespace(self) -> PhysicalNamespace:
        return self.registry_location.namespace

    @property
    def path(self) -> Path:
        return self.registry_location.path

    async def scan(
        self,
        match: str = r"*",
    ) -> AsyncIterable[ClassifiedResourceLocation[ResourceType]]:
        """Yield all matching locations in the registry."""
        # TODO Should glob be async (in batches)? #async-file-io
        for path in self.path.rglob(match):
            if path.is_file():
                rel_path = path.relative_to(self.path)
                parts_without_ext = (*(rel_path.parts[:-1]), rel_path.stem)
                location = ClassifiedResourceLocation[ResourceType](
                    namespace=self.namespace,
                    parts=parts_without_ext,
                    resource_class=self.resource_class,
                )
                yield location
