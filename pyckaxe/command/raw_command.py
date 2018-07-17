import typing

from pyckaxe.command.abc.command import Command


class RawCommand(Command):
    def __init__(self, command_string: str):
        self._command_string = command_string

    def _tokens(self) -> typing.Iterable[typing.Any]:
        yield self._command_string
