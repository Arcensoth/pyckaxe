from pyckaxe.command.abc.command import CommandArgument, CommandLiteral, CommandNode
from pyckaxe.types import BlockPredicate, CommandTarget, Position


class ExecuteCommandMixin:
    @property
    def as_(self: CommandNode) -> "ExecuteAsCommand":
        return ExecuteAsCommand(self)

    @property
    def at(self: CommandNode) -> "ExecuteAtCommand":
        return ExecuteAtCommand(self)

    @property
    def if_(self: CommandNode) -> "ExecuteIfCommand":
        return ExecuteIfCommand(self)

    @property
    def unless(self: CommandNode) -> "ExecuteUnlessCommand":
        return ExecuteUnlessCommand(self)

    @property
    def in_(self: CommandNode) -> "ExecuteInCommand":
        return ExecuteInCommand(self)

    @property
    def run(self: CommandNode) -> "ExecuteRunCommand":
        # TODO Can we make circular redirects work without this hack?
        from pyckaxe.command.commands.execute_run import ExecuteRunCommand

        return ExecuteRunCommand(self)


class ExecuteIfUnlessCommandMixin:
    @property
    def block(self: CommandNode) -> "ExecuteIfUnlessBlockCommand":
        return ExecuteIfUnlessBlockCommand(self)

    @property
    def blocks(self: CommandNode) -> "ExecuteIfUnlessBlocksCommand":
        return ExecuteIfUnlessBlocksCommand(self)

    @property
    def entity(self: CommandNode) -> "ExecuteIfUnlessEntityCommand":
        return ExecuteIfUnlessEntityCommand(self)

    @property
    def score(self: CommandNode) -> "ExecuteIfUnlessScoreCommand":
        return ExecuteIfUnlessScoreCommand(self)


class ExecuteCommand(CommandLiteral, ExecuteCommandMixin):
    _LITERAL = "execute"


class ExecuteAsCommand(CommandLiteral):
    _LITERAL = "as"

    def __call__(self, targets: CommandTarget) -> "ExecuteAsTargetsCommand":
        return self.targets(targets)

    def targets(self, targets: CommandTarget) -> "ExecuteAsTargetsCommand":
        return ExecuteAsTargetsCommand(self, targets)


class ExecuteAtCommand(CommandLiteral):
    _LITERAL = "at"

    def __call__(self, targets: CommandTarget) -> "ExecuteAtTargetsCommand":
        return self.targets(targets)

    def targets(self, targets: CommandTarget) -> "ExecuteAtTargetsCommand":
        return ExecuteAtTargetsCommand(self, targets)


class ExecuteAsTargetsCommand(CommandArgument, ExecuteCommandMixin):
    pass


class ExecuteAtTargetsCommand(CommandArgument, ExecuteCommandMixin):
    pass


class ExecuteIfCommand(CommandLiteral, ExecuteIfUnlessCommandMixin):
    _LITERAL = "if"


class ExecuteUnlessCommand(CommandLiteral, ExecuteIfUnlessCommandMixin):
    _LITERAL = "unless"


class ExecuteIfUnlessBlockCommand(CommandLiteral):
    _LITERAL = "block"

    def __call__(
        self, position: Position, block: BlockPredicate
    ) -> "ExecuteIfUnlessBlockPositionBlockCommand":
        return self.position(position).block(block)

    def position(self, position: Position) -> "ExecuteIfUnlessBlockPositionCommand":
        return ExecuteIfUnlessBlockPositionCommand(self, position)


class ExecuteIfUnlessBlockPositionCommand(CommandArgument):
    def block(
        self, block: BlockPredicate
    ) -> "ExecuteIfUnlessBlockPositionBlockCommand":
        return ExecuteIfUnlessBlockPositionBlockCommand(self, block)


class ExecuteIfUnlessBlockPositionBlockCommand(CommandArgument, ExecuteCommandMixin):
    pass


class ExecuteIfUnlessBlocksCommand(CommandLiteral):
    _LITERAL = "blocks"

    # TODO finish execute if/unless blocks


class ExecuteIfUnlessEntityCommand(CommandLiteral):
    _LITERAL = "entity"

    # TODO finish execute if/unless entity


class ExecuteIfUnlessScoreCommand(CommandLiteral):
    _LITERAL = "score"

    # TODO finish execute if/unless score


class ExecuteInCommand(CommandLiteral):
    _LITERAL = "in"

    @property
    def overworld(self) -> "ExecuteInOverworldCommand":
        return ExecuteInOverworldCommand(self)

    @property
    def the_end(self) -> "ExecuteInTheEndCommand":
        return ExecuteInTheEndCommand(self)

    @property
    def the_nether(self) -> "ExecuteInTheNetherCommand":
        return ExecuteInTheNetherCommand(self)


class ExecuteInOverworldCommand(CommandLiteral, ExecuteCommandMixin):
    _LITERAL = "overworld"


class ExecuteInTheEndCommand(CommandLiteral, ExecuteCommandMixin):
    _LITERAL = "the_end"


class ExecuteInTheNetherCommand(CommandLiteral, ExecuteCommandMixin):
    _LITERAL = "the_nether"
