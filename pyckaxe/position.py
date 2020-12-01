from typing import Any, Tuple

from pyckaxe.command.abc.command_token import CommandToken
from pyckaxe.coordinate import Coordinate
from pyckaxe.utils.fields import DEFAULT, get_field


class Position(CommandToken):
    @staticmethod
    def from_field(raw: dict, field: str, default=DEFAULT) -> "Position":
        raw_position = get_field(
            raw, field, type=list, check=lambda obj: len(obj) == 3, default=default
        )
        position = Position(*raw_position)
        return position

    def __init__(self, x: Any, y: Any, z: Any):
        self.x: Coordinate = Coordinate.from_any(x)
        self.y: Coordinate = Coordinate.from_any(y)
        self.z: Coordinate = Coordinate.from_any(z)

    def __repr__(self) -> str:
        return str(self)

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
        raise ValueError(f"Value cannot be added with {Position.__name__}: {other}")

    def unpack(self) -> Tuple[Coordinate, Coordinate, Coordinate]:
        return self.x, self.y, self.z

    def unpack_floats(self) -> Tuple[float, float, float]:
        return self.x.value, self.y.value, self.z.value

    def unpack_ints(self) -> Tuple[int, int, int]:
        return int(self.x.value), int(self.y.value), int(self.z.value)

    def exceeds(self, other: "Position") -> bool:
        return (self.x > other.x) and (self.y > other.y) and (self.z > other.z)

    # @implements CommandToken
    def command_stringify(self) -> str:
        return " ".join(coord.command_stringify() for coord in (self.x, self.y, self.z))
