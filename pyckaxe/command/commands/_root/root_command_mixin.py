from pyckaxe.command import commands as cc
from pyckaxe.command.abc.command import CommandNode


class RootCommandMixin:
    @property
    def advancement(self: CommandNode) -> "AdvancementCommand":
        return cc.AdvancementCommand(self)

    @property
    def clear(self: CommandNode) -> "ClearCommand":
        return cc.ClearCommand(self)

    @property
    def clone(self: CommandNode) -> "CloneCommand":
        return cc.CloneCommand(self)

    @property
    def data(self: CommandNode) -> "DataCommand":
        return cc.DataCommand(self)

    @property
    def effect(self: CommandNode) -> "EffectCommand":
        return cc.EffectCommand(self)

    @property
    def execute(self: CommandNode) -> "ExecuteCommand":
        return cc.ExecuteCommand(self)

    @property
    def fill(self: CommandNode) -> "FillCommand":
        return cc.FillCommand(self)

    @property
    def function(self: CommandNode) -> "FunctionCommand":
        return cc.FunctionCommand(self)

    @property
    def give(self: CommandNode) -> "GiveCommand":
        return cc.GiveCommand(self)

    @property
    def kill(self: CommandNode) -> "KillCommand":
        return cc.KillCommand(self)

    @property
    def playsound(self: CommandNode) -> "PlaysoundCommand":
        return cc.PlaysoundCommand(self)

    @property
    def replaceitem(self: CommandNode) -> "ReplaceitemCommand":
        return cc.ReplaceitemCommand(self)

    @property
    def say(self: CommandNode) -> "SayCommand":
        return cc.SayCommand(self)

    @property
    def scoreboard(self: CommandNode) -> "ScoreboardCommand":
        return cc.ScoreboardCommand(self)

    @property
    def setblock(self: CommandNode) -> "SetblockCommand":
        return cc.SetblockCommand(self)

    @property
    def summon(self: CommandNode) -> "SummonCommand":
        return cc.SummonCommand(self)

    @property
    def tag(self: CommandNode) -> "TagCommand":
        return cc.TagCommand(self)

    @property
    def teleport(self: CommandNode) -> "TeleportCommand":
        return cc.TeleportCommand(self)

    @property
    def tellraw(self: CommandNode) -> "TellrawCommand":
        return cc.TellrawCommand(self)

    @property
    def time(self: CommandNode) -> "TimeCommand":
        return cc.TimeCommand(self)

    @property
    def tp(self: CommandNode) -> "TpCommand":
        return cc.TpCommand(self)

    @property
    def trigger(self: CommandNode) -> "TriggerCommand":
        return cc.TriggerCommand(self)
