from pyckaxe.command.abc.command import CommandLiteral
from pyckaxe.command.commands.execute.execute_command_mixin import ExecuteCommandMixin


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
