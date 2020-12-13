from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.position import Position
from pyckaxe.types import CommandTarget, EntityAnchor, Rotation, UniqueCommandTarget


class TeleportCommand(CommandLiteral):
    _LITERAL = "teleport"

    def __call__(
        self, targets: CommandTarget, location: Position.Thing
    ) -> "TeleportTargetsLocationCommand":
        return self.targets(targets).location(location)

    def destination(self, destination: UniqueCommandTarget) -> "TeleportDestinationCommand":
        return TeleportDestinationCommand(self, destination)

    def location(self, location: Position.Thing) -> "TeleportLocationCommand":
        return TeleportLocationCommand(self, location)

    def targets(self, targets: CommandTarget) -> "TeleportTargetsCommand":
        return TeleportTargetsCommand(self, targets)


class TeleportDestinationCommand(CommandArgument):
    pass


class TeleportLocationCommand(CommandArgument):
    _TYPE = Position


class TeleportTargetsCommand(CommandArgument):
    def destination(self, destination: UniqueCommandTarget) -> "TeleportTargetsDestinationCommand":
        return TeleportTargetsDestinationCommand(self, destination)

    def location(self, location: Position.Thing) -> "TeleportTargetsLocationCommand":
        return TeleportTargetsLocationCommand(self, location)


class TeleportTargetsDestinationCommand(CommandArgument):
    pass


class TeleportTargetsLocationCommand(CommandArgument):
    _TYPE = Position

    def __call__(self, rotation: Rotation) -> "TeleportTargetsLocationRotationCommand":
        return self.rotation(rotation)

    @property
    def facing(self) -> "TeleportTargetsLocationFacingCommand":
        return TeleportTargetsLocationFacingCommand(self)

    def rotation(self, rotation: Rotation) -> "TeleportTargetsLocationRotationCommand":
        return TeleportTargetsLocationRotationCommand(self, rotation)


class TeleportTargetsLocationRotationCommand(CommandArgument):
    pass


class TeleportTargetsLocationFacingCommand(CommandLiteral):
    _LITERAL = "facing"

    def __call__(self, location: Position.Thing) -> "TeleportTargetsLocationFacingLocationCommand":
        return self.location(location)

    @property
    def entity(self) -> "TeleportTargetsLocationFacingEntityCommand":
        return TeleportTargetsLocationFacingEntityCommand(self)

    def location(self, location: Position.Thing) -> "TeleportTargetsLocationFacingLocationCommand":
        return TeleportTargetsLocationFacingLocationCommand(self, location)


class TeleportTargetsLocationFacingLocationCommand(CommandArgument):
    _TYPE = Position


class TeleportTargetsLocationFacingEntityCommand(CommandLiteral):
    _LITERAL = "entity"

    def __call__(
        self, entity: CommandTarget, anchor: EntityAnchor
    ) -> "TeleportTargetsLocationFacingEntityEntityAnchorCommand":
        return self.entity(entity).anchor(anchor)

    def entity(self, entity: CommandTarget) -> "TeleportTargetsLocationFacingEntityEntityCommand":
        return TeleportTargetsLocationFacingEntityEntityCommand(self, entity)


class TeleportTargetsLocationFacingEntityEntityCommand(CommandArgument):
    def anchor(
        self, anchor: EntityAnchor
    ) -> "TeleportTargetsLocationFacingEntityEntityAnchorCommand":
        return TeleportTargetsLocationFacingEntityEntityAnchorCommand(self, anchor)


class TeleportTargetsLocationFacingEntityEntityAnchorCommand(CommandArgument):
    pass
