from pyckaxe.command.abc.command import CommandArguments, CommandLiteral


class TeleportCommand(CommandLiteral):
    _LITERAL = 'teleport'

    def __call__(self, targets: str = None, location: str = None) -> 'TeleportTargetsLocationCommand':
        return TeleportTargetsLocationCommand(parent=self, args=(targets, location))

    def destination(self, destination: str):
        return TeleportDestinationCommand(parent=self, args=(destination,))

    def location(self, location: str):
        return TeleportLocationCommand(parent=self, args=(location,))

    def targets(self, targets: str) -> 'TeleportTargetsCommand':
        return TeleportTargetsCommand(parent=self, args=(targets,))


class TeleportDestinationCommand(CommandArguments):
    pass


class TeleportLocationCommand(CommandArguments):
    pass


class TeleportTargetsCommand(CommandArguments):
    def destination(self, destination: str) -> 'TeleportTargetsDestinationCommand':
        return TeleportTargetsDestinationCommand(parent=self._parent, args=(*self._args, destination))

    def location(self, location: str) -> 'TeleportTargetsLocationCommand':
        return TeleportTargetsLocationCommand(parent=self._parent, args=(*self._args, location))


class TeleportTargetsDestinationCommand(CommandArguments):
    pass


class TeleportTargetsLocationCommand(CommandArguments):
    def __call__(self, rotation: str = None) -> 'TeleportTargetsLocationRotationCommand':
        return TeleportTargetsLocationRotationCommand(parent=self, args=(rotation,))

    @property
    def facing(self) -> 'TeleportTargetsLocationFacingCommand':
        return TeleportTargetsLocationFacingCommand(parent=self)

    def rotation(self, rotation: str) -> 'TeleportTargetsLocationRotationCommand':
        return TeleportTargetsLocationRotationCommand(parent=self, args=(rotation,))


class TeleportTargetsLocationRotationCommand(CommandArguments):
    pass


class TeleportTargetsLocationFacingCommand(CommandLiteral):
    _LITERAL = 'facing'

    def __call__(self, location: str = None) -> 'TeleportTargetsLocationFacingLocationCommand':
        return TeleportTargetsLocationFacingLocationCommand(parent=self, args=(location,))

    @property
    def entity(self) -> 'TeleportTargetsLocationFacingEntityCommand':
        return TeleportTargetsLocationFacingEntityCommand(parent=self)

    def location(self, location: str) -> 'TeleportTargetsLocationFacingLocationCommand':
        return TeleportTargetsLocationFacingLocationCommand(parent=self, args=(location,))


class TeleportTargetsLocationFacingLocationCommand(CommandArguments):
    pass


class TeleportTargetsLocationFacingEntityCommand(CommandLiteral):
    _LITERAL = 'entity'

    def __call__(
            self, entity: str = None, anchor: str = None
    ) -> 'TeleportTargetsLocationFacingEntityEntityAnchorCommand':
        return TeleportTargetsLocationFacingEntityEntityAnchorCommand(parent=self, args=(entity, anchor))

    def entity(self, entity: str) -> 'TeleportTargetsLocationFacingEntityEntityCommand':
        return TeleportTargetsLocationFacingEntityEntityCommand(parent=self, args=(entity,))


class TeleportTargetsLocationFacingEntityEntityCommand(CommandArguments):
    def anchor(self, anchor: str) -> 'TeleportTargetsLocationFacingEntityEntityAnchorCommand':
        return TeleportTargetsLocationFacingEntityEntityAnchorCommand(parent=self._parent, args=(*self._args, anchor,))


class TeleportTargetsLocationFacingEntityEntityAnchorCommand(CommandArguments):
    pass
