from nbtlib import tag
from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.position import Position
from pyckaxe.types import DataPath, StorageResourceLocation, UniqueCommandTarget


class DataCommand(CommandLiteral):
    _LITERAL = "data"

    @property
    def get(self) -> "DataGetCommand":
        return DataGetCommand(self)

    @property
    def merge(self) -> "DataMergeCommand":
        return DataMergeCommand(self)

    @property
    def modify(self) -> "DataModifyCommand":
        return DataModifyCommand(self)

    @property
    def remove(self) -> "DataRemoveCommand":
        return DataRemoveCommand(self)


# @@ data get


class DataGetCommand(CommandLiteral):
    _LITERAL = "get"

    @property
    def block(self) -> "DataGetBlockCommand":
        return DataGetBlockCommand(self)

    @property
    def entity(self) -> "DataGetEntityCommand":
        return DataGetEntityCommand(self)

    @property
    def storage(self) -> "DataGetStorageCommand":
        return DataGetStorageCommand(self)


# @@ data get block


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


# @@ data get entity


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


# @@ data get storage


class DataGetStorageCommand(CommandLiteral):
    _LITERAL = "storage"

    def __call__(
        self, location: StorageResourceLocation, path: DataPath
    ) -> "DataGetStorageLocationPathCommand":
        return self.location(location).path(path)

    def location(self, location: StorageResourceLocation) -> "DataGetStorageLocationCommand":
        return DataGetStorageLocationCommand(self, location)


class DataGetStorageLocationCommand(CommandArgument):
    def path(self, path: DataPath) -> "DataGetStorageLocationPathCommand":
        return DataGetStorageLocationPathCommand(self, path)


class DataGetStorageLocationPathCommand(CommandArgument):
    pass


# @@ data merge


class DataMergeCommand(CommandLiteral):
    _LITERAL = "merge"

    @property
    def block(self) -> "DataMergeBlockCommand":
        return DataMergeBlockCommand(self)

    @property
    def entity(self) -> "DataMergeEntityCommand":
        return DataMergeEntityCommand(self)

    @property
    def storage(self) -> "DataMergeStorageCommand":
        return DataMergeStorageCommand(self)


# @@ data merge block


class DataMergeBlockCommand(CommandLiteral):
    _LITERAL = "block"

    def __call__(self, position: Position, nbt: tag.Compound) -> "DataMergeBlockPositionNbtCommand":
        return self.position(position).nbt(nbt)

    def position(self, position: Position) -> "DataMergeBlockPositionCommand":
        return DataMergeBlockPositionCommand(self, position)


class DataMergeBlockPositionCommand(CommandArgument):
    def nbt(self, nbt: tag.Compound) -> "DataMergeBlockPositionNbtCommand":
        return DataMergeBlockPositionNbtCommand(self, nbt)


class DataMergeBlockPositionNbtCommand(CommandArgument):
    pass


# @@ data merge entity


class DataMergeEntityCommand(CommandLiteral):
    _LITERAL = "entity"

    def __call__(
        self, target: UniqueCommandTarget, nbt: tag.Compound
    ) -> "DataMergeEntityTargetNbtCommand":
        return self.target(target).nbt(nbt)

    def target(self, target: UniqueCommandTarget) -> "DataMergeEntityTargetCommand":
        return DataMergeEntityTargetCommand(self, target)


class DataMergeEntityTargetCommand(CommandArgument):
    def nbt(self, nbt: tag.Compound) -> "DataMergeEntityTargetNbtCommand":
        return DataMergeEntityTargetNbtCommand(self, nbt)


class DataMergeEntityTargetNbtCommand(CommandArgument):
    pass


# @@ data merge storage


class DataMergeStorageCommand(CommandLiteral):
    _LITERAL = "storage"

    def __call__(
        self, location: StorageResourceLocation, nbt: tag.Compound
    ) -> "DataMergeStorageLocationNbtCommand":
        return self.location(location).nbt(nbt)

    def location(self, location: StorageResourceLocation) -> "DataMergeStorageLocationCommand":
        return DataMergeStorageLocationCommand(self, location)


class DataMergeStorageLocationCommand(CommandArgument):
    def nbt(self, nbt: tag.Compound) -> "DataMergeStorageLocationNbtCommand":
        return DataMergeStorageLocationNbtCommand(self, nbt)


class DataMergeStorageLocationNbtCommand(CommandArgument):
    pass


# @@ data modify


class DataModifyCommand(CommandLiteral):
    _LITERAL = "modify"
    # IMPL data modify


# @@ data remove


class DataRemoveCommand(CommandLiteral):
    _LITERAL = "remove"

    @property
    def block(self) -> "DataRemoveBlockCommand":
        return DataRemoveBlockCommand(self)

    @property
    def entity(self) -> "DataRemoveEntityCommand":
        return DataRemoveEntityCommand(self)

    @property
    def storage(self) -> "DataRemoveStorageCommand":
        return DataRemoveStorageCommand(self)


# @@ data remove block


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


# @@ data remove entity


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


# @@ data remove storage


class DataRemoveStorageCommand(CommandLiteral):
    _LITERAL = "storage"

    def __call__(
        self, location: StorageResourceLocation, path: DataPath
    ) -> "DataRemoveStorageLocationPathCommand":
        return self.location(location).path(path)

    def location(self, location: StorageResourceLocation) -> "DataRemoveStorageLocationCommand":
        return DataRemoveStorageLocationCommand(self, location)


class DataRemoveStorageLocationCommand(CommandArgument):
    def path(self, path: DataPath) -> "DataRemoveStorageLocationPathCommand":
        return DataRemoveStorageLocationPathCommand(self, path)


class DataRemoveStorageLocationPathCommand(CommandArgument):
    pass
