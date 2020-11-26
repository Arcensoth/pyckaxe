from abc import ABC, abstractmethod
from typing import Any, Union

SerializedValue = Union[int, float, str, dict, list]


class Serializable(ABC):
    @staticmethod
    def deserialize(raw: dict) -> Any:
        ...

    @abstractmethod
    def serialize(self) -> SerializedValue:
        ...


class AsyncSerializable(ABC):
    @staticmethod
    async def deserialize(raw: dict) -> Any:
        ...

    @abstractmethod
    async def serialize(self) -> SerializedValue:
        ...
