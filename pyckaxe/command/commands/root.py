import typing

from pyckaxe.command.abc.command import Command
from pyckaxe.command.commands.clear import ClearCommand
from pyckaxe.command.commands.execute import ExecuteCommand
from pyckaxe.command.commands.say import SayCommand
from pyckaxe.command.commands.setblock import SetblockCommand
from pyckaxe.command.commands.tag import TagCommand
from pyckaxe.command.commands.teleport import TeleportCommand
from pyckaxe.command.commands.time import TimeCommand
from pyckaxe.command.commands.tp import TpCommand


class RootCommandMixin:
    @property
    def clear(self: Command) -> ClearCommand:
        return ClearCommand(parent=self)

    @property
    def execute(self: Command) -> ExecuteCommand:
        return ExecuteCommand(parent=self)

    @property
    def say(self: Command) -> SayCommand:
        return SayCommand(parent=self)

    @property
    def setblock(self: Command) -> SetblockCommand:
        return SetblockCommand(parent=self)

    @property
    def tag(self: Command) -> TagCommand:
        return TagCommand(parent=self)

    @property
    def teleport(self: Command) -> TeleportCommand:
        return TeleportCommand(parent=self)

    @property
    def time(self: Command) -> TimeCommand:
        return TimeCommand(parent=self)

    @property
    def tp(self: Command) -> TpCommand:
        return TpCommand(parent=self)


class RootCommand(Command, RootCommandMixin):
    def _tokens(self) -> typing.Iterable[typing.Any]:
        yield from ()
