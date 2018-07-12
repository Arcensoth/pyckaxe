from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.types import CommandTarget, EntityAnchor, Position, Rotation, UniqueCommandTarget


class TeleportCommand(CommandLiteral):
    _LITERAL = 'teleport'

    def __call__(self, targets: CommandTarget, location: Position) -> 'TeleportTargetsLocationCommand':
        return self.targets(targets).location(location)

    def destination(self, destination: UniqueCommandTarget) -> 'TeleportDestinationCommand':
        return TeleportDestinationCommand(self, destination)

    def location(self, location: Position) -> 'TeleportLocationCommand':
        return TeleportLocationCommand(self, location)

    def targets(self, targets: CommandTarget) -> 'TeleportTargetsCommand':
        return TeleportTargetsCommand(self, targets)


class TeleportDestinationCommand(CommandArgument):
    pass


class TeleportLocationCommand(CommandArgument):
    pass


class TeleportTargetsCommand(CommandArgument):
    def destination(self, destination: UniqueCommandTarget) -> 'TeleportTargetsDestinationCommand':
        return TeleportTargetsDestinationCommand(self, destination)

    def location(self, location: Position) -> 'TeleportTargetsLocationCommand':
        return TeleportTargetsLocationCommand(self, location)


class TeleportTargetsDestinationCommand(CommandArgument):
    pass


class TeleportTargetsLocationCommand(CommandArgument):
    def __call__(self, rotation: Rotation) -> 'TeleportTargetsLocationRotationCommand':
        return self.rotation(rotation)

    @property
    def facing(self) -> 'TeleportTargetsLocationFacingCommand':
        return TeleportTargetsLocationFacingCommand(self)

    def rotation(self, rotation: Rotation) -> 'TeleportTargetsLocationRotationCommand':
        return TeleportTargetsLocationRotationCommand(self, rotation)


class TeleportTargetsLocationRotationCommand(CommandArgument):
    pass


class TeleportTargetsLocationFacingCommand(CommandLiteral):
    _LITERAL = 'facing'

    def __call__(self, location: Position) -> 'TeleportTargetsLocationFacingLocationCommand':
        return self.location(location)

    @property
    def entity(self) -> 'TeleportTargetsLocationFacingEntityCommand':
        return TeleportTargetsLocationFacingEntityCommand(self)

    def location(self, location: Position) -> 'TeleportTargetsLocationFacingLocationCommand':
        return TeleportTargetsLocationFacingLocationCommand(self, location)


class TeleportTargetsLocationFacingLocationCommand(CommandArgument):
    pass


class TeleportTargetsLocationFacingEntityCommand(CommandLiteral):
    _LITERAL = 'entity'

    def __call__(
            self, entity: CommandTarget, anchor: EntityAnchor
    ) -> 'TeleportTargetsLocationFacingEntityEntityAnchorCommand':
        return self.entity(entity).anchor(anchor)

    def entity(self, entity: CommandTarget) -> 'TeleportTargetsLocationFacingEntityEntityCommand':
        return TeleportTargetsLocationFacingEntityEntityCommand(self, entity)


class TeleportTargetsLocationFacingEntityEntityCommand(CommandArgument):
    def anchor(self, anchor: EntityAnchor) -> 'TeleportTargetsLocationFacingEntityEntityAnchorCommand':
        return TeleportTargetsLocationFacingEntityEntityAnchorCommand(self, anchor)


class TeleportTargetsLocationFacingEntityEntityAnchorCommand(CommandArgument):
    pass
