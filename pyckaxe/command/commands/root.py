import typing

from pyckaxe.command.abc.command import CommandNode
from pyckaxe.command.commands.clear import ClearCommand
from pyckaxe.command.commands.effect import EffectCommand
from pyckaxe.command.commands.execute import ExecuteCommand
from pyckaxe.command.commands.say import SayCommand
from pyckaxe.command.commands.setblock import SetblockCommand
from pyckaxe.command.commands.tag import TagCommand
from pyckaxe.command.commands.teleport import TeleportCommand
from pyckaxe.command.commands.time import TimeCommand
from pyckaxe.command.commands.tp import TpCommand
from pyckaxe.command.commands.trigger import TriggerCommand


class RootCommandMixin:
    @property
    def clear(self: CommandNode) -> ClearCommand:
        return ClearCommand(self)

    @property
    def effect(self: CommandNode) -> EffectCommand:
        return EffectCommand(self)

    @property
    def execute(self: CommandNode) -> ExecuteCommand:
        return ExecuteCommand(self)

    @property
    def say(self: CommandNode) -> SayCommand:
        return SayCommand(self)

    @property
    def setblock(self: CommandNode) -> SetblockCommand:
        return SetblockCommand(self)

    @property
    def tag(self: CommandNode) -> TagCommand:
        return TagCommand(self)

    @property
    def teleport(self: CommandNode) -> TeleportCommand:
        return TeleportCommand(self)

    @property
    def time(self: CommandNode) -> TimeCommand:
        return TimeCommand(self)

    @property
    def tp(self: CommandNode) -> TpCommand:
        return TpCommand(self)

    @property
    def trigger(self: CommandNode) -> TriggerCommand:
        return TriggerCommand(self)


class RootCommand(CommandNode, RootCommandMixin):
    def __init__(self):
        super().__init__(None, None)

    def _tokens(self) -> typing.Iterable[typing.Any]:
        yield from ()
