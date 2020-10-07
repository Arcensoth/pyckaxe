from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.position import Position
from pyckaxe.types import CompoundDataTag, DataPath, UniqueCommandTarget


class DataCommand(CommandLiteral):
    _LITERAL = "data"

    @property
    def get(self) -> "DataGetCommand":
        return DataGetCommand(self)

    @property
    def merge(self) -> "DataMergeCommand":
        return DataMergeCommand(self)

    @property
    def remove(self) -> "DataRemoveCommand":
        return DataRemoveCommand(self)


# data get


class DataGetCommand(CommandLiteral):
    _LITERAL = "get"

    @property
    def block(self) -> "DataGetBlockCommand":
        return DataGetBlockCommand(self)

    @property
    def entity(self) -> "DataGetEntityCommand":
        return DataGetEntityCommand(self)


class DataGetBlockCommand(CommandLiteral):
    _LITERAL = "block"

    def __call__(
        self, position: Position, path: DataPath, scale: float
    ) -> "DataGetBlockPositionPathScaleCommand":
        return self.position(position).path(path).scale(scale)

    def position(self, position: Position) -> "DataGetBlockPositionCommand":
        return DataGetBlockPositionCommand(self, position)


class DataGetBlockPositionCommand(CommandArgument):
    def path(self, path: DataPath) -> "DataGetBlockPositionPathCommand":
        return DataGetBlockPositionPathCommand(self, path)


class DataGetBlockPositionPathCommand(CommandArgument):
    def scale(self, scale: float) -> "DataGetBlockPositionPathScaleCommand":
        return DataGetBlockPositionPathScaleCommand(self, scale)


class DataGetBlockPositionPathScaleCommand(CommandArgument):
    pass


class DataGetEntityCommand(CommandLiteral):
    _LITERAL = "entity"

    def __call__(
        self, target: UniqueCommandTarget, path: DataPath, scale: float
    ) -> "DataGetEntityTargetPathScaleCommand":
        return self.target(target).path(path).scale(scale)

    def target(self, target: UniqueCommandTarget) -> "DataGetEntityTargetCommand":
        return DataGetEntityTargetCommand(self, target)


class DataGetEntityTargetCommand(CommandArgument):
    def path(self, path: DataPath) -> "DataGetEntityTargetPathCommand":
        return DataGetEntityTargetPathCommand(self, path)


class DataGetEntityTargetPathCommand(CommandArgument):
    def scale(self, scale: float) -> "DataGetEntityTargetPathScaleCommand":
        return DataGetEntityTargetPathScaleCommand(self, scale)


class DataGetEntityTargetPathScaleCommand(CommandArgument):
    pass


# data merge


class DataMergeCommand(CommandLiteral):
    _LITERAL = "merge"

    @property
    def block(self) -> "DataMergeBlockCommand":
        return DataMergeBlockCommand(self)

    @property
    def entity(self) -> "DataMergeEntityCommand":
        return DataMergeEntityCommand(self)


class DataMergeBlockCommand(CommandLiteral):
    _LITERAL = "block"

    def __call__(
        self, position: Position, nbt: CompoundDataTag
    ) -> "DataMergeBlockPositionNbtCommand":
        return self.position(position).nbt(nbt)

    def position(self, position: Position) -> "DataMergeBlockPositionCommand":
        return DataMergeBlockPositionCommand(self, position)


class DataMergeBlockPositionCommand(CommandArgument):
    def nbt(self, nbt: CompoundDataTag) -> "DataMergeBlockPositionNbtCommand":
        return DataMergeBlockPositionNbtCommand(self, nbt)


class DataMergeBlockPositionNbtCommand(CommandArgument):
    pass


class DataMergeEntityCommand(CommandLiteral):
    _LITERAL = "entity"

    def __call__(
        self, target: UniqueCommandTarget, nbt: CompoundDataTag
    ) -> "DataMergeEntityTargetNbtCommand":
        return self.target(target).nbt(nbt)

    def target(self, target: UniqueCommandTarget) -> "DataMergeEntityTargetCommand":
        return DataMergeEntityTargetCommand(self, target)


class DataMergeEntityTargetCommand(CommandArgument):
    def nbt(self, nbt: CompoundDataTag) -> "DataMergeEntityTargetNbtCommand":
        return DataMergeEntityTargetNbtCommand(self, nbt)


class DataMergeEntityTargetNbtCommand(CommandArgument):
    pass


# data remove


class DataRemoveCommand(CommandLiteral):
    _LITERAL = "remove"

    @property
    def block(self) -> "DataRemoveBlockCommand":
        return DataRemoveBlockCommand(self)

    @property
    def entity(self) -> "DataRemoveEntityCommand":
        return DataRemoveEntityCommand(self)


class DataRemoveBlockCommand(CommandLiteral):
    _LITERAL = "block"

    def __call__(self, position: Position, path: DataPath) -> "DataRemoveBlockPositionPathCommand":
        return self.position(position).path(path)

    def position(self, position: Position) -> "DataRemoveBlockPositionCommand":
        return DataRemoveBlockPositionCommand(self, position)


class DataRemoveBlockPositionCommand(CommandArgument):
    def path(self, path: DataPath) -> "DataRemoveBlockPositionPathCommand":
        return DataRemoveBlockPositionPathCommand(self, path)


class DataRemoveBlockPositionPathCommand(CommandArgument):
    pass


class DataRemoveEntityCommand(CommandLiteral):
    _LITERAL = "entity"

    def __call__(
        self, target: UniqueCommandTarget, path: DataPath
    ) -> "DataRemoveEntityTargetPathCommand":
        return self.target(target).path(path)

    def target(self, target: UniqueCommandTarget) -> "DataRemoveEntityTargetCommand":
        return DataRemoveEntityTargetCommand(self, target)


class DataRemoveEntityTargetCommand(CommandArgument):
    def path(self, path: DataPath) -> "DataRemoveEntityTargetPathCommand":
        return DataRemoveEntityTargetPathCommand(self, path)


class DataRemoveEntityTargetPathCommand(CommandArgument):
    pass
