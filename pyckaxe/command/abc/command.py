import abc
import typing


class Command(abc.ABC):
    """ Base object representing a literal command node. """

    def __init__(self, parent: 'Command' = None):
        self._parent = parent

    def __str__(self):
        return ' '.join(str(token) for token in self._tokens() if token is not None)

    @abc.abstractmethod
    def _tokens(self) -> typing.Iterable[typing.Any]: ...


class CommandLiteral(Command):
    _LITERAL = None

    def _tokens(self) -> typing.Iterable[typing.Any]:
        yield from self._parent._tokens()
        yield self._LITERAL


class CommandArguments(Command):
    def __init__(self, parent: Command = None, args: tuple = ()):
        super().__init__(parent)
        self._args = args

    def _tokens(self) -> typing.Iterable[typing.Any]:
        yield from self._parent._tokens()
        yield from self._args
