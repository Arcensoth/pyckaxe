from dataclasses import dataclass
from typing import TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.physical_resource_location import PhysicalResourceLocation
from pyckaxe.lib.pack.resource_dumper.common_resource_dumper import CommonResourceDumper
from pyckaxe.utils import dump_text_async

__all__ = ("TextResourceDumper",)


ResourceType = TypeVar("ResourceType", bound=Resource)


# @implements CommonResourceDumper
@dataclass
class TextResourceDumper(CommonResourceDumper[ResourceType, str]):
    # @implements CommonResourceDumper
    @property
    def default_suffix(self) -> str:
        return ".txt"

    # @implements CommonResourceDumper
    async def _dump_raw(self, raw: str, location: PhysicalResourceLocation):
        path = await self._get_path_to_dump(location)
        await dump_text_async(raw, path, self.options)
