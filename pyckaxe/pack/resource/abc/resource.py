from abc import ABC, abstractmethod
from pathlib import Path
from typing import Generic, Type, TypeVar

from pyckaxe.utils.resources import load_dict_resource, load_raw_resource

ResourceType = TypeVar("ResourceType", bound="Resource")
RawType = TypeVar("RawType")


class Resource(ABC, Generic[RawType]):
    @staticmethod
    @abstractmethod
    async def load_raw(path: Path) -> RawType:
        ...

    @staticmethod
    @abstractmethod
    async def from_raw(raw: RawType) -> ResourceType:
        ...

    @classmethod
    async def from_path(cls: Type[ResourceType], path: Path) -> ResourceType:
        raw = await cls.load_raw(path)
        return await cls.from_raw(raw)


class RawResource(Resource[str]):
    # @implements Resource
    @staticmethod
    async def load_raw(path: Path) -> str:
        return await load_raw_resource(path)


class DictResource(Resource[dict]):
    # @implements Resource
    @staticmethod
    async def load_raw(path: Path) -> dict:
        return await load_dict_resource(path)
