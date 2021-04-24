from __future__ import annotations

from pyckaxe.lib import (
    CommandArgument,
    CommandLiteral,
    command_argument,
    command_literal,
)

# TODO Use FunctionLocation argument. #enhance


@command_literal("function")
class FunctionCommand(CommandLiteral):
    def __call__(self, name: str) -> FunctionNameCommand:
        return self.name(name)

    def name(self, name: str) -> FunctionNameCommand:
        return FunctionNameCommand(self, name)


@command_argument(str)
class FunctionNameCommand(CommandArgument[str]):
    pass
