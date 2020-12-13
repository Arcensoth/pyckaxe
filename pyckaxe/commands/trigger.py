from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.types import ScoreboardObjective


class TriggerObjectiveAddSetValueCommandMixin:
    def __call__(self, value: int):
        return self.value(value)

    def value(self, value: int) -> "TriggerObjectiveAddSetValueCommand":
        return TriggerObjectiveAddSetValueCommand(self, value)


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


class TriggerObjectiveAddCommand(CommandLiteral, TriggerObjectiveAddSetValueCommandMixin):
    _LITERAL = "add"


class TriggerObjectiveSetCommand(CommandLiteral, TriggerObjectiveAddSetValueCommandMixin):
    _LITERAL = "set"


class TriggerObjectiveAddSetValueCommand(CommandArgument):
    pass
