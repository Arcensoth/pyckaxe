from dataclasses import dataclass
from typing import TypeVar

from pyckaxe.lib.nbt import NbtCompound
from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.physical_resource_location import PhysicalResourceLocation
from pyckaxe.lib.pack.resource_dumper.common_resource_dumper import CommonResourceDumper
from pyckaxe.utils import dump_nbt_async

__all__ = ("NbtResourceDumper",)


ResourceType = TypeVar("ResourceType", bound=Resource)


# @implements CommonResourceDumper
@dataclass
class NbtResourceDumper(CommonResourceDumper[ResourceType, NbtCompound]):
    # @implements CommonResourceDumper
    @property
    def default_suffix(self) -> str:
        return ".nbt"

    # @implements CommonResourceDumper
    async def _dump_raw(self, raw: NbtCompound, location: PhysicalResourceLocation):
        path = await self._get_path_to_dump(location)
        await dump_nbt_async(raw, path, self.options)
