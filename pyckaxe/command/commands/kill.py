from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.types import CommandTarget


class KillCommand(CommandLiteral):
    _LITERAL = "kill"

    def __call__(self, targets: CommandTarget) -> "KillTargetsCommand":
        return self.targets(targets)

    def targets(self, targets: CommandTarget) -> "KillTargetsCommand":
        return KillTargetsCommand(self, targets)


class KillTargetsCommand(CommandArgument):
    pass
