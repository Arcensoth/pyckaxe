from pyckaxe.command.abc.command import CommandArgument, CommandLiteral


class ClearCommand(CommandLiteral):
    _LITERAL = 'clear'

    def __call__(self, targets: str, item: str, max_count: int) -> 'ClearTargetsItemMaxCountCommand':
        return self.targets(targets).item(item).max_count(max_count)

    def targets(self, targets: str) -> 'ClearTargetsCommand':
        return ClearTargetsCommand(self, targets)


class ClearTargetsCommand(CommandArgument):
    def item(self, item: str) -> 'ClearTargetsItemCommand':
        return ClearTargetsItemCommand(self, item)


class ClearTargetsItemCommand(CommandArgument):
    def max_count(self, max_count: int) -> 'ClearTargetsItemMaxCountCommand':
        return ClearTargetsItemMaxCountCommand(self, max_count)


class ClearTargetsItemMaxCountCommand(CommandArgument):
    pass
