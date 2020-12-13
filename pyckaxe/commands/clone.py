from pyckaxe.block_predicate import BlockPredicate
from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.position import Position


class CloneBeginEndDestinationFMRCommandMixin:
    @property
    def force(self) -> "CloneBeginEndDestinationFMRForceCommand":
        return CloneBeginEndDestinationFMRForceCommand(self)

    @property
    def move(self) -> "CloneBeginEndDestinationFMRMoveCommand":
        return CloneBeginEndDestinationFMRMoveCommand(self)

    @property
    def normal(self) -> "CloneBeginEndDestinationFMRNormalCommand":
        return CloneBeginEndDestinationFMRNormalCommand(self)


class CloneCommand(CommandLiteral):
    _LITERAL = "clone"

    def __call__(
        self, begin: Position.Thing, end: Position.Thing, destination: Position.Thing
    ) -> "CloneBeginEndDestinationCommand":
        return self.begin(begin).end(end).destination(destination)

    def begin(self, begin: Position.Thing) -> "CloneBeginCommand":
        return CloneBeginCommand(self, begin)


class CloneBeginCommand(CommandArgument):
    _TYPE = Position

    def end(self, end: Position.Thing) -> "CloneBeginEndCommand":
        return CloneBeginEndCommand(self, end)


class CloneBeginEndCommand(CommandArgument):
    _TYPE = Position

    def destination(self, destination: Position.Thing) -> "CloneBeginEndDestinationCommand":
        return CloneBeginEndDestinationCommand(self, destination)


class CloneBeginEndDestinationCommand(CommandArgument):
    _TYPE = Position

    @property
    def filtered(self) -> "CloneBeginEndDestinationFilteredCommand":
        return CloneBeginEndDestinationFilteredCommand(self)

    @property
    def masked(self) -> "CloneBeginEndDestinationMaskedCommand":
        return CloneBeginEndDestinationMaskedCommand(self)

    @property
    def replace(self) -> "CloneBeginEndDestinationReplaceCommand":
        return CloneBeginEndDestinationReplaceCommand(self)


class CloneBeginEndDestinationFilteredCommand(CommandLiteral):
    _LITERAL = "filtered"

    def __call__(self, filter_: BlockPredicate) -> "CloneBeginEndDestinationFilteredFilterCommand":
        return self.filter(filter_)

    def filter(self, filter_: BlockPredicate) -> "CloneBeginEndDestinationFilteredFilterCommand":
        return CloneBeginEndDestinationFilteredFilterCommand(self, filter_)


class CloneBeginEndDestinationFilteredFilterCommand(
    CommandArgument, CloneBeginEndDestinationFMRCommandMixin
):
    pass


class CloneBeginEndDestinationMaskedCommand(
    CommandLiteral, CloneBeginEndDestinationFMRCommandMixin
):
    _LITERAL = "masked"


class CloneBeginEndDestinationReplaceCommand(
    CommandLiteral, CloneBeginEndDestinationFMRCommandMixin
):
    _LITERAL = "replace"


class CloneBeginEndDestinationFMRForceCommand(CommandLiteral):
    _LITERAL = "force"


class CloneBeginEndDestinationFMRMoveCommand(CommandLiteral):
    _LITERAL = "move"


class CloneBeginEndDestinationFMRNormalCommand(CommandLiteral):
    _LITERAL = "normal"
