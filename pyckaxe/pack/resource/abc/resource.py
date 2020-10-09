import json
from abc import abstractmethod
from pathlib import Path
from typing import Generic, Type, TypeVar

from pyckaxe.abc.serializable import AsyncSerializable
from pyckaxe.utils.resources import ResourceError, load_dict_resource, load_raw_resource

ResourceType = TypeVar("ResourceType", bound="Resource")
RawType = TypeVar("RawType")


class Resource(AsyncSerializable, Generic[RawType]):
    @classmethod
    @abstractmethod
    async def _load_raw(cls, partial_path: Path) -> RawType:
        ...

    @classmethod
    @abstractmethod
    async def _dump_raw(cls, raw: RawType, partial_path: Path):
        ...

    @staticmethod
    @abstractmethod
    async def deserialize(raw: RawType) -> ResourceType:
        ...

    @abstractmethod
    async def serialize(self) -> RawType:
        ...

    @classmethod
    async def load(cls: Type[ResourceType], partial_path: Path) -> ResourceType:
        try:
            raw = await cls._load_raw(partial_path)
            return await cls.deserialize(raw)
        except ResourceError:
            raise
        except Exception as ex:
            raise ResourceError(partial_path) from ex

    async def dump(self, partial_path: Path) -> ResourceType:
        raw = await self.serialize()
        partial_path.parent.mkdir(parents=True, exist_ok=True)
        await self._dump_raw(raw, partial_path)


class RawResource(Resource[str]):
    _file_suffix = ".txt"

    # @implements Resource
    @classmethod
    async def _load_raw(cls, partial_path: Path) -> str:
        return await load_raw_resource(partial_path)

    # @implements Resource
    @classmethod
    async def _dump_raw(cls, raw: dict, partial_path: Path):
        with open(partial_path.with_suffix(cls._file_suffix), "w") as fp:
            fp.write(raw)


class DictResource(Resource[dict]):
    _file_suffix = ".json"

    # @implements Resource
    @classmethod
    async def _load_raw(cls, partial_path: Path) -> dict:
        return await load_dict_resource(partial_path)

    # @implements Resource
    @classmethod
    async def _dump_raw(cls, raw: dict, partial_path: Path):
        with open(partial_path.with_suffix(cls._file_suffix), "w") as fp:
            json.dump(raw, fp)
