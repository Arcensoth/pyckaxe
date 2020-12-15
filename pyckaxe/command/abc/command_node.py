from typing import Any, Callable, Iterable, Optional, TypeVar

from pyckaxe.abc.from_thingable import FromThingable
from pyckaxe.command.abc.command import Command
from pyckaxe.command.debug_command import DebugCommand
from pyckaxe.command.raw_command import RawCommand


class CommandNode(Command):
    """ A single node in the parent-child command hierarchy. """

    def __init__(self, parent: "CommandNode" = None, token: Any = None):
        self._parent = parent
        self._token = token

    def _tokens(self) -> Iterable[Any]:
        yield from self._parent or ()
        yield self._token

    def __add__(self, other: Any) -> "CommandNode":
        # TODO Can we feasibly support concatenating two commands? #enhance
        if isinstance(other, str):
            return self._raw(other)
        if isinstance(other, (list, tuple)):
            return self._raw(*other)
        raise ValueError(f"Value cannot be added with {CommandNode.__name__}: {other}")

    def __invert__(self) -> "CommandNode":
        return self._debug

    def _raw(self, *tokens) -> RawCommand:
        return RawCommand(*tokens, parent=self)

    @property
    def _debug(self) -> DebugCommand:
        return DebugCommand(self)


CommandLiteralType = TypeVar("CommandLiteralType", bound="CommandNode")


class CommandLiteral(CommandNode):
    """ A node in the command hierarchy that always resolves to the same literal. """

    _LITERAL: Optional[str] = None

    def __init__(self, parent: CommandNode = None, literal: str = None):
        super().__init__(parent, literal or self._LITERAL)

    def __call__(self: CommandLiteralType) -> CommandLiteralType:
        return self


class CommandArgument(CommandNode):
    """ A node in the command hierarchy that resolves to the given argument. """

    _CONVERT: Optional[Callable] = None
    _TYPE: Optional[type] = None

    def __init__(self, parent: CommandNode = None, argument: Any = None):
        converter = self.__class__._CONVERT
        type_ = self.__class__._TYPE
        if converter:
            argument = converter(argument)
        if type_:
            if issubclass(type_, FromThingable):
                argument = type_.from_thing(argument)
            if not isinstance(argument, type_):
                raise ValueError(
                    f"Invalid command argument of type {argument.__class__.__name__}: {argument!r}"
                )
        super().__init__(parent, argument)
