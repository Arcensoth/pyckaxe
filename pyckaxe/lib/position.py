from __future__ import annotations

from dataclasses import dataclass
from typing import List, Tuple, Union

from pyckaxe.lib.coordinate import Coordinate, CoordinateConvertible

__all__ = (
    "PositionConvertible",
    "Position",
)


PositionAsTuple = Tuple[
    CoordinateConvertible, CoordinateConvertible, CoordinateConvertible
]
PositionAsList = Union[
    List[int],
    List[float],
    List[Union[int, float]],
    List[Coordinate],
    List[CoordinateConvertible],
]
PositionConvertible = Union[
    "Position",
    PositionAsTuple,
    PositionAsList,
]


@dataclass(frozen=True)
class Position:
    x: Coordinate
    y: Coordinate
    z: Coordinate

    @classmethod
    def convert(cls, value: PositionConvertible) -> Position:
        if isinstance(value, cls):
            return value
        # tuple -> absolute
        if isinstance(value, tuple):
            return cls.from_tuple(value)
        # list -> relative
        assert isinstance(value, list)
        return cls.from_list(value)

    @classmethod
    def from_xyz(
        cls,
        x: CoordinateConvertible,
        y: CoordinateConvertible,
        z: CoordinateConvertible,
    ) -> Position:
        return cls(Coordinate.convert(x), Coordinate.convert(y), Coordinate.convert(z))

    @classmethod
    def from_tuple(cls, t: PositionAsTuple) -> Position:
        assert len(t) == 3
        return cls.from_xyz(t[0], t[1], t[2])

    @classmethod
    def from_list(cls, l: PositionAsList) -> Position:
        assert len(l) == 3
        return cls.from_xyz(l[0], l[1], l[2]).relative()

    def __str__(self) -> str:
        return " ".join(str(coord) for coord in (self.x, self.y, self.z))

    def __hash__(self) -> int:
        return hash(str(self))

    def __invert__(self) -> Position:
        return self.__class__(~self.x, ~self.y, ~self.z)

    def __neg__(self) -> Position:
        return self.__class__(-self.x, -self.y, -self.z)

    def __add__(self, other: PositionConvertible) -> Position:
        other_position = Position.convert(other)
        new_position = self.__class__(
            self.x + other_position.x,
            self.y + other_position.y,
            self.z + other_position.z,
        )
        return new_position

    def __radd__(self, other: PositionConvertible) -> Position:
        other_position = Position.convert(other)
        new_position = self.__class__(
            other_position.x + self.x,
            other_position.y + self.y,
            other_position.z + self.z,
        )
        return new_position

    def __sub__(self, other: PositionConvertible) -> Position:
        other_position = Position.convert(other)
        new_position = self.__class__(
            self.x - other_position.x,
            self.y - other_position.y,
            self.z - other_position.z,
        )
        return new_position

    def __mul__(self, other: CoordinateConvertible) -> Position:
        return self.__class__(
            self.x * other,
            self.y * other,
            self.z * other,
        )

    def __rmul__(self, other: CoordinateConvertible) -> Position:
        return self.__class__(
            other * self.x,
            other * self.y,
            other * self.z,
        )

    def __truediv__(self, other: CoordinateConvertible) -> Position:
        return self.__class__(
            self.x / other,
            self.y / other,
            self.z / other,
        )

    def __floordiv__(self, other: CoordinateConvertible) -> Position:
        return self.__class__(
            self.x // other,
            self.y // other,
            self.z // other,
        )

    def __mod__(self, other: CoordinateConvertible) -> Position:
        return self.__class__(
            self.x % other,
            self.y % other,
            self.z % other,
        )

    def __pow__(self, other: CoordinateConvertible) -> Position:
        return self.__class__(
            self.x ** other,
            self.y ** other,
            self.z ** other,
        )

    def unpack(self) -> Tuple[Coordinate, Coordinate, Coordinate]:
        return self.x, self.y, self.z

    def unpack_floats(self) -> Tuple[float, float, float]:
        return self.x.value, self.y.value, self.z.value

    def unpack_ints(self) -> Tuple[int, int, int]:
        return int(self.x.value), int(self.y.value), int(self.z.value)

    def exceeds(self, other: Position) -> bool:
        return (self.x > other.x) and (self.y > other.y) and (self.z > other.z)

    def absolute(self) -> Position:
        return self.__class__(self.x.absolute(), self.y.absolute(), self.z.absolute())

    def relative(self) -> Position:
        return self.__class__(self.x.relative(), self.y.relative(), self.z.relative())

    def local(self) -> Position:
        return self.__class__(self.x.local(), self.y.local(), self.z.local())
