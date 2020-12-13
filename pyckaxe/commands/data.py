from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.nbt import (
    NbtAble,
    NbtBase,
    NbtCompound,
    NbtCompoundAble,
    NbtPath,
    NbtPathAble,
    to_nbt,
    to_nbt_path,
)
from pyckaxe.position import Position
from pyckaxe.types import StorageResourceLocation, UniqueCommandTarget


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
        self, position: Position.Thing, path: NbtPathAble, scale: float
    ) -> "DataGetBlockPositionPathScaleCommand":
        return self.position(position).path(path).scale(scale)

    def position(self, position: Position.Thing) -> "DataGetBlockPositionCommand":
        return DataGetBlockPositionCommand(self, position)


class DataGetBlockPositionCommand(CommandArgument):
    _TYPE = Position

    def path(self, path: NbtPathAble) -> "DataGetBlockPositionPathCommand":
        return DataGetBlockPositionPathCommand(self, path)


class DataGetBlockPositionPathCommand(CommandArgument):
    _CONVERT = to_nbt_path
    _TYPE = NbtPath

    def scale(self, scale: float) -> "DataGetBlockPositionPathScaleCommand":
        return DataGetBlockPositionPathScaleCommand(self, scale)


class DataGetBlockPositionPathScaleCommand(CommandArgument):
    _CONVERT = float
    _TYPE = float


# @@ data get entity


class DataGetEntityCommand(CommandLiteral):
    _LITERAL = "entity"

    def __call__(
        self, target: UniqueCommandTarget, path: NbtPathAble, scale: float
    ) -> "DataGetEntityTargetPathScaleCommand":
        return self.target(target).path(path).scale(scale)

    def target(self, target: UniqueCommandTarget) -> "DataGetEntityTargetCommand":
        return DataGetEntityTargetCommand(self, target)


class DataGetEntityTargetCommand(CommandArgument):
    def path(self, path: NbtPathAble) -> "DataGetEntityTargetPathCommand":
        return DataGetEntityTargetPathCommand(self, path)


class DataGetEntityTargetPathCommand(CommandArgument):
    _CONVERT = to_nbt_path
    _TYPE = NbtPath

    def scale(self, scale: float) -> "DataGetEntityTargetPathScaleCommand":
        return DataGetEntityTargetPathScaleCommand(self, scale)


class DataGetEntityTargetPathScaleCommand(CommandArgument):
    _CONVERT = float
    _TYPE = float


# @@ data get storage


class DataGetStorageCommand(CommandLiteral):
    _LITERAL = "storage"

    def __call__(
        self, location: StorageResourceLocation, path: NbtPathAble
    ) -> "DataGetStorageLocationPathCommand":
        return self.location(location).path(path)

    def location(self, location: StorageResourceLocation) -> "DataGetStorageLocationCommand":
        return DataGetStorageLocationCommand(self, location)


class DataGetStorageLocationCommand(CommandArgument):
    def path(self, path: NbtPathAble) -> "DataGetStorageLocationPathCommand":
        return DataGetStorageLocationPathCommand(self, path)


class DataGetStorageLocationPathCommand(CommandArgument):
    _CONVERT = to_nbt_path
    _TYPE = NbtPath


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

    def __call__(
        self, position: Position.Thing, nbt: NbtCompoundAble
    ) -> "DataMergeBlockPositionNbtCommand":
        return self.position(position).nbt(nbt)

    def position(self, position: Position.Thing) -> "DataMergeBlockPositionCommand":
        return DataMergeBlockPositionCommand(self, position)


class DataMergeBlockPositionCommand(CommandArgument):
    _TYPE = Position

    def nbt(self, nbt: NbtCompoundAble) -> "DataMergeBlockPositionNbtCommand":
        return DataMergeBlockPositionNbtCommand(self, nbt)


class DataMergeBlockPositionNbtCommand(CommandArgument):
    _CONVERT = to_nbt
    _TYPE = NbtCompound


# @@ data merge entity


class DataMergeEntityCommand(CommandLiteral):
    _LITERAL = "entity"

    def __call__(
        self, target: UniqueCommandTarget, nbt: NbtCompoundAble
    ) -> "DataMergeEntityTargetNbtCommand":
        return self.target(target).nbt(nbt)

    def target(self, target: UniqueCommandTarget) -> "DataMergeEntityTargetCommand":
        return DataMergeEntityTargetCommand(self, target)


