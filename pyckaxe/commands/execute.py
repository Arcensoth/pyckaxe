from typing import TYPE_CHECKING

from pyckaxe.block_predicate import BlockPredicate
from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.nbt import NbtPath, NbtPathAble, to_nbt_path
from pyckaxe.position import Position
from pyckaxe.types import (
    BossbarID,
    CommandTarget,
    ScoreboardObjective,
    ScoreHolder,
    StorageResourceLocation,
)

if TYPE_CHECKING:
    from pyckaxe.commands.execute_run import ExecuteRunCommand


class ExecuteCommandMixin:
    @property
    def align(self) -> "ExecuteAlignCommand":
        return ExecuteAlignCommand(self)

    @property
    def anchored(self) -> "ExecuteAnchoredCommand":
        return ExecuteAnchoredCommand(self)

    @property
    def as_(self) -> "ExecuteAsCommand":
        return ExecuteAsCommand(self)

    @property
    def at(self) -> "ExecuteAtCommand":
        return ExecuteAtCommand(self)

    @property
    def facing(self) -> "ExecuteFacingCommand":
        return ExecuteFacingCommand(self)

    @property
    def if_(self) -> "ExecuteIfCommand":
        return ExecuteIfCommand(self)

    @property
    def if_block(self) -> "ExecuteIfUnlessBlockCommand":
        return self.if_.block

    @property
    def if_blocks(self) -> "ExecuteIfUnlessBlocksCommand":
        return self.if_.blocks

    @property
    def if_data(self) -> "ExecuteIfUnlessDataCommand":
        return self.if_.data

    @property
    def if_entity(self) -> "ExecuteIfUnlessEntityCommand":
        return self.if_.entity

    @property
    def if_predicate(self) -> "ExecuteIfUnlessPredicateCommand":
        return self.if_.predicate

    @property
    def if_score(self) -> "ExecuteIfUnlessScoreCommand":
        return self.if_.score

    @property
    def in_(self) -> "ExecuteInCommand":
        return ExecuteInCommand(self)

    @property
    def positioned(self) -> "ExecutePositionedCommand":
        return ExecutePositionedCommand(self)

    @property
    def rotated(self) -> "ExecuteRotatedCommand":
        return ExecuteRotatedCommand(self)

    @property
    def run(self) -> "ExecuteRunCommand":
        # NOTE This needs to be imported locally to avoid a circular import.
        from pyckaxe.commands.execute_run import ExecuteRunCommand

        return ExecuteRunCommand(self)

    @property
    def store(self) -> "ExecuteStoreCommand":
        return ExecuteStoreCommand(self)

    @property
    def unless(self) -> "ExecuteUnlessCommand":
        return ExecuteUnlessCommand(self)

    @property
    def unless_block(self) -> "ExecuteIfUnlessBlockCommand":
        return self.unless.block

    @property
    def unless_blocks(self) -> "ExecuteIfUnlessBlocksCommand":
        return self.unless.blocks

    @property
    def unless_data(self) -> "ExecuteIfUnlessDataCommand":
        return self.unless.data

    @property
    def unless_entity(self) -> "ExecuteIfUnlessEntityCommand":
        return self.unless.entity

    @property
    def unless_predicate(self) -> "ExecuteIfUnlessPredicateCommand":
        return self.unless.predicate

    @property
    def unless_score(self) -> "ExecuteIfUnlessScoreCommand":
        return self.unless.score


class ExecuteCommand(CommandLiteral, ExecuteCommandMixin):
    _LITERAL = "execute"


# @@ execute align


class ExecuteAlignCommand(CommandLiteral):
    _LITERAL = "align"
    # IMPL execute align


# @@ execute anchored


class ExecuteAnchoredCommand(CommandLiteral):
    _LITERAL = "anchored"
    # IMPL execute anchored


# @@ execute as


class ExecuteAsCommand(CommandLiteral):
    _LITERAL = "as"

    def __call__(self, targets: CommandTarget) -> "ExecuteAsTargetsCommand":
        return self.targets(targets)

    def targets(self, targets: CommandTarget) -> "ExecuteAsTargetsCommand":
        return ExecuteAsTargetsCommand(self, targets)


