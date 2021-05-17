from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List, Tuple, Union

from pyckaxe.lib.coordinate import Coordinate, CoordinateConvertible

__all__ = (
    "PositionConvertible",
    "MalformedPosition",
    "Position",
    "ORIGIN",
    "HERE",
    "THERE",
    "NORTH",
    "SOUTH",
    "WEST",
    "EAST",
    "DOWN",
    "UP",
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


class MalformedPosition(Exception):
    def __init__(self, message: str, value: Any):
        self.value: Any = value
        super().__init__(f"Can't convert value `{value}` to position: {message}")


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
        if isinstance(value, list):
            return cls.from_list(value)
        raise MalformedPosition(f"Bad type: {type(value)}", value)

    @classmethod
    def from_xyz(
        cls,
        x: CoordinateConvertible,
        y: CoordinateConvertible,
        z: CoordinateConvertible,
    ) -> Position:
        return cls(Coordinate.convert(x), Coordinate.convert(y), Coordinate.convert(z))

    @classmethod
    def from_tuple(cls, value: PositionAsTuple) -> Position:
        if len(value) != 3:
            raise MalformedPosition(f"Bad length: {len(value)}", value)
        return cls.from_xyz(value[0], value[1], value[2])

    @classmethod
    def from_list(cls, value: PositionAsList) -> Position:
        if len(value) != 3:
            raise MalformedPosition(f"Bad length: {len(value)}", value)
        return cls.from_xyz(value[0], value[1], value[2]).relative()

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return " ".join(str(coord) for coord in (self.x, self.y, self.z))

    def __hash__(self) -> int:
        return hash(str(self))

    def __neg__(self) -> Position:
        return self.__class__(-self.x, -self.y, -self.z)

    def __pos__(self) -> Position:
        return self.__class__(+self.x, +self.y, +self.z)

    def __abs__(self) -> Position:
        return self.__class__(abs(self.x), abs(self.y), abs(self.z))

    def __invert__(self) -> Position:
        return self.__class__(~self.x, ~self.y, ~self.z)

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
        return float(self.x.value), float(self.y.value), float(self.z.value)

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


ORIGIN: Position = Position.from_xyz(0, 0, 0)
HERE: Position = ORIGIN.relative()
THERE: Position = ORIGIN.local()

NORTH = Position.from_xyz(0, 0, -1)
SOUTH = Position.from_xyz(0, 0, 1)
WEST = Position.from_xyz(-1, 0, 0)
EAST = Position.from_xyz(1, 0, 0)
DOWN = Position.from_xyz(0, -1, 0)
UP = Position.from_xyz(0, 1, 0)
