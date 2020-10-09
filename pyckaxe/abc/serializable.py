from abc import ABC, abstractmethod
from typing import Union

SerializedValue = Union[int, float, str, dict, list]


class Serializable(ABC):
    @abstractmethod
    def serialize(self) -> SerializedValue:
        ...


class AsyncSerializable(ABC):
    @abstractmethod
    async def serialize(self) -> SerializedValue:
        ...