class ExecuteAsTargetsCommand(CommandArgument, ExecuteCommandMixin):
    pass


# @@ execute at


class ExecuteAtCommand(CommandLiteral):
    _LITERAL = "at"

    def __call__(self, targets: CommandTarget) -> "ExecuteAtTargetsCommand":
        return self.targets(targets)

    def targets(self, targets: CommandTarget) -> "ExecuteAtTargetsCommand":
        return ExecuteAtTargetsCommand(self, targets)


class ExecuteAtTargetsCommand(CommandArgument, ExecuteCommandMixin):
    pass


# @@ execute facing


class ExecuteFacingCommand(CommandLiteral):
    _LITERAL = "facing"


# @@ execute if/unless


class ExecuteIfUnlessCommandMixin:
    @property
    def block(self) -> "ExecuteIfUnlessBlockCommand":
        return ExecuteIfUnlessBlockCommand(self)

    @property
    def blocks(self) -> "ExecuteIfUnlessBlocksCommand":
        return ExecuteIfUnlessBlocksCommand(self)

    @property
    def data(self) -> "ExecuteIfUnlessDataCommand":
        return ExecuteIfUnlessDataCommand(self)

    @property
    def entity(self) -> "ExecuteIfUnlessEntityCommand":
        return ExecuteIfUnlessEntityCommand(self)

    @property
    def predicate(self) -> "ExecuteIfUnlessPredicateCommand":
        return ExecuteIfUnlessPredicateCommand(self)

    @property
    def score(self) -> "ExecuteIfUnlessScoreCommand":
        return ExecuteIfUnlessScoreCommand(self)


class ExecuteIfCommand(CommandLiteral, ExecuteIfUnlessCommandMixin):
    _LITERAL = "if"


class ExecuteUnlessCommand(CommandLiteral, ExecuteIfUnlessCommandMixin):
    _LITERAL = "unless"


# @@ execute if/unless block


class ExecuteIfUnlessBlockCommand(CommandLiteral):
    _LITERAL = "block"

    def __call__(
        self, position: Position.Thing, block: BlockPredicate
    ) -> "ExecuteIfUnlessBlockPositionBlockCommand":
        return self.position(position).block(block)

    def position(self, position: Position.Thing) -> "ExecuteIfUnlessBlockPositionCommand":
        return ExecuteIfUnlessBlockPositionCommand(self, position)


class ExecuteIfUnlessBlockPositionCommand(CommandArgument):
    _TYPE = Position

    def block(self, block: BlockPredicate) -> "ExecuteIfUnlessBlockPositionBlockCommand":
        return ExecuteIfUnlessBlockPositionBlockCommand(self, block)


class ExecuteIfUnlessBlockPositionBlockCommand(CommandArgument, ExecuteCommandMixin):
    pass


# @@ execute if/unless blocks


class ExecuteIfUnlessBlocksCommand(CommandLiteral):
    _LITERAL = "blocks"

    def __call__(
        self, start: Position, end: Position, destination: Position
    ) -> "ExecuteIfUnlessBlocksStartEndDestinationCommand":
        return self.start(start).end(end).destination(destination)

    def start(self, start: Position) -> "ExecuteIfUnlessBlocksStartCommand":
        return ExecuteIfUnlessBlocksStartCommand(self, start)


class ExecuteIfUnlessBlocksStartCommand(CommandArgument):
    def end(self, end: Position) -> "ExecuteIfUnlessBlocksStartEndCommand":
        return ExecuteIfUnlessBlocksStartEndCommand(self, end)


class ExecuteIfUnlessBlocksStartEndCommand(CommandArgument):
    def destination(
        self, destination: Position
    ) -> "ExecuteIfUnlessBlocksStartEndDestinationCommand":
        return ExecuteIfUnlessBlocksStartEndDestinationCommand(self, destination)


