from typing import Union

from pyckaxe.command.abc.command_node import CommandArgument, CommandLiteral
from pyckaxe.pack.resource.function.function_location import FunctionLocation

FunctionArgument = Union[FunctionLocation, str]


class FunctionCommand(CommandLiteral):
    _LITERAL = "function"

    def __call__(self, name: FunctionArgument) -> "FunctionNameCommand":
        return self.name(name)

    def name(self, name: FunctionArgument) -> "FunctionNameCommand":
        return FunctionNameCommand(self, name)


class FunctionNameCommand(CommandArgument):
    pass
