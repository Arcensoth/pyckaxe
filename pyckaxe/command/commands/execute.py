from pyckaxe.command.abc.command import Command, CommandArguments, CommandLiteral


class ExecuteCommandMixin:
    @property
    def as_(self: Command) -> 'ExecuteAsCommand':
        return ExecuteAsCommand(parent=self)

    @property
    def at(self: Command) -> 'ExecuteAtCommand':
        return ExecuteAtCommand(parent=self)

    @property
    def if_(self: Command) -> 'ExecuteIfCommand':
        return ExecuteIfCommand(parent=self)

    @property
    def unless(self: Command) -> 'ExecuteUnlessCommand':
        return ExecuteUnlessCommand(parent=self)

    @property
    def run(self: Command) -> 'ExecuteRunCommand':
        # TODO Can we make circular redirects work without this hack?
        from pyckaxe.command.commands.execute_run import ExecuteRunCommand
        return ExecuteRunCommand(parent=self)


class ExecuteIfUnlessCommandMixin:
    @property
    def block(self: Command) -> 'ExecuteIfUnlessBlockCommand':
        return ExecuteIfUnlessBlockCommand(parent=self)

    @property
    def blocks(self: Command) -> 'ExecuteIfUnlessBlocksCommand':
        return ExecuteIfUnlessBlocksCommand(parent=self)

    @property
    def entity(self: Command) -> 'ExecuteIfUnlessEntityCommand':
        return ExecuteIfUnlessEntityCommand(parent=self)

    @property
    def score(self: Command) -> 'ExecuteIfUnlessScoreCommand':
        return ExecuteIfUnlessScoreCommand(parent=self)


class ExecuteCommand(CommandLiteral, ExecuteCommandMixin):
    _LITERAL = 'execute'


class ExecuteAsCommand(CommandLiteral):
    _LITERAL = 'as'

    def __call__(self, targets: str) -> 'ExecuteAsTargetsCommand':
        return ExecuteAsTargetsCommand(parent=self, args=(targets,))

    def targets(self, targets: str) -> 'ExecuteAsTargetsCommand':
        return ExecuteAsTargetsCommand(parent=self, args=(targets,))


class ExecuteAtCommand(CommandLiteral):
    _LITERAL = 'at'

    def __call__(self, targets: str) -> 'ExecuteAtTargetsCommand':
        return ExecuteAtTargetsCommand(parent=self, args=(targets,))

    def targets(self, targets: str) -> 'ExecuteAtTargetsCommand':
        return ExecuteAtTargetsCommand(parent=self, args=(targets,))


class ExecuteAsTargetsCommand(CommandArguments, ExecuteCommandMixin):
    pass


class ExecuteAtTargetsCommand(CommandArguments, ExecuteCommandMixin):
    pass


class ExecuteIfCommand(CommandLiteral, ExecuteIfUnlessCommandMixin):
    _LITERAL = 'if'


class ExecuteUnlessCommand(CommandLiteral, ExecuteIfUnlessCommandMixin):
    _LITERAL = 'unless'


class ExecuteIfUnlessBlockCommand(CommandLiteral):
    _LITERAL = 'block'

    def __call__(self, position: str, block: str) -> 'ExecuteIfUnlessBlockPositionBlockCommand':
        return ExecuteIfUnlessBlockPositionBlockCommand(parent=self, args=(position, block))

    def position(self, position: str) -> 'ExecuteIfUnlessBlockPositionCommand':
        return ExecuteIfUnlessBlockPositionCommand(parent=self, args=(position,))


class ExecuteIfUnlessBlockPositionCommand(CommandArguments):
    def block(self, block: str) -> 'ExecuteIfUnlessBlockPositionBlockCommand':
        return ExecuteIfUnlessBlockPositionBlockCommand(parent=self._parent, args=(*self._args, block))


class ExecuteIfUnlessBlockPositionBlockCommand(CommandArguments, ExecuteCommandMixin):
    pass


class ExecuteIfUnlessBlocksCommand(CommandLiteral):
    _LITERAL = 'blocks'


class ExecuteIfUnlessEntityCommand(CommandLiteral):
    _LITERAL = 'entity'


class ExecuteIfUnlessScoreCommand(CommandLiteral):
    _LITERAL = 'score'