class ExecuteIfUnlessBlocksStartEndDestinationCommand(CommandArgument):
    @property
    def all(self) -> "ExecuteIfUnlessBlocksStartEndDestinationAllCommand":
        return ExecuteIfUnlessBlocksStartEndDestinationAllCommand(self)

    @property
    def masked(self) -> "ExecuteIfUnlessBlocksStartEndDestinationMaskedCommand":
        return ExecuteIfUnlessBlocksStartEndDestinationMaskedCommand(self)


class ExecuteIfUnlessBlocksStartEndDestinationAllCommand(CommandLiteral, ExecuteCommandMixin):
    _LITERAL = "all"


class ExecuteIfUnlessBlocksStartEndDestinationMaskedCommand(CommandLiteral, ExecuteCommandMixin):
    _LITERAL = "masked"


# @@ execute if/unless data


class ExecuteIfUnlessDataCommand(CommandLiteral):
    _LITERAL = "data"

    @property
    def block(self) -> "ExecuteIfUnlessDataBlockCommand":
        return ExecuteIfUnlessDataBlockCommand(self)

    @property
    def entity(self) -> "ExecuteIfUnlessDataEntityCommand":
        return ExecuteIfUnlessDataEntityCommand(self)

    @property
    def storage(self) -> "ExecuteIfUnlessDataStorageCommand":
        return ExecuteIfUnlessDataStorageCommand(self)


# @@ execute if/unless data block


class ExecuteIfUnlessDataBlockCommand(CommandLiteral):
    _LITERAL = "block"

    def __call__(
        self, position: Position.Thing, path: NbtPathAble
    ) -> "ExecuteIfUnlessDataBlockPositionPathCommand":
        return self.position(position).path(path)

    def position(self, position: Position.Thing) -> "ExecuteIfUnlessDataBlockPositionCommand":
        return ExecuteIfUnlessDataBlockPositionCommand(self, position)


class ExecuteIfUnlessDataBlockPositionCommand(CommandArgument, ExecuteCommandMixin):
    _TYPE = Position

    def path(self, path: NbtPathAble) -> "ExecuteIfUnlessDataBlockPositionPathCommand":
        return ExecuteIfUnlessDataBlockPositionPathCommand(self, path)


class ExecuteIfUnlessDataBlockPositionPathCommand(CommandArgument, ExecuteCommandMixin):
    _CONVERT = to_nbt_path
    _TYPE = NbtPath


# @@ execute if/unless data entity
class ExecuteIfUnlessDataEntityCommand(CommandLiteral):
    _LITERAL = "entity"

    def __call__(
        self, target: CommandTarget, path: NbtPathAble
    ) -> "ExecuteIfUnlessDataEntityTargetPathCommand":
        return self.target(target).path(path)

    def target(self, target: CommandTarget) -> "ExecuteIfUnlessDataEntityTargetCommand":
        return ExecuteIfUnlessDataEntityTargetCommand(self, target)


class ExecuteIfUnlessDataEntityTargetCommand(CommandArgument, ExecuteCommandMixin):
    def path(self, path: NbtPathAble) -> "ExecuteIfUnlessDataEntityTargetPathCommand":
        return ExecuteIfUnlessDataEntityTargetPathCommand(self, path)


class ExecuteIfUnlessDataEntityTargetPathCommand(CommandArgument, ExecuteCommandMixin):
    _CONVERT = to_nbt_path
    _TYPE = NbtPath


# @@ execute if/unless data storage
class ExecuteIfUnlessDataStorageCommand(CommandLiteral):
    _LITERAL = "storage"

    def __call__(
        self, location: StorageResourceLocation, path: NbtPathAble
    ) -> "ExecuteIfUnlessDataStorageLocationPathCommand":
        return self.location(location).path(path)

    def location(
        self, location: StorageResourceLocation
    ) -> "ExecuteIfUnlessDataStorageLocationCommand":
        return ExecuteIfUnlessDataStorageLocationCommand(self, location)


class ExecuteIfUnlessDataStorageLocationCommand(CommandArgument, ExecuteCommandMixin):
    def path(self, path: NbtPathAble) -> "ExecuteIfUnlessDataStorageLocationPathCommand":
        return ExecuteIfUnlessDataStorageLocationPathCommand(self, path)


