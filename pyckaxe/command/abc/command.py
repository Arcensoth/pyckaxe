import abc
import typing


class Command(abc.ABC):
    """ A printable command that can be iterated over to retrieve its space-delimited tokens. """

    def __str__(self):
        return ' '.join(str(token) for token in self)

    def __iter__(self):
        return self._tokens()

    @abc.abstractmethod
    def _tokens(self) -> typing.Iterable[typing.Any]: ...


class CommandNode(Command):
    """ A single node in the parent-child command hierarchy. """

    def __init__(self, parent: 'CommandNode', token: typing.Any):
        self._parent = parent
        self._token = token

    def _tokens(self) -> typing.Iterable[typing.Any]:
        yield from self._parent
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
