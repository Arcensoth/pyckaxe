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
    def advancement(self) -> AdvancementCommand:
        return AdvancementCommand(self)

    @property
    def clear(self) -> ClearCommand:
        return ClearCommand(self)

    @property
    def clone(self) -> CloneCommand:
        return CloneCommand(self)

    @property
    def data(self) -> DataCommand:
        return DataCommand(self)

    @property
    def effect(self) -> EffectCommand:
        return EffectCommand(self)

    @property
    def execute(self) -> ExecuteCommand:
        return ExecuteCommand(self)

    @property
    def fill(self) -> FillCommand:
        return FillCommand(self)

    @property
    def function(self) -> FunctionCommand:
        return FunctionCommand(self)

    @property
    def give(self) -> GiveCommand:
        return GiveCommand(self)

    @property
    def kill(self) -> KillCommand:
        return KillCommand(self)

    @property
    def playsound(self) -> PlaysoundCommand:
        return PlaysoundCommand(self)

    @property
    def replaceitem(self) -> ReplaceitemCommand:
        return ReplaceitemCommand(self)

    @property
    def say(self) -> SayCommand:
        return SayCommand(self)

    @property
    def scoreboard(self) -> ScoreboardCommand:
        return ScoreboardCommand(self)

    @property
    def setblock(self) -> SetblockCommand:
        return SetblockCommand(self)

    @property
    def summon(self) -> SummonCommand:
        return SummonCommand(self)

    @property
    def tag(self) -> TagCommand:
        return TagCommand(self)

    @property
    def teleport(self) -> TeleportCommand:
        return TeleportCommand(self)

    @property
    def tellraw(self) -> TellrawCommand:
        return TellrawCommand(self)

    @property
    def time(self) -> TimeCommand:
        return TimeCommand(self)

    @property
    def tp(self) -> TpCommand:
        return TpCommand(self)

    @property
    def trigger(self) -> TriggerCommand:
        return TriggerCommand(self)
