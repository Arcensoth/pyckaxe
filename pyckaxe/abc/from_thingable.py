from abc import ABC, abstractmethod
from typing import Any, Optional, Type, TypeVar

ClassType = TypeVar("ClassType", bound="FromThingable")


class FromThingable(ABC):
    # NOTE No generic for this because that doesn't work well with union type aliases.
    Thing = Any

    @classmethod
    def from_thing(cls: Type[ClassType], thing: Thing) -> ClassType:
        try:
            converted = cls._convert_from_thing(thing)
        except:
            raise ValueError(f"Error attempting to convert value to {cls.__name__}: {thing!r}")

        if isinstance(converted, cls):
            return converted

        if isinstance(thing, cls):
            return thing

        raise ValueError(f"Cannot convert value to {cls.__name__}: {thing!r}")

    @classmethod
    @abstractmethod
    def _convert_from_thing(cls: Type[ClassType], thing: Thing) -> Optional[ClassType]:
        ...
