from pyckaxe.command.abc.command import CommandArgument, CommandLiteral, CommandNode


class ExecuteCommandMixin:
    @property
    def as_(self: CommandNode) -> 'ExecuteAsCommand':
        return ExecuteAsCommand(self)

    @property
    def at(self: CommandNode) -> 'ExecuteAtCommand':
        return ExecuteAtCommand(self)

    @property
    def if_(self: CommandNode) -> 'ExecuteIfCommand':
        return ExecuteIfCommand(self)

    @property
    def unless(self: CommandNode) -> 'ExecuteUnlessCommand':
        return ExecuteUnlessCommand(self)

    @property
    def run(self: CommandNode) -> 'ExecuteRunCommand':
        # TODO Can we make circular redirects work without this hack?
        from pyckaxe.command.commands.execute_run import ExecuteRunCommand
        return ExecuteRunCommand(self)


class ExecuteIfUnlessCommandMixin:
    @property
    def block(self: CommandNode) -> 'ExecuteIfUnlessBlockCommand':
        return ExecuteIfUnlessBlockCommand(self)

    @property
    def blocks(self: CommandNode) -> 'ExecuteIfUnlessBlocksCommand':
        return ExecuteIfUnlessBlocksCommand(self)

    @property
    def entity(self: CommandNode) -> 'ExecuteIfUnlessEntityCommand':
        return ExecuteIfUnlessEntityCommand(self)

    @property
    def score(self: CommandNode) -> 'ExecuteIfUnlessScoreCommand':
        return ExecuteIfUnlessScoreCommand(self)


class ExecuteCommand(CommandLiteral, ExecuteCommandMixin):
    _LITERAL = 'execute'


class ExecuteAsCommand(CommandLiteral):
    _LITERAL = 'as'

    def __call__(self, targets: str) -> 'ExecuteAsTargetsCommand':
        return self.targets(targets)

    def targets(self, targets: str) -> 'ExecuteAsTargetsCommand':
        return ExecuteAsTargetsCommand(self, targets)


class ExecuteAtCommand(CommandLiteral):
    _LITERAL = 'at'

    def __call__(self, targets: str) -> 'ExecuteAtTargetsCommand':
        return self.targets(targets)

    def targets(self, targets: str) -> 'ExecuteAtTargetsCommand':
        return ExecuteAtTargetsCommand(self, targets)


class ExecuteAsTargetsCommand(CommandArgument, ExecuteCommandMixin):
    pass


class ExecuteAtTargetsCommand(CommandArgument, ExecuteCommandMixin):
    pass


class ExecuteIfCommand(CommandLiteral, ExecuteIfUnlessCommandMixin):
    _LITERAL = 'if'


class ExecuteUnlessCommand(CommandLiteral, ExecuteIfUnlessCommandMixin):
    _LITERAL = 'unless'


class ExecuteIfUnlessBlockCommand(CommandLiteral):
    _LITERAL = 'block'

    def __call__(self, position: str, block: str) -> 'ExecuteIfUnlessBlockPositionBlockCommand':
        return self.position(position).block(block)

    def position(self, position: str) -> 'ExecuteIfUnlessBlockPositionCommand':
        return ExecuteIfUnlessBlockPositionCommand(self, position)


class ExecuteIfUnlessBlockPositionCommand(CommandArgument):
    def block(self, block: str) -> 'ExecuteIfUnlessBlockPositionBlockCommand':
        return ExecuteIfUnlessBlockPositionBlockCommand(self, block)


class ExecuteIfUnlessBlockPositionBlockCommand(CommandArgument, ExecuteCommandMixin):
    pass


class ExecuteIfUnlessBlocksCommand(CommandLiteral):
    _LITERAL = 'blocks'


class ExecuteIfUnlessEntityCommand(CommandLiteral):
    _LITERAL = 'entity'


class ExecuteIfUnlessScoreCommand(CommandLiteral):
    _LITERAL = 'score'
