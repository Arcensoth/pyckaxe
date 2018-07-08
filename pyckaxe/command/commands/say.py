from pyckaxe.command.abc.command import CommandArguments, CommandLiteral


class SayCommand(CommandLiteral):
    _LITERAL = 'say'

    def __call__(self, message: str = None) -> 'SayMessageCommand':
        return SayMessageCommand(parent=self, args=(message,))

    def message(self, message: str) -> 'SayMessageCommand':
        return SayMessageCommand(parent=self, args=(message,))


class SayMessageCommand(CommandArguments):
    pass
