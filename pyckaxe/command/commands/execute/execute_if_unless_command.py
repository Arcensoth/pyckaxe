from pyckaxe.command import commands as cc
from pyckaxe.command.abc.command import CommandLiteral, CommandNode


class ExecuteIfUnlessCommandMixin:
    @property
    def block(self: CommandNode) -> "ExecuteIfUnlessBlockCommand":
        return cc.ExecuteIfUnlessBlockCommand(self)

    @property
    def blocks(self: CommandNode) -> "ExecuteIfUnlessBlocksCommand":
        return cc.ExecuteIfUnlessBlocksCommand(self)

    @property
    def entity(self: CommandNode) -> "ExecuteIfUnlessEntityCommand":
        return cc.ExecuteIfUnlessEntityCommand(self)

    @property
    def score(self: CommandNode) -> "ExecuteIfUnlessScoreCommand":
        return cc.ExecuteIfUnlessScoreCommand(self)


class ExecuteIfCommand(CommandLiteral, ExecuteIfUnlessCommandMixin):
    _LITERAL = "if"


class ExecuteUnlessCommand(CommandLiteral, ExecuteIfUnlessCommandMixin):
    _LITERAL = "unless"