class ExecuteIfUnlessDataStorageLocationPathCommand(CommandArgument, ExecuteCommandMixin):
    _CONVERT = to_nbt_path
    _TYPE = NbtPath


# @@ execute if/unless entity


class ExecuteIfUnlessEntityCommand(CommandLiteral):
    _LITERAL = "entity"
    # IMPL execute if/unless entity


# @@ execute if/unless predicate


class ExecuteIfUnlessPredicateCommand(CommandLiteral):
    _LITERAL = "predicate"
    # IMPL execute if/unless data


# @@ execute if/unless score


class ExecuteIfUnlessScoreCommand(CommandLiteral):
    _LITERAL = "score"
    # IMPL execute if/unless score


# @@ execute in


class ExecuteInCommand(CommandLiteral):
    _LITERAL = "in"

    @property
    def overworld(self) -> "ExecuteInOverworldCommand":
        return ExecuteInOverworldCommand(self)

    @property
    def the_end(self) -> "ExecuteInTheEndCommand":
        return ExecuteInTheEndCommand(self)

    @property
    def the_nether(self) -> "ExecuteInTheNetherCommand":
        return ExecuteInTheNetherCommand(self)


class ExecuteInOverworldCommand(CommandLiteral, ExecuteCommandMixin):
    _LITERAL = "overworld"


class ExecuteInTheEndCommand(CommandLiteral, ExecuteCommandMixin):
    _LITERAL = "the_end"


class ExecuteInTheNetherCommand(CommandLiteral, ExecuteCommandMixin):
    _LITERAL = "the_nether"


# @@ execute positioned


class ExecutePositionedCommand(CommandLiteral):
    _LITERAL = "positioned"

    def __call__(self, position: Position.Thing) -> "ExecutePositionedPositionCommand":
        return self.position(position)

    def position(self, position: Position.Thing) -> "ExecutePositionedPositionCommand":
        return ExecutePositionedPositionCommand(self, position)

    @property
    def as_(self) -> "ExecutePositionedAsCommand":
        return ExecutePositionedAsCommand(self)


class ExecutePositionedPositionCommand(CommandArgument, ExecuteCommandMixin):
    _TYPE = Position


class ExecutePositionedAsCommand(CommandLiteral):
    _LITERAL = "as"

    def __call__(self, target: CommandTarget) -> "ExecutePositionedAsTargetCommand":
        return self.target(target)

    def target(self, target: CommandTarget) -> "ExecutePositionedAsTargetCommand":
        return ExecutePositionedAsTargetCommand(self, target)


class ExecutePositionedAsTargetCommand(CommandArgument, ExecuteCommandMixin):
    pass


# @@ execute rotated


class ExecuteRotatedCommand(CommandLiteral):
    _LITERAL = "rotated"
    # IMPL execute rotated


# @@ execute store


class ExecuteStoreCommand(CommandLiteral):
    _LITERAL = "store"

    @property
    def result(self) -> "ExecuteStoreResultCommand":
        return ExecuteStoreResultCommand(self)

    @property
    def success(self) -> "ExecuteStoreSuccessCommand":
        return ExecuteStoreSuccessCommand(self)


class ExecuteStoreResultSuccessCommandMixin:
    @property
    def block(self) -> "ExecuteStoreResultSuccessBlockCommand":
        return ExecuteStoreResultSuccessBlockCommand(self)

    @property
    def bossbar(self) -> "ExecuteStoreResultSuccessBossbarCommand":
        return ExecuteStoreResultSuccessBossbarCommand(self)

    @property
    def entity(self) -> "ExecuteStoreResultSuccessEntityCommand":
        return ExecuteStoreResultSuccessEntityCommand(self)

    @property
    def score(self) -> "ExecuteStoreResultSuccessScoreCommand":
        return ExecuteStoreResultSuccessScoreCommand(self)

    @property
    def storage(self) -> "ExecuteStoreResultSuccessStorageCommand":
        return ExecuteStoreResultSuccessStorageCommand(self)


class ExecuteStoreResultCommand(CommandLiteral, ExecuteStoreResultSuccessCommandMixin):
    _LITERAL = "result"


