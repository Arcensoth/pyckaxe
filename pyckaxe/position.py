import collections.abc
from typing import Any, Iterable, Tuple, Union

from pyckaxe.abc.from_thingable import FromThingable
from pyckaxe.command.abc.command_token import CommandToken
from pyckaxe.coordinate import AbsoluteCoordinate, Coordinate, LocalCoordinate, RelativeCoordinate
from pyckaxe.utils.fields import DEFAULT, get_field


class Position(CommandToken, FromThingable):
    Thing = Union["Position", Iterable[Union[int, float]]]

    @classmethod
    def _convert_from_thing(cls, thing):
        if isinstance(thing, collections.abc.Iterable):
            return ~Position(*thing)

    @classmethod
    def from_field(cls, raw: dict, field: str, default=DEFAULT) -> "Position":
        raw_position = get_field(
            raw, field, type=list, check=lambda obj: len(obj) == 3, default=default
        )
        position = Position(*raw_position)
        return position

    def __init__(self, x: Coordinate.Thing, y: Coordinate.Thing, z: Coordinate.Thing):
        self.x: Coordinate = Coordinate.from_thing(x)
        self.y: Coordinate = Coordinate.from_thing(y)
        self.z: Coordinate = Coordinate.from_thing(z)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.x!r}, {self.y!r}, {self.z!r})"

    def __str__(self) -> str:
        return self.command_stringify()

    def __hash__(self) -> int:
        return hash(self.x) + hash(self.y) + hash(self.z)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Position):
            return (other.x == self.x) and (other.y == self.y) and (other.z == self.z)
        return False

    def __bool__(self) -> bool:
        return bool(self.x) or bool(self.y) or bool(self.z)

    def __invert__(self) -> "Position":
        return Position(~self.x, ~self.y, ~self.z)

    def __neg__(self) -> "Position":
        return Position(-self.x, -self.y, -self.z)

    def __add__(self, other: Any) -> "Position":
        if isinstance(other, Position):
            return Position(self.x + other.x, self.y + other.y, self.z + other.z)
        if isinstance(other, (tuple, list)) and len(other) == 3:
            return Position(self.x + other[0], self.y + other[1], self.z + other[2])
        raise ValueError(f"Value cannot be added to {Position.__name__}: {other}")

    def __sub__(self, other: Any) -> "Position":
        if isinstance(other, Position):
            return Position(self.x - other.x, self.y - other.y, self.z - other.z)
        if isinstance(other, (tuple, list)) and len(other) == 3:
            return Position(self.x - other[0], self.y - other[1], self.z - other[2])
        raise ValueError(f"Value cannot be subtracted from {Position.__name__}: {other}")

    def unpack(self) -> Tuple[Coordinate, Coordinate, Coordinate]:
        return self.x, self.y, self.z

    def unpack_floats(self) -> Tuple[float, float, float]:
        return self.x.value, self.y.value, self.z.value

    def unpack_ints(self) -> Tuple[int, int, int]:
        return int(self.x.value), int(self.y.value), int(self.z.value)

    def exceeds(self, other: "Position") -> bool:
        return (self.x > other.x) and (self.y > other.y) and (self.z > other.z)

    def absolute(self) -> "Position":
        return Position(AbsoluteCoordinate(c) for c in self.unpack_floats())

    def relative(self) -> "Position":
        return Position(RelativeCoordinate(c) for c in self.unpack_floats())

    def local(self) -> "Position":
        return Position(LocalCoordinate(c) for c in self.unpack_floats())

    # @implements CommandToken
    def command_stringify(self) -> str:
        return " ".join(coord.command_stringify() for coord in (self.x, self.y, self.z))
