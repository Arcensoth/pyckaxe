from pyckaxe.command.abc.command import CommandArgument, CommandLiteral


class SayCommand(CommandLiteral):
    _LITERAL = 'say'

    def __call__(self, message: str) -> 'SayMessageCommand':
        return SayMessageCommand(self, message)

    def message(self, message: str) -> 'SayMessageCommand':
        return SayMessageCommand(self, message)


class SayMessageCommand(CommandArgument):
    pass
