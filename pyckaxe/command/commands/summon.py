from pyckaxe.command.abc.command import CommandArgument, CommandLiteral


class SummonCommand(CommandLiteral):
    _LITERAL = 'summon'

    def __call__(self, entity: str, position: str, nbt: str) -> 'SummonEntityPositionNbtCommand':
        return self.entity(entity).position(position).nbt(nbt)

    def entity(self, entity: str) -> 'SummonEntityCommand':
        return SummonEntityCommand(self, entity)


class SummonEntityCommand(CommandArgument):
    def position(self, position: str) -> 'SummonEntityPositionCommand':
        return SummonEntityPositionCommand(self, position)


class SummonEntityPositionCommand(CommandArgument):
    def nbt(self, nbt: str) -> 'SummonEntityPositionNbtCommand':
        return SummonEntityPositionNbtCommand(self, nbt)


class SummonEntityPositionNbtCommand(CommandArgument):
    pass
