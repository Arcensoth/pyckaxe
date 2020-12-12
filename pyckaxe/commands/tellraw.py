from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.types import CommandTarget, TextComponent


class TellrawCommand(CommandLiteral):
    _LITERAL = "tellraw"

    def __call__(
        self, targets: CommandTarget, message: TextComponent
    ) -> "TellrawTargetsMessageCommand":
        return self.targets(targets).message(message)

    def targets(self, targets: CommandTarget) -> "TellrawTargetsCommand":
        return TellrawTargetsCommand(self, targets)


class TellrawTargetsCommand(CommandArgument):
    def message(self, message: TextComponent) -> "TellrawTargetsMessageCommand":
        return TellrawTargetsMessageCommand(self, message)


class TellrawTargetsMessageCommand(CommandArgument):
    pass
