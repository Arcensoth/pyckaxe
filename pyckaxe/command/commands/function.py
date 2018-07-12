from pyckaxe.command.abc.command import CommandArgument, CommandLiteral


class FunctionCommand(CommandLiteral):
    _LITERAL = 'function'

    def __call__(self, name: str) -> 'FunctionNameCommand':
        return self.name(name)

    def name(self, name: str) -> 'FunctionNameCommand':
        return FunctionNameCommand(self, name)


class FunctionNameCommand(CommandArgument):
    pass