class DataMergeEntityTargetCommand(CommandArgument):
    def nbt(self, nbt: NbtCompoundAble) -> "DataMergeEntityTargetNbtCommand":
        return DataMergeEntityTargetNbtCommand(self, nbt)


class DataMergeEntityTargetNbtCommand(CommandArgument):
    _CONVERT = to_nbt
    _TYPE = NbtCompound


# @@ data merge storage


class DataMergeStorageCommand(CommandLiteral):
    _LITERAL = "storage"

    def __call__(
        self, location: StorageResourceLocation, nbt: NbtCompoundAble
    ) -> "DataMergeStorageLocationNbtCommand":
        return self.location(location).nbt(nbt)

    def location(self, location: StorageResourceLocation) -> "DataMergeStorageLocationCommand":
        return DataMergeStorageLocationCommand(self, location)


class DataMergeStorageLocationCommand(CommandArgument):
    def nbt(self, nbt: NbtCompoundAble) -> "DataMergeStorageLocationNbtCommand":
        return DataMergeStorageLocationNbtCommand(self, nbt)


class DataMergeStorageLocationNbtCommand(CommandArgument):
    _CONVERT = to_nbt
    _TYPE = NbtCompound


# @@ data modify


class DataModifyCommand(CommandLiteral):
    _LITERAL = "modify"

    @property
    def block(self) -> "DataModifyBlockCommand":
        return DataModifyBlockCommand(self)

    @property
    def entity(self) -> "DataModifyEntityCommand":
        return DataModifyEntityCommand(self)

    @property
    def storage(self) -> "DataModifyStorageCommand":
        return DataModifyStorageCommand(self)


class DataModifyBESCommandMixin:
    @property
    def append(self) -> "DataModifyBESAppendCommand":
        return DataModifyBESAppendCommand(self)

    @property
    def insert(self) -> "DataModifyBESInsertCommand":
        return DataModifyBESInsertCommand(self)

    @property
    def merge(self) -> "DataModifyBESMergeCommand":
        return DataModifyBESMergeCommand(self)

    @property
    def prepend(self) -> "DataModifyBESPrependCommand":
        return DataModifyBESPrependCommand(self)

    @property
    def set(self) -> "DataModifyBESSetCommand":
        return DataModifyBESSetCommand(self)


class DataModifyBESOpCommandMixin:
    @property
    def from_(self) -> "DataModifyBESOpFromCommand":
        return DataModifyBESOpFromCommand(self)

    @property
    def from_block(self) -> "DataModifyBESOpFromBlockCommand":
        return self.from_.block

    @property
    def from_entity(self) -> "DataModifyBESOpFromEntityCommand":
        return self.from_.entity

    @property
    def from_storage(self) -> "DataModifyBESOpFromStorageCommand":
        return self.from_.storage

    @property
    def value(self) -> "DataModifyBESOpValueCommand":
        return DataModifyBESOpValueCommand(self)


class DataModifyBESAppendCommand(CommandLiteral, DataModifyBESOpCommandMixin):
    _LITERAL = "append"


class DataModifyBESInsertCommand(CommandLiteral):
    _LITERAL = "insert"

    def __call__(self, index: int) -> "DataModifyBESInsertIndexCommand":
        return self.index(index)

    def index(self, index: int) -> "DataModifyBESInsertIndexCommand":
        return DataModifyBESInsertIndexCommand(self, index)


class DataModifyBESInsertIndexCommand(CommandArgument, DataModifyBESOpCommandMixin):
    _CONVERT = int
    _TYPE = int


class DataModifyBESMergeCommand(CommandLiteral, DataModifyBESOpCommandMixin):
    _LITERAL = "merge"


class DataModifyBESPrependCommand(CommandLiteral, DataModifyBESOpCommandMixin):
    _LITERAL = "prepend"


class DataModifyBESSetCommand(CommandLiteral, DataModifyBESOpCommandMixin):
    _LITERAL = "set"


# @@data modify ... from


class DataModifyBESOpFromCommand(CommandLiteral):
    _LITERAL = "from"

    @property
    def block(self) -> "DataModifyBESOpFromBlockCommand":
        return DataModifyBESOpFromBlockCommand(self)

    @property
    def entity(self) -> "DataModifyBESOpFromEntityCommand":
        return DataModifyBESOpFromEntityCommand(self)

    @property
    def storage(self) -> "DataModifyBESOpFromStorageCommand":
        return DataModifyBESOpFromStorageCommand(self)


