from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.types import CompoundDataTag, Entity, Position


class SummonCommand(CommandLiteral):
    _LITERAL = 'summon'

    def __call__(self, entity: Entity, position: Position, nbt: CompoundDataTag) -> 'SummonEntityPositionNbtCommand':
        return self.entity(entity).position(position).nbt(nbt)

    def entity(self, entity: Entity) -> 'SummonEntityCommand':
        return SummonEntityCommand(self, entity)


class SummonEntityCommand(CommandArgument):
    def position(self, position: Position) -> 'SummonEntityPositionCommand':
        return SummonEntityPositionCommand(self, position)


class SummonEntityPositionCommand(CommandArgument):
    def nbt(self, nbt: CompoundDataTag) -> 'SummonEntityPositionNbtCommand':
        return SummonEntityPositionNbtCommand(self, nbt)


class SummonEntityPositionNbtCommand(CommandArgument):
    pass
