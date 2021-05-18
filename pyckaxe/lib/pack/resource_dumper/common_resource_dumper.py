from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Coroutine, Dict, Generic, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.abc.resource_serializer import ResourceSerializer
from pyckaxe.lib.pack.physical_resource_location import PhysicalResourceLocation
from pyckaxe.lib.pack.resource_dumper.errors import (
    FailedToDumpResourceError,
    NonFileResourceExistsError,
    ResourceDumperError,
)
from pyckaxe.utils import DEFAULT

__all__ = ("CommonResourceDumper",)


ResourceType = TypeVar("ResourceType", bound=Resource)
RawType = TypeVar("RawType")


# @implements ResourceDumper
@dataclass
class CommonResourceDumper(ABC, Generic[ResourceType, RawType]):
    """
    Dumps a resource to an absolute resource location.

    Similar to `CommonResourceLoader` but in the opposite direction.

    Attributes
    ----------
    serializer
        Turns a resource into raw data.
    options
        Arbitrary options to pass to the underlying dumping mechanism.
    """

    serializer: ResourceSerializer[ResourceType, RawType]
    options: Dict[str, Any] = field(default=DEFAULT)
    suffix: str = field(default=DEFAULT)

    @property
    @abstractmethod
    def default_suffix(self) -> str:
        ...

    @abstractmethod
    async def _dump_raw(self, raw: RawType, location: PhysicalResourceLocation):
        ...

    @classmethod
    def default_options_factory(cls) -> Dict[str, Any]:
        return dict()

    def __post_init__(self):
        if self.options is DEFAULT:
            self.options = self.default_options_factory()
        if self.suffix is DEFAULT:
            self.suffix = self.default_suffix

    async def _get_path_to_dump(self, location: PhysicalResourceLocation) -> Path:
        """
        Get the file path matching `location`.

        Raises
        ------
        NonFileResourceExistsError
            If a non-file already exists at the corresponding path.
        """
        path = location.path.with_suffix(self.suffix)
        if path.exists() and not path.is_file():
            raise NonFileResourceExistsError(path)
        return path

    async def dump(self, resource: ResourceType, location: PhysicalResourceLocation):
        """Dump `resource` to `location`."""
        try:
            # Serialize the resource.
            raw = self.serializer(resource)
            # Make sure the target directory exists.
            location.path.parent.mkdir(parents=True, exist_ok=True)
            # Dump the raw data to file.
            await self._dump_raw(raw, location)
        except ResourceDumperError:
            raise
        except Exception as ex:
            raise FailedToDumpResourceError(location.path) from ex

    # @implements ResourceDumper
    def __call__(
        self, resource: ResourceType, location: PhysicalResourceLocation
    ) -> Coroutine[None, None, None]:
        return self.dump(resource, location)
