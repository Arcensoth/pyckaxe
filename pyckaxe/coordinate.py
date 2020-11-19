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
        raise ValueError(f"Value cannot be converted to {Coordinate.__name__}: {value}")

    def __bool__(self) -> bool:
        return bool(self.value)

    def __invert__(self) -> "Coordinate":
        return RelativeCoordinate(self.value)


class AbsoluteCoordinate(Coordinate):
    def __add__(self, other: Any) -> "AbsoluteCoordinate":
        c = Coordinate.from_any(other)
        return AbsoluteCoordinate(self.value + c.value)

    # @implements CommandToken
    def command_stringify(self) -> str:
        return f"{self.value:g}"


class RelativeCoordinate(Coordinate):
    def __add__(self, other: Any) -> "RelativeCoordinate":
        c = Coordinate.from_any(other)
        return RelativeCoordinate(self.value + c.value)

    # @implements CommandToken
    def command_stringify(self) -> str:
        return f"~{self.value:g}"


class LocalCoordinate(Coordinate):
    def __add__(self, other: Any) -> "LocalCoordinate":
        c = Coordinate.from_any(other)
        return LocalCoordinate(self.value + c.value)

    # @implements CommandToken
    def command_stringify(self) -> str:
        return f"^{self.value:g}"
