from pyckaxe.command.abc.command import CommandArgument, CommandLiteral, CommandNode


class TriggerObjectiveAddSetValueCommandMixin:
    def __call__(self, value: int):
        return self.value(value)

    def value(self: CommandNode, value: int) -> 'TriggerObjectiveAddSetValueCommand':
        return TriggerObjectiveAddSetValueCommand(self, value)


class TriggerCommand(CommandLiteral):
    _LITERAL = 'trigger'

    def __call__(self, objective: str) -> 'TriggerObjectiveCommand':
        return self.objective(objective)

    def objective(self, objective: str) -> 'TriggerObjectiveCommand':
        return TriggerObjectiveCommand(self, objective)


class TriggerObjectiveCommand(CommandArgument):
    @property
    def add(self) -> 'TriggerObjectiveAddCommand':
        return TriggerObjectiveAddCommand(self)

    @property
    def set(self) -> 'TriggerObjectiveSetCommand':
        return TriggerObjectiveSetCommand(self)


class TriggerObjectiveAddCommand(CommandLiteral, TriggerObjectiveAddSetValueCommandMixin):
    _LITERAL = 'add'


class TriggerObjectiveSetCommand(CommandLiteral, TriggerObjectiveAddSetValueCommandMixin):
    _LITERAL = 'set'


class TriggerObjectiveAddSetValueCommand(CommandArgument):
    pass
