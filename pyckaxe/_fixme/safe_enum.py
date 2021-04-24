from enum import Enum
from typing import Optional, Type, TypeVar

from pyckaxe.utils.fields import DEFAULT, get_field

SelfType = TypeVar("SelfType", bound=Enum)


class SafeEnum(Enum):
    def __str__(self) -> str:
        return self.value

    @classmethod
    def contains(cls: Type[SelfType], s: str) -> bool:
        return s in cls.__members__.keys()

    @classmethod
    def from_str(cls: Type[SelfType], s: str) -> Optional[SelfType]:
        try:
            return cls[s]
        except KeyError:
            return None

    @classmethod
    def from_field(
        cls: Type[SelfType], raw: dict, field: str, default=DEFAULT
    ) -> SelfType:
        raw_value = get_field(raw, field, type=str, check=cls.contains, default=default)
        value = cls[raw_value]
        return value
