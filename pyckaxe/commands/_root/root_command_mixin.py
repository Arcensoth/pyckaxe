from pyckaxe.command.abc.command import CommandNode
from pyckaxe.commands.advancement import AdvancementCommand
from pyckaxe.commands.clear import ClearCommand
from pyckaxe.commands.clone import CloneCommand
from pyckaxe.commands.data import DataCommand
from pyckaxe.commands.effect import EffectCommand
from pyckaxe.commands.execute import ExecuteCommand
from pyckaxe.commands.fill import FillCommand
from pyckaxe.commands.function import FunctionCommand
from pyckaxe.commands.give import GiveCommand
from pyckaxe.commands.kill import KillCommand
from pyckaxe.commands.playsound import PlaysoundCommand
from pyckaxe.commands.replaceitem import ReplaceitemCommand
from pyckaxe.commands.say import SayCommand
from pyckaxe.commands.scoreboard import ScoreboardCommand
from pyckaxe.commands.setblock import SetblockCommand
from pyckaxe.commands.summon import SummonCommand
from pyckaxe.commands.tag import TagCommand
from pyckaxe.commands.teleport import TeleportCommand
from pyckaxe.commands.tellraw import TellrawCommand
from pyckaxe.commands.time import TimeCommand
from pyckaxe.commands.tp import TpCommand
from pyckaxe.commands.trigger import TriggerCommand


class RootCommandMixin:
    @property
    def advancement(self: CommandNode) -> AdvancementCommand:
        return AdvancementCommand(self)

    @property
    def clear(self: CommandNode) -> ClearCommand:
        return ClearCommand(self)

    @property
    def clone(self: CommandNode) -> CloneCommand:
        return CloneCommand(self)

    @property
    def data(self: CommandNode) -> DataCommand:
        return DataCommand(self)

    @property
    def effect(self: CommandNode) -> EffectCommand:
        return EffectCommand(self)

    @property
    def execute(self: CommandNode) -> ExecuteCommand:
        return ExecuteCommand(self)

    @property
    def fill(self: CommandNode) -> FillCommand:
        return FillCommand(self)

    @property
    def function(self: CommandNode) -> FunctionCommand:
        return FunctionCommand(self)

    @property
    def give(self: CommandNode) -> GiveCommand:
        return GiveCommand(self)

    @property
    def kill(self: CommandNode) -> KillCommand:
        return KillCommand(self)

    @property
    def playsound(self: CommandNode) -> PlaysoundCommand:
        return PlaysoundCommand(self)

    @property
    def replaceitem(self: CommandNode) -> ReplaceitemCommand:
        return ReplaceitemCommand(self)

    @property
    def say(self: CommandNode) -> SayCommand:
        return SayCommand(self)

    @property
    def scoreboard(self: CommandNode) -> ScoreboardCommand:
        return ScoreboardCommand(self)

    @property
    def setblock(self: CommandNode) -> SetblockCommand:
        return SetblockCommand(self)

    @property
    def summon(self: CommandNode) -> SummonCommand:
        return SummonCommand(self)

    @property
    def tag(self: CommandNode) -> TagCommand:
        return TagCommand(self)

    @property
    def teleport(self: CommandNode) -> TeleportCommand:
        return TeleportCommand(self)

    @property
    def tellraw(self: CommandNode) -> TellrawCommand:
        return TellrawCommand(self)

    @property
    def time(self: CommandNode) -> TimeCommand:
        return TimeCommand(self)

    @property
    def tp(self: CommandNode) -> TpCommand:
        return TpCommand(self)

    @property
    def trigger(self: CommandNode) -> TriggerCommand:
        return TriggerCommand(self)