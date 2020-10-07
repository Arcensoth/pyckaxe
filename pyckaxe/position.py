from typing import Any

from pyckaxe.command.abc.command_token import CommandToken
from pyckaxe.coordinate import Coordinate
from pyckaxe.utils.fields import get_field


class Position(CommandToken):
    def __init__(self, x: Any, y: Any, z: Any):
        self.x: Coordinate = Coordinate.from_any(x)
        self.y: Coordinate = Coordinate.from_any(y)
        self.z: Coordinate = Coordinate.from_any(z)

    @staticmethod
    def from_field(raw: dict, name: str) -> "Position":
        raw_pos = get_field(raw, name, type=list, check=lambda obj: len(obj) == 3)
        return Position(*raw_pos)

    def __invert__(self) -> "Position":
        rx = ~self.x
        ry = ~self.y
        rz = ~self.z
        return Position(rx, ry, rz)

    # @implements CommandToken
    def command_stringify(self) -> str:
        return " ".join(coord.command_stringify() for coord in (self.x, self.y, self.z))
