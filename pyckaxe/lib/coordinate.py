from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Any, ClassVar, Dict, Union

__all__ = (
    "CoordinateConvertible",
    "Coordinate",
)

CoordinateAsNumber = Union[int, float]
CoordinateConvertible = Union[
    "Coordinate",
    CoordinateAsNumber,
]


class CoordinateSign(Enum):
    ABSOLUTE = "absolute"
    RELATIVE = "relative"
    LOCAL = "local"


@dataclass(frozen=True)
class Coordinate:
    value: float
    sign: CoordinateSign = CoordinateSign.ABSOLUTE

    PREFIX_MAP: ClassVar[Dict[CoordinateSign, str]] = {
        CoordinateSign.ABSOLUTE: "",
        CoordinateSign.RELATIVE: "~",
        CoordinateSign.LOCAL: "^",
    }

    @classmethod
    def convert(cls, value: CoordinateConvertible) -> Coordinate:
        if isinstance(value, cls):
            return value
        assert isinstance(value, (int, float))
        return cls.from_number(value)

    @classmethod
    def from_number(cls, n: CoordinateAsNumber) -> Coordinate:
        return cls(float(n))

    def __str__(self) -> str:
        prefix = self.prefix
        if self.value == 0 and prefix:
            return prefix
        return f"{prefix}{self.value:g}"

    def __hash__(self) -> int:
        return hash(str(self))

    def __lt__(self, other: Any) -> bool:
        return other.__lt__(self.value)

    def __gt__(self, other: Any) -> bool:
        return other.__gt__(self.value)

    def __int__(self) -> int:
        return int(self.value)

    def __neg__(self) -> Coordinate:
        return Coordinate(-self.value, sign=self.sign)

    def __pos__(self) -> Coordinate:
        return self.absolute()

    def __abs__(self) -> Coordinate:
        return Coordinate(abs(self.value), sign=self.sign)

    def __invert__(self) -> Coordinate:
        return self.relative()

    def __add__(self, other: CoordinateConvertible) -> Coordinate:
        other_coord = Coordinate.convert(other)
        new_coord = Coordinate(self.value + other_coord.value, sign=self.sign)
        return new_coord

    def __radd__(self, other: CoordinateConvertible) -> Coordinate:
        return self.__add__(other)

    def __sub__(self, other: CoordinateConvertible) -> Coordinate:
        other_coord = Coordinate.convert(other)
        new_coord = Coordinate(self.value - other_coord.value, sign=self.sign)
        return new_coord

    def __mul__(self, other: CoordinateConvertible) -> Coordinate:
        other_coord = Coordinate.convert(other)
        new_coord = Coordinate(self.value * other_coord.value, sign=self.sign)
        return new_coord

    def __rmul__(self, other: CoordinateConvertible) -> Coordinate:
        return self.__mul__(other)

    def __floordiv__(self, other: CoordinateConvertible) -> Coordinate:
        other_coord = Coordinate.convert(other)
        new_coord = Coordinate(self.value // other_coord.value, sign=self.sign)
        return new_coord

    def __truediv__(self, other: CoordinateConvertible) -> Coordinate:
        other_coord = Coordinate.convert(other)
        new_coord = Coordinate(self.value / other_coord.value, sign=self.sign)
        return new_coord

    def __mod__(self, other: CoordinateConvertible) -> Coordinate:
        other_coord = Coordinate.convert(other)
        new_coord = Coordinate(self.value % other_coord.value, sign=self.sign)
        return new_coord

    def __pow__(self, other: CoordinateConvertible) -> Coordinate:
        other_coord = Coordinate.convert(other)
        new_coord = Coordinate(self.value ** other_coord.value, sign=self.sign)
        return new_coord

    @property
    def is_absolute(self) -> bool:
        return self.sign == CoordinateSign.ABSOLUTE

    @property
    def is_relative(self) -> bool:
        return self.sign == CoordinateSign.RELATIVE

    @property
    def is_local(self) -> bool:
        return self.sign == CoordinateSign.LOCAL

    @property
    def prefix(self) -> str:
        return self.PREFIX_MAP[self.sign]

    def absolute(self) -> Coordinate:
        return Coordinate(self.value, sign=CoordinateSign.ABSOLUTE)

    def relative(self) -> Coordinate:
        return Coordinate(self.value, sign=CoordinateSign.RELATIVE)

    def local(self) -> Coordinate:
        return Coordinate(self.value, sign=CoordinateSign.LOCAL)
