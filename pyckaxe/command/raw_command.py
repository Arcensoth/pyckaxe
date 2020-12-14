from typing import Any, Iterable

from pyckaxe.command.abc.command import CommandNode
from pyckaxe.command.abc.command_token import CommandToken


class RawCommand(CommandNode):
    def __init__(self, command_string: str, parent: "CommandNode" = None):
        super().__init__(parent, command_string)

    @staticmethod
    def from_tokens(*tokens: Iterable[CommandToken]) -> "RawCommand":
        str_tokens = (
            token.command_stringify() if isinstance(token, CommandToken) else str(token)
            for token in tokens
        )
        command_string = " ".join(str_tokens)
        return RawCommand(command_string)
