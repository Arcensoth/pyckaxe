from typing import Any

from pyckaxe.command.abc.command_token import CommandToken


class Coordinate(CommandToken):
    def __init__(self, value: float):
        self.value: float = float(value)

    @staticmethod
    def from_any(value: Any) -> "Coordinate":
        if isinstance(value, Coordinate):
            return value
        if isinstance(value, float):
            return AbsoluteCoordinate(value)
        if isinstance(value, int):
            return AbsoluteCoordinate(float(value))
        raise ValueError(f"Value cannot be converted to coordinate: {value}")

    def __bool__(self) -> bool:
        return bool(self.value)

    def __invert__(self) -> "Coordinate":
        return RelativeCoordinate(self.value)


class AbsoluteCoordinate(Coordinate):
    # @implements CommandToken
    def command_stringify(self) -> str:
        return f"{self.value:g}"


class RelativeCoordinate(Coordinate):
    # @implements CommandToken
    def command_stringify(self) -> str:
        return f"~{self.value:g}"


class LocalCoordinate(Coordinate):
    # @implements CommandToken
    def command_stringify(self) -> str:
        return f"^{self.value:g}"