# @@data modify ... from block


class DataModifyBESOpFromBlockCommand(CommandLiteral):
    _LITERAL = "block"

    def __call__(
        self, position: Position.Thing, path: NbtPathAble
    ) -> "DataModifyBESOpFromBlockPositionPathCommand":
        return self.position(position).path(path)

    def position(self, position: Position.Thing) -> "DataModifyBESOpFromBlockPositionCommand":
        return DataModifyBESOpFromBlockPositionCommand(self, position)


class DataModifyBESOpFromBlockPositionCommand(CommandArgument):
    _TYPE = Position

    def __call__(self, path: NbtPathAble) -> "DataModifyBESOpFromBlockPositionPathCommand":
        return self.path(path)

    def path(self, path: NbtPathAble) -> "DataModifyBESOpFromBlockPositionPathCommand":
        return DataModifyBESOpFromBlockPositionPathCommand(self, path)


class DataModifyBESOpFromBlockPositionPathCommand(CommandArgument):
    _CONVERT = to_nbt_path
    _TYPE = NbtPath


# @@data modify ... from entity


class DataModifyBESOpFromEntityCommand(CommandLiteral):
    _LITERAL = "entity"

    def __call__(
        self, target: UniqueCommandTarget, path: NbtPathAble
    ) -> "DataModifyBESOpFromEntityTargetPathCommand":
        return self.target(target).path(path)

    def target(self, target: UniqueCommandTarget) -> "DataModifyBESOpFromEntityTargetCommand":
        return DataModifyBESOpFromEntityTargetCommand(self, target)


class DataModifyBESOpFromEntityTargetCommand(CommandArgument):
    def __call__(self, path: NbtPathAble) -> "DataModifyBESOpFromEntityTargetPathCommand":
        return self.path(path)

    def path(self, path: NbtPathAble) -> "DataModifyBESOpFromEntityTargetPathCommand":
        return DataModifyBESOpFromEntityTargetPathCommand(self, path)


class DataModifyBESOpFromEntityTargetPathCommand(CommandArgument):
    _CONVERT = to_nbt_path
    _TYPE = NbtPath


# @@data modify ... from storage


class DataModifyBESOpFromStorageCommand(CommandLiteral):
    _LITERAL = "storage"

    def __call__(
        self, location: StorageResourceLocation, path: NbtPathAble
    ) -> "DataModifyBESOpFromStorageLocationPathCommand":
        return self.location(location).path(path)

    def location(
        self, location: StorageResourceLocation
    ) -> "DataModifyBESOpFromStorageLocationCommand":
        return DataModifyBESOpFromStorageLocationCommand(self, location)


class DataModifyBESOpFromStorageLocationCommand(CommandArgument):
    def __call__(self, path: NbtPathAble) -> "DataModifyBESOpFromStorageLocationPathCommand":
        return self.path(path)

    def path(self, path: NbtPathAble) -> "DataModifyBESOpFromStorageLocationPathCommand":
        return DataModifyBESOpFromStorageLocationPathCommand(self, path)


class DataModifyBESOpFromStorageLocationPathCommand(CommandArgument):
    _CONVERT = to_nbt_path
    _TYPE = NbtPath


# @@data modify ... value


class DataModifyBESOpValueCommand(CommandLiteral):
    _LITERAL = "value"

    def __call__(self, value: NbtAble) -> "DataModifyBESOpValueValueCommand":
        return self.value(value)

    def value(self, value: NbtAble) -> "DataModifyBESOpValueValueCommand":
        return DataModifyBESOpValueValueCommand(self, value)


class DataModifyBESOpValueValueCommand(CommandArgument):
    _CONVERT = to_nbt
    _TYPE = NbtBase


# @@ data modify block


class DataModifyBlockCommand(CommandLiteral):
    _LITERAL = "block"

    def __call__(
        self, position: Position.Thing, path: NbtPathAble
    ) -> "DataModifyBlockPositionPathCommand":
        return self.position(position).path(path)

    def position(self, position: Position.Thing) -> "DataModifyBlockPositionCommand":
        return DataModifyBlockPositionCommand(self, position)


