from typing import Any, Union

from pyckaxe.abc.from_thingable import FromThingable
from pyckaxe.command.abc.command_token import CommandToken


class Coordinate(CommandToken, FromThingable):
    Thing = Union["Coordinate", float, int]

    @classmethod
    def _convert_from_thing(cls, thing):
        if isinstance(thing, (float, int)):
            return AbsoluteCoordinate(float(thing))

    def __init__(self, value: float):
        self.value: float = float(value)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.value!r})"

    def __str__(self) -> str:
        return self.command_stringify()

    def __hash__(self) -> int:
        return hash(self.value)

    def __eq__(self, other: Any) -> bool:
        return other.__eq__(self.value)

    def __lt__(self, other: Any) -> bool:
        return other.__lt__(self.value)

    def __gt__(self, other: Any) -> bool:
        return other.__gt__(self.value)

    def __bool__(self) -> bool:
        return bool(self.value)

    def __int__(self) -> int:
        return int(self.value)

    def __invert__(self) -> "Coordinate":
        return RelativeCoordinate(self.value)


class AbsoluteCoordinate(Coordinate):
    def __add__(self, other: Any) -> "AbsoluteCoordinate":
        c = Coordinate.from_thing(other)
        return AbsoluteCoordinate(self.value + c.value)

    def __sub__(self, other: Any) -> "AbsoluteCoordinate":
        c = Coordinate.from_thing(other)
        return AbsoluteCoordinate(self.value - c.value)

    def __mul__(self, other: Any) -> "AbsoluteCoordinate":
        c = Coordinate.from_thing(other)
        return AbsoluteCoordinate(self.value * c.value)

    def __neg__(self) -> "AbsoluteCoordinate":
        return AbsoluteCoordinate(-self.value)

    # @implements CommandToken
    def command_stringify(self) -> str:
        return f"{self.value:g}"


class RelativeCoordinate(Coordinate):
    def __add__(self, other: Any) -> "RelativeCoordinate":
        c = Coordinate.from_thing(other)
        return RelativeCoordinate(self.value + c.value)

    def __sub__(self, other: Any) -> "RelativeCoordinate":
        c = Coordinate.from_thing(other)
        return RelativeCoordinate(self.value - c.value)

    def __mul__(self, other: Any) -> "RelativeCoordinate":
        c = Coordinate.from_thing(other)
        return RelativeCoordinate(self.value * c.value)

    def __neg__(self) -> "RelativeCoordinate":
        return RelativeCoordinate(-self.value)

    # @implements CommandToken
    def command_stringify(self) -> str:
        return f"~" if self.value == 0 else f"~{self.value:g}"


class LocalCoordinate(Coordinate):
    def __add__(self, other: Any) -> "LocalCoordinate":
        c = Coordinate.from_thing(other)
        return LocalCoordinate(self.value + c.value)

    def __sub__(self, other: Any) -> "LocalCoordinate":
        c = Coordinate.from_thing(other)
        return LocalCoordinate(self.value - c.value)

    def __mul__(self, other: Any) -> "LocalCoordinate":
        c = Coordinate.from_thing(other)
        return LocalCoordinate(self.value * c.value)

    def __neg__(self) -> "LocalCoordinate":
        return LocalCoordinate(-self.value)

    # @implements CommandToken
    def command_stringify(self) -> str:
        return f"^" if self.value == 0 else f"^{self.value:g}"
