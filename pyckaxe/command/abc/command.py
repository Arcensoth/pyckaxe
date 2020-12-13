from abc import ABC, abstractmethod
from typing import Any, Iterable, Optional, Type

from pyckaxe.abc.from_thingable import FromThingable
from pyckaxe.command.abc.command_token import CommandToken


class Command(ABC):
    """ A printable command that can be iterated over to retrieve its space-delimited tokens. """

    def __str__(self):
        return " ".join(self._convert(token) for token in self._tokens())

    def __iter__(self):
        return self._tokens()

    @staticmethod
    def _convert(token) -> str:
        if isinstance(token, CommandToken):
            return token.command_stringify()
        if isinstance(token, bool):
            return "true" if token else "false"
        if token is None:
            raise ValueError("Cannot stringify None into a command token")
        return str(token)

    @abstractmethod
    def _tokens(self) -> Iterable[Any]:
        """ Yield command tokens as literals or arguments. """


class CommandNode(Command):
    """ A single node in the parent-child command hierarchy. """

    def __init__(self, parent: "CommandNode" = None, token: Any = None):
        self._parent = parent
        self._token = token

    def _tokens(self) -> Iterable[Any]:
        yield from self._parent or ()
        yield self._token


class CommandLiteral(CommandNode):
    """ A node in the command hierarchy that always resolves to the same literal. """

    _LITERAL: Optional[str] = None

    def __init__(self, parent: CommandNode = None, literal: str = None):
        super().__init__(parent, literal or self._LITERAL)


class CommandArgument(CommandNode):
    """ A node in the command hierarchy that resolves to the given argument. """

    _TYPE: Optional[type] = None

    def __init__(self, parent: CommandNode = None, argument: Any = None):
        if self._TYPE:
            if issubclass(self._TYPE, FromThingable):
                argument = self._TYPE.from_thing(argument)
            if not isinstance(argument, self._TYPE):
                raise ValueError(
                    f"Invalid command argument of type {self._TYPE.__name__}: {argument}"
                )
        super().__init__(parent, argument)