class DataModifyBlockPositionCommand(CommandArgument):
    _TYPE = Position

    def path(self, path: NbtPathAble) -> "DataModifyBlockPositionPathCommand":
        return DataModifyBlockPositionPathCommand(self, path)


class DataModifyBlockPositionPathCommand(CommandArgument, DataModifyBESCommandMixin):
    _CONVERT = to_nbt_path
    _TYPE = NbtPath


# @@ data remove entity


class DataModifyEntityCommand(CommandLiteral):
    _LITERAL = "entity"

    def __call__(
        self, target: UniqueCommandTarget, path: NbtPathAble
    ) -> "DataModifyEntityTargetPathCommand":
        return self.target(target).path(path)

    def target(self, target: UniqueCommandTarget) -> "DataModifyEntityTargetCommand":
        return DataModifyEntityTargetCommand(self, target)


class DataModifyEntityTargetCommand(CommandArgument):
    def path(self, path: NbtPathAble) -> "DataModifyEntityTargetPathCommand":
        return DataModifyEntityTargetPathCommand(self, path)


class DataModifyEntityTargetPathCommand(CommandArgument, DataModifyBESCommandMixin):
    _CONVERT = to_nbt_path
    _TYPE = NbtPath


# @@ data modify storage


class DataModifyStorageCommand(CommandLiteral):
    _LITERAL = "storage"

    def __call__(
        self, location: StorageResourceLocation, path: NbtPathAble
    ) -> "DataModifyStorageLocationPathCommand":
        return self.location(location).path(path)

    def location(self, location: StorageResourceLocation) -> "DataModifyStorageLocationCommand":
        return DataModifyStorageLocationCommand(self, location)


class DataModifyStorageLocationCommand(CommandArgument):
    def path(self, path: NbtPathAble) -> "DataModifyStorageLocationPathCommand":
        return DataModifyStorageLocationPathCommand(self, path)


class DataModifyStorageLocationPathCommand(CommandArgument, DataModifyBESCommandMixin):
    _CONVERT = to_nbt_path
    _TYPE = NbtPath


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

    def __call__(
        self, position: Position.Thing, path: NbtPathAble
    ) -> "DataRemoveBlockPositionPathCommand":
        return self.position(position).path(path)

    def position(self, position: Position.Thing) -> "DataRemoveBlockPositionCommand":
        return DataRemoveBlockPositionCommand(self, position)


class DataRemoveBlockPositionCommand(CommandArgument):
    _TYPE = Position

    def path(self, path: NbtPathAble) -> "DataRemoveBlockPositionPathCommand":
        return DataRemoveBlockPositionPathCommand(self, path)


class DataRemoveBlockPositionPathCommand(CommandArgument):
    _CONVERT = to_nbt_path
    _TYPE = NbtPath


# @@ data remove entity


class DataRemoveEntityCommand(CommandLiteral):
    _LITERAL = "entity"

    def __call__(
        self, target: UniqueCommandTarget, path: NbtPathAble
    ) -> "DataRemoveEntityTargetPathCommand":
        return self.target(target).path(path)

    def target(self, target: UniqueCommandTarget) -> "DataRemoveEntityTargetCommand":
        return DataRemoveEntityTargetCommand(self, target)


class DataRemoveEntityTargetCommand(CommandArgument):
    def path(self, path: NbtPathAble) -> "DataRemoveEntityTargetPathCommand":
        return DataRemoveEntityTargetPathCommand(self, path)


class DataRemoveEntityTargetPathCommand(CommandArgument):
    _CONVERT = to_nbt_path
    _TYPE = NbtPath


# @@ data remove storage


class DataRemoveStorageCommand(CommandLiteral):
    _LITERAL = "storage"

    def __call__(
        self, location: StorageResourceLocation, path: NbtPathAble
    ) -> "DataRemoveStorageLocationPathCommand":
        return self.location(location).path(path)

    def location(self, location: StorageResourceLocation) -> "DataRemoveStorageLocationCommand":
        return DataRemoveStorageLocationCommand(self, location)


class DataRemoveStorageLocationCommand(CommandArgument):
    def path(self, path: NbtPathAble) -> "DataRemoveStorageLocationPathCommand":
        return DataRemoveStorageLocationPathCommand(self, path)


class DataRemoveStorageLocationPathCommand(CommandArgument):
    _CONVERT = to_nbt_path
    _TYPE = NbtPath
