from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.types import ScoreboardObjective


class TriggerCommand(CommandLiteral):
    _LITERAL = "trigger"

    def __call__(self, objective: ScoreboardObjective) -> "TriggerObjectiveCommand":
        return self.objective(objective)

    def objective(self, objective: ScoreboardObjective) -> "TriggerObjectiveCommand":
        return TriggerObjectiveCommand(self, objective)


class TriggerObjectiveCommand(CommandArgument):
    @property
    def add(self) -> "TriggerObjectiveAddCommand":
        return TriggerObjectiveAddCommand(self)

    @property
    def set(self) -> "TriggerObjectiveSetCommand":
        return TriggerObjectiveSetCommand(self)


class TriggerObjectiveAddSetValueCommandLiteralBase(CommandLiteral):
    def __call__(self, value: int):
        return self.value(value)

    def value(self, value: int) -> "TriggerObjectiveAddSetValueCommand":
        return TriggerObjectiveAddSetValueCommand(self, value)


class TriggerObjectiveAddCommand(TriggerObjectiveAddSetValueCommandLiteralBase):
    _LITERAL = "add"


class TriggerObjectiveSetCommand(TriggerObjectiveAddSetValueCommandLiteralBase):
    _LITERAL = "set"


class TriggerObjectiveAddSetValueCommand(CommandArgument):
    pass
