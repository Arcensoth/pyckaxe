from typing import Any, Tuple

from pyckaxe.command.abc.command_token import CommandToken
from pyckaxe.coordinate import Coordinate
from pyckaxe.utils.fields import DEFAULT, get_field


class Position(CommandToken):
    def __init__(self, x: Any, y: Any, z: Any):
        self.x: Coordinate = Coordinate.from_any(x)
        self.y: Coordinate = Coordinate.from_any(y)
        self.z: Coordinate = Coordinate.from_any(z)

    @staticmethod
    def from_field(raw: dict, field: str, default=DEFAULT) -> "Position":
        raw_position = get_field(
            raw, field, type=list, check=lambda obj: len(obj) == 3, default=default
        )
        position = Position(*raw_position)
        return position

    def __bool__(self) -> bool:
        return bool(self.x) or bool(self.y) or bool(self.z)

    def __invert__(self) -> "Position":
        rx = ~self.x
        ry = ~self.y
        rz = ~self.z
        return Position(rx, ry, rz)

    def __add__(self, other: Any) -> "Position":
        if isinstance(other, Position):
            return Position(self.x + other.x, self.y + other.y, self.z + other.z)
        if isinstance(other, (tuple, list)) and len(other) == 3:
            return Position(self.x + other[0], self.y + other[1], self.z + other[2])
        raise ValueError(f"Value cannot be added with {Position.__name__}: {other}")

    def unpack(self) -> Tuple[Coordinate, Coordinate, Coordinate]:
        return self.x, self.y, self.z

    # @implements CommandToken
    def command_stringify(self) -> str:
        return " ".join(coord.command_stringify() for coord in (self.x, self.y, self.z))
