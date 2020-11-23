from abc import ABC, abstractmethod

from nbtlib import tag


class NbtSerializable(ABC):
    @abstractmethod
    def to_nbt(self) -> tag.Compound:
        ...


class AsyncNbtSerializable(ABC):
    @abstractmethod
    async def to_nbt(self) -> tag.Compound:
        ...
