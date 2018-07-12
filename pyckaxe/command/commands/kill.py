from pyckaxe.command.abc.command import CommandArgument, CommandLiteral


class KillCommand(CommandLiteral):
    _LITERAL = 'kill'

    def __call__(self, targets: str) -> 'KillTargetsCommand':
        return self.targets(targets)

    def targets(self, targets: str) -> 'KillTargetsCommand':
        return KillTargetsCommand(self, targets)


class KillTargetsCommand(CommandArgument):
    pass
