from dataclasses import dataclass
from typing import TypeVar

from pyckaxe.lib.nbt import NbtCompound
from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.physical_resource_location import PhysicalResourceLocation
from pyckaxe.lib.pack.resource_loader.common_resource_loader import CommonResourceLoader
from pyckaxe.lib.pack.resource_loader.errors import UnsupportedResourceExtensionError
from pyckaxe.utils import load_nbt_async

__all__ = ("NbtResourceLoader",)


ResourceType = TypeVar("ResourceType", bound=Resource)


# @implements CommonResourceLoader
@dataclass
class NbtResourceLoader(CommonResourceLoader[ResourceType, NbtCompound]):
    # @implements CommonResourceLoader
    async def _load_raw(self, location: PhysicalResourceLocation) -> NbtCompound:
        path = await self._get_path_to_load(location)
        if path.suffix == ".nbt":
            return await load_nbt_async(path, **self.options)
        raise UnsupportedResourceExtensionError(path)
