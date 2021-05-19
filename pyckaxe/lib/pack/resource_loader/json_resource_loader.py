from dataclasses import dataclass
from typing import TypeVar

from pyckaxe.lib.pack.abc.resource import Resource
from pyckaxe.lib.pack.physical_resource_location import PhysicalResourceLocation
from pyckaxe.lib.pack.resource_loader.common_resource_loader import CommonResourceLoader
from pyckaxe.lib.pack.resource_loader.errors import UnsupportedResourceExtensionError
from pyckaxe.lib.types import JsonValue
from pyckaxe.utils import load_json_async, load_yaml_async

__all__ = ("JsonResourceLoader",)


ResourceType = TypeVar("ResourceType", bound=Resource)


# @implements CommonResourceLoader
@dataclass
class JsonResourceLoader(CommonResourceLoader[ResourceType, JsonValue]):
    # @implements CommonResourceLoader
    async def _load_raw(self, location: PhysicalResourceLocation) -> JsonValue:
        path = await self._get_path_to_load(location)
        if path.suffix == ".json":
            return await load_json_async(path, **self.options)
        if path.suffix in (".yaml", ".yml"):
            return await load_yaml_async(path, **self.options)
        raise UnsupportedResourceExtensionError(path)
