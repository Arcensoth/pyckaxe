from dataclasses import dataclass
from typing import TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.physical_resource_location import PhysicalResourceLocation
from pyckaxe.lib.pack.resource_dumper.common_resource_dumper import CommonResourceDumper
from pyckaxe.lib.types import JsonValue
from pyckaxe.utils import dump_json_async

__all__ = ("JsonResourceDumper",)


ResourceType = TypeVar("ResourceType", bound=Resource)


# @implements CommonResourceDumper
@dataclass
class JsonResourceDumper(CommonResourceDumper[ResourceType, JsonValue]):
    # @implements CommonResourceDumper
    @property
    def default_suffix(self) -> str:
        return ".json"

    # @implements CommonResourceDumper
    async def _dump_raw(self, raw: JsonValue, location: PhysicalResourceLocation):
        path = await self._get_path_to_dump(location)
        await dump_json_async(raw, path, self.options)
