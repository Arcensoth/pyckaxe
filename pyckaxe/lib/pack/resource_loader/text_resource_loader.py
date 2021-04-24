from dataclasses import dataclass
from typing import TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.physical_resource_location import PhysicalResourceLocation
from pyckaxe.lib.pack.resource_loader.common_resource_loader import CommonResourceLoader

__all__ = ("TextResourceLoader",)


ResourceType = TypeVar("ResourceType", bound=Resource)


# @implements CommonResourceLoader
@dataclass
class TextResourceLoader(CommonResourceLoader[ResourceType, str]):
    # @implements CommonResourceLoader
    async def _load_raw(self, location: PhysicalResourceLocation) -> str:
        path = await self._get_path_to_load(location)
        with path.open("r", **self.options) as fp:
            return fp.read()
