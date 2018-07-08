from pyckaxe.command.abc.command import CommandArguments, CommandLiteral


class ClearCommand(CommandLiteral):
    _LITERAL = 'clear'

    def __call__(
            self, targets: str = None, item: str = None, max_count: int = None
    ) -> 'ClearTargetsItemMaxCountCommand':
        return ClearTargetsItemMaxCountCommand(parent=self, args=(targets, item, max_count))


class ClearTargetsItemMaxCountCommand(CommandArguments):
    @property
    def targets(self) -> str:
        return self._args[0]

    @property
    def item(self) -> str:
        return self._args[1]

    @property
    def max_count(self) -> int:
        return self._args[2]
