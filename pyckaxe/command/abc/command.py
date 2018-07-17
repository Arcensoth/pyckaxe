import abc
import typing


class Command(abc.ABC):
    """ A printable command that can be iterated over to retrieve its space-delimited tokens. """

    def __str__(self):
        return ' '.join(self._convert(token) for token in self)

    def __iter__(self):
        return self._tokens()

    @staticmethod
    def _convert(token) -> str:
        if isinstance(token, bool):
            return 'true' if token else 'false'
        elif token is None:
            raise ValueError('Cannot stringify None into a command token')
        return str(token)

    @abc.abstractmethod
    def _tokens(self) -> typing.Iterable[typing.Any]: ...


class CommandNode(Command):
    """ A single node in the parent-child command hierarchy. """

    def __init__(self, parent: 'CommandNode' = None, token: typing.Any = None):
        self._parent = parent
        self._token = token

    def _tokens(self) -> typing.Iterable[typing.Any]:
        yield from self._parent or ()
        yield self._token


class CommandLiteral(CommandNode):
    """ A node in the command hierarchy that always resolves to the same literal. """

    _LITERAL = None

    def __init__(self, parent: CommandNode, literal: str = None):
        super().__init__(parent, literal or self._LITERAL)


class CommandArgument(CommandNode):
    """ A node in the command hierarchy that resolves to the given argument. """

    def __init__(self, parent: CommandNode, argument: typing.Any):
        super().__init__(parent, argument)
