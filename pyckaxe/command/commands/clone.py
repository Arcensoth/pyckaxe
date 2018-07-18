from pyckaxe.command.abc.command import Command, CommandArgument, CommandLiteral
from pyckaxe.types import Block, Position


class CloneBeginEndDestinationFMRMixin:
    @property
    def force(self: Command) -> 'CloneBeginEndDestinationFMRForceCommand':
        return CloneBeginEndDestinationFMRForceCommand(self)

    @property
    def move(self: Command) -> 'CloneBeginEndDestinationFMRMoveCommand':
        return CloneBeginEndDestinationFMRMoveCommand(self)

    @property
    def normal(self: Command) -> 'CloneBeginEndDestinationFMRNormalCommand':
        return CloneBeginEndDestinationFMRNormalCommand(self)


class CloneCommand(CommandLiteral):
    _LITERAL = 'clone'

    def __call__(self, begin: Position, end: Position, destination: Position) -> 'CloneBeginEndDestinationCommand':
        return self.begin(begin).end(end).destination(destination)

    def begin(self, begin: Position) -> 'CloneBeginCommand':
        return CloneBeginCommand(self, begin)


class CloneBeginCommand(CommandArgument):
    def end(self, end: Position) -> 'CloneBeginEndCommand':
        return CloneBeginEndCommand(self, end)


class CloneBeginEndCommand(CommandArgument):
    def destination(self, destination: Position) -> 'CloneBeginEndDestinationCommand':
        return CloneBeginEndDestinationCommand(self, destination)


class CloneBeginEndDestinationCommand(CommandArgument):
    @property
    def filtered(self) -> 'CloneBeginEndDestinationFilteredCommand':
        return CloneBeginEndDestinationFilteredCommand(self)

    @property
    def masked(self) -> 'CloneBeginEndDestinationMaskedCommand':
        return CloneBeginEndDestinationMaskedCommand(self)

    @property
    def replace(self) -> 'CloneBeginEndDestinationReplaceCommand':
        return CloneBeginEndDestinationReplaceCommand(self)


class CloneBeginEndDestinationFilteredCommand(CommandLiteral):
    _LITERAL = 'filtered'

    def __call__(self, filter: Block) -> 'CloneBeginEndDestinationFilteredFilterCommand':
        return self.filter(filter)

    def filter(self, filter: Block) -> 'CloneBeginEndDestinationFilteredFilterCommand':
        return CloneBeginEndDestinationFilteredFilterCommand(self, filter)


class CloneBeginEndDestinationFilteredFilterCommand(CommandArgument, CloneBeginEndDestinationFMRMixin):
    pass


class CloneBeginEndDestinationMaskedCommand(CommandLiteral, CloneBeginEndDestinationFMRMixin):
    _LITERAL = 'masked'


class CloneBeginEndDestinationReplaceCommand(CommandLiteral, CloneBeginEndDestinationFMRMixin):
    _LITERAL = 'replace'


class CloneBeginEndDestinationFMRForceCommand(CommandLiteral):
    _LITERAL = 'force'


class CloneBeginEndDestinationFMRMoveCommand(CommandLiteral):
    _LITERAL = 'move'


class CloneBeginEndDestinationFMRNormalCommand(CommandLiteral):
    _LITERAL = 'normal'
