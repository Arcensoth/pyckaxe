from dataclasses import dataclass
from typing import Any, List, Tuple, Union

from pyckaxe.coordinate import Coordinate, CoordinateConvertible, to_coordinate

__all__ = (
    "PositionConvertible",
    "to_position",
    "Position",
)


PositionAsTuple = Tuple[
    CoordinateConvertible, CoordinateConvertible, CoordinateConvertible
]
PositionAsList = List[CoordinateConvertible]
PositionConvertible = Union[
    "Position",
    PositionAsTuple,
    PositionAsList,
]


def to_position(value: PositionConvertible) -> "Position":
    if isinstance(value, Position):
        return value
    # tuple -> absolute
    if isinstance(value, tuple):
        return Position.from_tuple(value)
    # list -> relative
    assert isinstance(value, list)
    return Position.from_list(value)


@dataclass
class Position:
    x: Coordinate
    y: Coordinate
    z: Coordinate

    @classmethod
    def from_xyz(
        cls,
        x: CoordinateConvertible,
        y: CoordinateConvertible,
        z: CoordinateConvertible,
    ) -> "Position":
        return cls(to_coordinate(x), to_coordinate(y), to_coordinate(z))

    @classmethod
    def from_tuple(cls, t: PositionAsTuple) -> "Position":
        assert len(t) == 3
        return cls.from_xyz(t[0], t[1], t[2])

    @classmethod
    def from_list(cls, l: PositionAsList) -> "Position":
        assert len(l) == 3
        return cls.from_xyz(l[0], l[1], l[2]).relative()

    def __str__(self) -> str:
        return self.command_tokenize()

    def __hash__(self) -> int:
        return hash(str(self))

    def __eq__(self, other: Any) -> bool:
        return (
            isinstance(other, Position)
            and (other.x == self.x)
            and (other.y == self.y)
            and (other.z == self.z)
        )

    def __invert__(self) -> "Position":
        return self.__class__(~self.x, ~self.y, ~self.z)

    def __neg__(self) -> "Position":
        return self.__class__(-self.x, -self.y, -self.z)

    def __add__(self, other: PositionConvertible) -> "Position":
        other_position = to_position(other)
        new_position = self.__class__(
            self.x + other_position.x,
            self.y + other_position.y,
            self.z + other_position.z,
        )
        return new_position

    def __sub__(self, other: PositionConvertible) -> "Position":
        other_position = to_position(other)
        new_position = self.__class__(
            self.x - other_position.x,
            self.y - other_position.y,
            self.z - other_position.z,
        )
        return new_position

    def unpack(self) -> Tuple[Coordinate, Coordinate, Coordinate]:
        return self.x, self.y, self.z

    def unpack_floats(self) -> Tuple[float, float, float]:
        return self.x.value, self.y.value, self.z.value

    def unpack_ints(self) -> Tuple[int, int, int]:
        return int(self.x.value), int(self.y.value), int(self.z.value)

    def exceeds(self, other: "Position") -> bool:
        return (self.x > other.x) and (self.y > other.y) and (self.z > other.z)

    def absolute(self) -> "Position":
        return self.__class__(self.x.absolute(), self.y.absolute(), self.z.absolute())

    def relative(self) -> "Position":
        return self.__class__(self.x.relative(), self.y.relative(), self.z.relative())

    def local(self) -> "Position":
        return self.__class__(self.x.local(), self.y.local(), self.z.local())

    # @implements CommandToken
    def command_tokenize(self) -> str:
        return " ".join(coord.command_tokenize() for coord in (self.x, self.y, self.z))
