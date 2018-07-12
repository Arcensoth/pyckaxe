from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.types import TextComponent


class TellrawCommand(CommandLiteral):
    _LITERAL = 'tellraw'

    def __call__(self, targets: str, message: TextComponent) -> 'TellrawTargetsMessageCommand':
        return self.targets(targets).message(message)

    def targets(self, targets: str) -> 'TellrawTargetsCommand':
        return TellrawTargetsCommand(self, targets)


class TellrawTargetsCommand(CommandArgument):
    def message(self, message: TextComponent) -> 'TellrawTargetsMessageCommand':
        return TellrawTargetsMessageCommand(self, message)


class TellrawTargetsMessageCommand(CommandArgument):
    pass
