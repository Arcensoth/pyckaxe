from typing import Any

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

    def __invert__(self) -> "Position":
        rx = ~self.x
        ry = ~self.y
        rz = ~self.z
        return Position(rx, ry, rz)

    # @implements CommandToken
    def command_stringify(self) -> str:
        return " ".join(coord.command_stringify() for coord in (self.x, self.y, self.z))
