from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.types import GreedyString


class SayCommand(CommandLiteral):
    _LITERAL = "say"

    def __call__(self, message: GreedyString) -> "SayMessageCommand":
        return self.message(message)

    def message(self, message: GreedyString) -> "SayMessageCommand":
        return SayMessageCommand(self, message)


class SayMessageCommand(CommandArgument):
    pass