class ExecuteStoreSuccessCommand(CommandLiteral, ExecuteStoreResultSuccessCommandMixin):
    _LITERAL = "success"


class ExecuteStoreResultSuccessNbtCommandMixin:
    @property
    def byte(self) -> "ExecuteStoreResultSuccessNbtByteCommand":
        return ExecuteStoreResultSuccessNbtByteCommand(self)

    @property
    def double(self) -> "ExecuteStoreResultSuccessNbtDoubleCommand":
        return ExecuteStoreResultSuccessNbtDoubleCommand(self)

    @property
    def float(self) -> "ExecuteStoreResultSuccessNbtFloatCommand":
        return ExecuteStoreResultSuccessNbtFloatCommand(self)

    @property
    def int(self) -> "ExecuteStoreResultSuccessNbtIntCommand":
        return ExecuteStoreResultSuccessNbtIntCommand(self)

    @property
    def long(self) -> "ExecuteStoreResultSuccessNbtLongCommand":
        return ExecuteStoreResultSuccessNbtLongCommand(self)

    @property
    def short(self) -> "ExecuteStoreResultSuccessNbtShortCommand":
        return ExecuteStoreResultSuccessNbtShortCommand(self)


class ExecuteStoreResultSuccessNbtTypeCommandLiteralBase(CommandLiteral):
    def __call__(self, scale: float) -> "ExecuteStoreResultSuccessNbtTypeCommand":
        return self.scale(scale)

    def scale(self, scale: float) -> "ExecuteStoreResultSuccessNbtTypeCommand":
        return ExecuteStoreResultSuccessNbtTypeCommand(self, scale)


class ExecuteStoreResultSuccessNbtByteCommand(ExecuteStoreResultSuccessNbtTypeCommandLiteralBase):
    _LITERAL = "byte"


class ExecuteStoreResultSuccessNbtDoubleCommand(ExecuteStoreResultSuccessNbtTypeCommandLiteralBase):
    _LITERAL = "double"


class ExecuteStoreResultSuccessNbtFloatCommand(ExecuteStoreResultSuccessNbtTypeCommandLiteralBase):
    _LITERAL = "float"


class ExecuteStoreResultSuccessNbtIntCommand(ExecuteStoreResultSuccessNbtTypeCommandLiteralBase):
    _LITERAL = "int"


class ExecuteStoreResultSuccessNbtLongCommand(ExecuteStoreResultSuccessNbtTypeCommandLiteralBase):
    _LITERAL = "long"


class ExecuteStoreResultSuccessNbtShortCommand(ExecuteStoreResultSuccessNbtTypeCommandLiteralBase):
    _LITERAL = "short"


class ExecuteStoreResultSuccessNbtTypeCommand(CommandArgument, ExecuteCommandMixin):
    _CONVERT = float
    _TYPE = float


# @@ execute store result/success block


class ExecuteStoreResultSuccessBlockCommand(CommandLiteral):
    _LITERAL = "block"

    def __call__(
        self, position: Position.Thing, path: NbtPathAble
    ) -> "ExecuteStoreResultSuccessBlockPositionPathCommand":
        return self.position(position).path(path)

    def position(self, position: Position.Thing) -> "ExecuteStoreResultSuccessBlockPositionCommand":
        return ExecuteStoreResultSuccessBlockPositionCommand(self, position)


class ExecuteStoreResultSuccessBlockPositionCommand(CommandArgument):
    _TYPE = Position

    def path(self, path: NbtPathAble) -> "ExecuteStoreResultSuccessBlockPositionPathCommand":
        return ExecuteStoreResultSuccessBlockPositionPathCommand(self, path)


class ExecuteStoreResultSuccessBlockPositionPathCommand(
    CommandArgument, ExecuteStoreResultSuccessNbtCommandMixin
):
    _CONVERT = to_nbt_path
    _TYPE = NbtPath


# @@ execute store result/success bossbar


