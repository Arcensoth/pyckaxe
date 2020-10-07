from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.types import FunctionResourceLocation


class FunctionCommand(CommandLiteral):
    _LITERAL = "function"

    def __call__(self, name: FunctionResourceLocation) -> "FunctionNameCommand":
        return self.name(name)

    def name(self, name: FunctionResourceLocation) -> "FunctionNameCommand":
        return FunctionNameCommand(self, name)


class FunctionNameCommand(CommandArgument):
    pass
