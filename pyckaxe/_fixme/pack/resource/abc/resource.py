import json
from abc import abstractmethod
from pathlib import Path
from typing import Generic, Type, TypeVar

import nbtlib
from pyckaxe.abc.serializable import AsyncSerializable
from pyckaxe.utils.resources import (
    ResourceError,
    load_dict_resource,
    load_nbt_resource,
    load_raw_resource,
)

ResourceType = TypeVar("ResourceType", bound="Resource")
RawType = TypeVar("RawType")


class Resource(AsyncSerializable, Generic[RawType]):
    @classmethod
    @abstractmethod
    async def _load_raw(cls, partial_path: Path, **options) -> RawType:
        ...

    @classmethod
    @abstractmethod
    async def _dump_raw(cls, raw: RawType, partial_path: Path, **options):
        ...

    @staticmethod
    @abstractmethod
    async def deserialize(raw: RawType, **options) -> ResourceType:
        ...

    @abstractmethod
    async def serialize(self, **options) -> RawType:
        ...

    @classmethod
    async def load(
        cls: Type[ResourceType], partial_path: Path, **options
    ) -> ResourceType:
        try:
            raw = await cls._load_raw(partial_path, **options)
            return await cls.deserialize(raw, **options)
        except ResourceError:
            raise
        except Exception as ex:
            raise ResourceError(partial_path, f"Resource error: {partial_path}") from ex

    async def dump(self, partial_path: Path, **options) -> ResourceType:
        raw = await self.serialize(**options)
        partial_path.parent.mkdir(parents=True, exist_ok=True)
        await self._dump_raw(raw, partial_path, **options)


class RawResource(Resource[str]):
    _file_suffix = ".txt"

    # @implements Resource
    @classmethod
    async def _load_raw(cls, partial_path: Path, **options) -> str:
        return await load_raw_resource(partial_path)

    # @implements Resource
    @classmethod
    async def _dump_raw(cls, raw: str, partial_path: Path, **options):
        with open(partial_path.with_suffix(cls._file_suffix), "w") as fp:
            fp.write(raw)


class DictResource(Resource[dict]):
    _file_suffix = ".json"

    # @implements Resource
    @classmethod
    async def _load_raw(cls, partial_path: Path, **options) -> dict:
        return await load_dict_resource(partial_path)

    # @implements Resource
    @classmethod
    async def _dump_raw(cls, raw: dict, partial_path: Path, indent: int = 2, **options):
        with open(partial_path.with_suffix(cls._file_suffix), "w") as fp:
            json.dump(raw, fp, indent=indent)


class NbtResource(Resource[nbtlib.Compound]):
    _file_suffix = ".nbt"

    # @implements Resource
    @classmethod
    async def _load_raw(cls, partial_path: Path, **options) -> nbtlib.Compound:
        return await load_nbt_resource(partial_path)

    # @implements Resource
    @classmethod
    async def _dump_raw(cls, raw: nbtlib.Compound, partial_path: Path, **options):
        filename = partial_path.with_suffix(cls._file_suffix)
        nbtfile = nbtlib.File({"": raw}, gzipped=True)
        nbtfile.save(filename)