class ExecuteStoreResultSuccessBossbarCommand(CommandLiteral):
    _LITERAL = "bossbar"

    def __call__(self, id: BossbarID) -> "ExecuteStoreResultSuccessBossbarIDCommand":
        return self.id(id)

    def id(self, id: BossbarID) -> "ExecuteStoreResultSuccessBossbarIDCommand":
        return ExecuteStoreResultSuccessBossbarIDCommand(self, id)


class ExecuteStoreResultSuccessBossbarIDCommand(CommandArgument):
    @property
    def max(self) -> "ExecuteStoreResultSuccessBossbarIDMaxCommand":
        return ExecuteStoreResultSuccessBossbarIDMaxCommand(self)

    @property
    def value(self) -> "ExecuteStoreResultSuccessBossbarIDValueCommand":
        return ExecuteStoreResultSuccessBossbarIDValueCommand(self)


class ExecuteStoreResultSuccessBossbarIDMaxCommand(CommandLiteral, ExecuteCommandMixin):
    _LITERAL = "max"


class ExecuteStoreResultSuccessBossbarIDValueCommand(CommandLiteral, ExecuteCommandMixin):
    _LITERAL = "value"


# @@ execute store result/success entity


class ExecuteStoreResultSuccessEntityCommand(CommandLiteral):
    _LITERAL = "entity"

    def __call__(
        self, target: CommandTarget, path: NbtPathAble
    ) -> "ExecuteStoreResultSuccessEntityTargetPathCommand":
        return self.target(target).path(path)

    def target(self, target: CommandTarget) -> "ExecuteStoreResultSuccessEntityTargetCommand":
        return ExecuteStoreResultSuccessEntityTargetCommand(self, target)


class ExecuteStoreResultSuccessEntityTargetCommand(CommandArgument):
    def path(self, path: NbtPathAble) -> "ExecuteStoreResultSuccessEntityTargetPathCommand":
        return ExecuteStoreResultSuccessEntityTargetPathCommand(self, path)


class ExecuteStoreResultSuccessEntityTargetPathCommand(
    CommandArgument, ExecuteStoreResultSuccessNbtCommandMixin
):
    _CONVERT = to_nbt_path
    _TYPE = NbtPath


# @@ execute store result/success score


class ExecuteStoreResultSuccessScoreCommand(CommandLiteral):
    _LITERAL = "score"

    def __call__(
        self, target: ScoreHolder, objective: ScoreboardObjective
    ) -> "ExecuteStoreResultSuccessScoreTargetObjectiveCommand":
        return self.target(target).objective(objective)

    def target(self, target: ScoreHolder) -> "ExecuteStoreResultSuccessScoreTargetCommand":
        return ExecuteStoreResultSuccessScoreTargetCommand(self, target)


class ExecuteStoreResultSuccessScoreTargetCommand(CommandArgument):
    def objective(
        self, objective: ScoreboardObjective
    ) -> "ExecuteStoreResultSuccessScoreTargetObjectiveCommand":
        return ExecuteStoreResultSuccessScoreTargetObjectiveCommand(self, objective)


class ExecuteStoreResultSuccessScoreTargetObjectiveCommand(CommandArgument, ExecuteCommandMixin):
    pass


# @@ execute store result/success storage


class ExecuteStoreResultSuccessStorageCommand(CommandLiteral):
    _LITERAL = "storage"

    def __call__(
        self, location: StorageResourceLocation, path: NbtPathAble
    ) -> "ExecuteStoreResultSuccessStorageLocationPathCommand":
        return self.location(location).path(path)

    def location(
        self, location: StorageResourceLocation
    ) -> "ExecuteStoreResultSuccessStorageLocationCommand":
        return ExecuteStoreResultSuccessStorageLocationCommand(self, location)


class ExecuteStoreResultSuccessStorageLocationCommand(CommandArgument):
    def path(self, path: NbtPathAble) -> "ExecuteStoreResultSuccessStorageLocationPathCommand":
        return ExecuteStoreResultSuccessStorageLocationPathCommand(self, path)


class ExecuteStoreResultSuccessStorageLocationPathCommand(
    CommandArgument, ExecuteStoreResultSuccessNbtCommandMixin
):
    _CONVERT = to_nbt_path
    _TYPE = NbtPath
