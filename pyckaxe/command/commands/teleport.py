from pyckaxe.command.abc.command import CommandArgument, CommandLiteral


class TeleportCommand(CommandLiteral):
    _LITERAL = 'teleport'

    def __call__(self, targets: str, location: str) -> 'TeleportTargetsLocationCommand':
        return self.targets(targets).location(location)

    def destination(self, destination: str) -> 'TeleportDestinationCommand':
        return TeleportDestinationCommand(self, destination)

    def location(self, location: str) -> 'TeleportLocationCommand':
        return TeleportLocationCommand(self, location)

    def targets(self, targets: str) -> 'TeleportTargetsCommand':
        return TeleportTargetsCommand(self, targets)


class TeleportDestinationCommand(CommandArgument):
    pass


class TeleportLocationCommand(CommandArgument):
    pass


class TeleportTargetsCommand(CommandArgument):
    def destination(self, destination: str) -> 'TeleportTargetsDestinationCommand':
        return TeleportTargetsDestinationCommand(self, destination)

    def location(self, location: str) -> 'TeleportTargetsLocationCommand':
        return TeleportTargetsLocationCommand(self, location)


class TeleportTargetsDestinationCommand(CommandArgument):
    pass


class TeleportTargetsLocationCommand(CommandArgument):
    def __call__(self, rotation: str) -> 'TeleportTargetsLocationRotationCommand':
        return TeleportTargetsLocationRotationCommand(self, rotation)

    @property
    def facing(self) -> 'TeleportTargetsLocationFacingCommand':
        return TeleportTargetsLocationFacingCommand(self)

    def rotation(self, rotation: str) -> 'TeleportTargetsLocationRotationCommand':
        return TeleportTargetsLocationRotationCommand(self, rotation)


class TeleportTargetsLocationRotationCommand(CommandArgument):
    pass


class TeleportTargetsLocationFacingCommand(CommandLiteral):
    _LITERAL = 'facing'

    def __call__(self, location: str) -> 'TeleportTargetsLocationFacingLocationCommand':
        return TeleportTargetsLocationFacingLocationCommand(self, location)

    @property
    def entity(self) -> 'TeleportTargetsLocationFacingEntityCommand':
        return TeleportTargetsLocationFacingEntityCommand(self)

    def location(self, location: str) -> 'TeleportTargetsLocationFacingLocationCommand':
        return TeleportTargetsLocationFacingLocationCommand(self, location)


class TeleportTargetsLocationFacingLocationCommand(CommandArgument):
    pass


class TeleportTargetsLocationFacingEntityCommand(CommandLiteral):
    _LITERAL = 'entity'

    def __call__(self, entity: str, anchor: str) -> 'TeleportTargetsLocationFacingEntityEntityAnchorCommand':
        return self.entity(entity).anchor(anchor)

    def entity(self, entity: str) -> 'TeleportTargetsLocationFacingEntityEntityCommand':
        return TeleportTargetsLocationFacingEntityEntityCommand(self, entity)


class TeleportTargetsLocationFacingEntityEntityCommand(CommandArgument):
    def anchor(self, anchor: str) -> 'TeleportTargetsLocationFacingEntityEntityAnchorCommand':
        return TeleportTargetsLocationFacingEntityEntityAnchorCommand(self, anchor)


class TeleportTargetsLocationFacingEntityEntityAnchorCommand(CommandArgument):
    pass
