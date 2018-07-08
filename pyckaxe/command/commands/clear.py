from pyckaxe.command.abc.command import CommandArguments, CommandLiteral


class ClearCommand(CommandLiteral):
    _LITERAL = 'clear'

    def __call__(
            self, targets: str = None, item: str = None, max_count: int = None
    ) -> 'ClearTargetsItemMaxCountCommand':
        return ClearTargetsItemMaxCountCommand(parent=self, args=(targets, item, max_count))

    def targets(self, targets: str) -> 'ClearTargetsCommand':
        return ClearTargetsCommand(parent=self, args=(targets,))


class ClearTargetsCommand(CommandArguments):
    def item(self, item: str) -> 'ClearTargetsItemCommand':
        return ClearTargetsItemCommand(parent=self._parent, args=(*self._args, item))


class ClearTargetsItemCommand(CommandArguments):
    def max_count(self, max_count: str) -> 'ClearTargetsItemMaxCountCommand':
        return ClearTargetsItemMaxCountCommand(parent=self._parent, args=(*self._args, max_count))


class ClearTargetsItemMaxCountCommand(CommandArguments):
    pass
