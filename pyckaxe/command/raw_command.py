from typing import Any, Iterable

from pyckaxe.command.abc.command import Command
from pyckaxe.command.abc.command_token import CommandToken


class RawCommand(Command):
    def __init__(self, command_string: str):
        self._command_string = command_string

    def _tokens(self) -> Iterable[Any]:
        yield self._command_string

    @staticmethod
    def from_tokens(*tokens: Iterable[CommandToken]) -> "Command":
        str_tokens = (
            token.command_stringify() if isinstance(token, CommandToken) else str(token)
            for token in tokens
        )
        command_string = " ".join(str_tokens)
        return RawCommand(command_string)
