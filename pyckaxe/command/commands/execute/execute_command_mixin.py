from pyckaxe.command import commands as cc
from pyckaxe.command.abc.command import CommandNode


class ExecuteCommandMixin:
    @property
    def as_(self: CommandNode) -> "ExecuteAsCommand":
        return cc.ExecuteAsCommand(self)

    @property
    def at(self: CommandNode) -> "ExecuteAtCommand":
        return cc.ExecuteAtCommand(self)

    @property
    def if_(self: CommandNode) -> "ExecuteIfCommand":
        return cc.ExecuteIfCommand(self)

    @property
    def unless(self: CommandNode) -> "ExecuteUnlessCommand":
        return cc.ExecuteUnlessCommand(self)

    @property
    def in_(self: CommandNode) -> "ExecuteInCommand":
        return cc.ExecuteInCommand(self)

    @property
    def run(self: CommandNode) -> "ExecuteRunCommand":
        return cc.ExecuteRunCommand(self)
