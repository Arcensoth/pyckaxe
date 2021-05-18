import re
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Coroutine, Dict, Generic, List, TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.abc.resource_deserializer import ResourceDeserializer
from pyckaxe.lib.pack.physical_resource_location import PhysicalResourceLocation
from pyckaxe.lib.pack.resource_loader.errors import (
    DuplicateResourceError,
    FailedToLoadResourceError,
    NoSuchResourceError,
    ResourceLoaderError,
)
from pyckaxe.utils import DEFAULT

__all__ = ("CommonResourceLoader",)


ResourceType = TypeVar("ResourceType", bound=Resource)
RawType = TypeVar("RawType")


# @implements ResourceLoader
@dataclass
class CommonResourceLoader(ABC, Generic[ResourceType, RawType]):
    """
    Loads a resource from an absolute resource location.

    This class is responsible for loading a file of a certain data format (such as NBT,
    JSON, or plain text) from a `PhysicalResourceLocation`, and then converting the raw
    data of type `RawType` into an instance of the corresponding `ResourceType`.

    A new implementation is typically only required when a new type of file format or a
    new loading mechanism needs to be supported.

    Attributes
    ----------
    deserializer
        Turns raw data into a resource.
    options
        Arbitrary options to pass to the underlying loading mechanism.
    """

    deserializer: ResourceDeserializer[ResourceType, RawType]
    options: Dict[str, Any] = field(default=DEFAULT)

    @abstractmethod
    async def _load_raw(self, location: PhysicalResourceLocation) -> RawType:
        ...

    @classmethod
    def default_options_factory(cls) -> Dict[str, Any]:
        return dict()

    def __post_init__(self):
        if self.options is DEFAULT:
            self.options = self.default_options_factory()

    async def _get_matching_paths(
        self, location: PhysicalResourceLocation
    ) -> List[Path]:
        """Get all file paths matching `location`."""
        # Since glob isn't expressive enough, we need to do a second pass with regex.
        # TODO Should glob be async? #async-file-io
        pattern = re.compile(r"^" + location.path.name + r"(?:\.[^\.]*)?$")
        all_paths = [path for path in location.path.parent.glob("*") if path.is_file()]
        matching_paths = [p for p in all_paths if pattern.match(p.name)]
        return matching_paths

    async def _get_path_to_load(self, location: PhysicalResourceLocation) -> Path:
        """
        Get the first file path matching `location`.

        Raises
        ------
        NoSuchResourceError
            If no file paths matching `location` are found.
        """
        paths = await self._get_matching_paths(location)
        if len(paths) < 1:
            raise NoSuchResourceError(location.path)
        elif len(paths) > 1:
            raise DuplicateResourceError(location.path, paths)
        return paths[0]

    async def load(self, location: PhysicalResourceLocation) -> ResourceType:
        """Load a `Resource` from `location`."""
        try:
            # Load the raw data from file.
            raw = await self._load_raw(location)
            # Deserialize the raw data into an object.
            resource = self.deserializer(raw)
            return resource
        except ResourceLoaderError:
            raise
        except Exception as ex:
            raise FailedToLoadResourceError(location.path) from ex

    # @implements ResourceLoader
    def __call__(
        self, location: PhysicalResourceLocation
    ) -> Coroutine[None, None, ResourceType]:
        return self.load(location)
