from pyckaxe.command.abc.command import Command, CommandArguments, CommandLiteral


class TagTargetsAddRemoveCommandMixin:
    def __call__(self: Command, tag: str) -> 'TagTargetsAddRemoveTagCommand':
        return TagTargetsAddRemoveTagCommand(parent=self, args=(tag,))

    def tag(self: Command, tag: str) -> 'TagTargetsAddRemoveTagCommand':
        return TagTargetsAddRemoveTagCommand(parent=self, args=(tag,))


class TagCommand(CommandLiteral):
    _LITERAL = 'tag'

    def __call__(self, targets: str) -> 'TagTargetsCommand':
        return TagTargetsCommand(parent=self, args=(targets,))

    def targets(self, targets: str) -> 'TagTargetsCommand':
        return TagTargetsCommand(parent=self, args=(targets,))


class TagTargetsCommand(CommandArguments):
    @property
    def add(self: Command) -> 'TagTargetsAddCommand':
        return TagTargetsAddCommand(parent=self)

    @property
    def remove(self: Command) -> 'TagTargetsRemoveCommand':
        return TagTargetsRemoveCommand(parent=self)

    @property
    def list(self: Command) -> 'TagTargetsListCommand':
        return TagTargetsListCommand(parent=self)


class TagTargetsAddCommand(CommandLiteral, TagTargetsAddRemoveCommandMixin):
    _LITERAL = 'add'


class TagTargetsRemoveCommand(CommandLiteral, TagTargetsAddRemoveCommandMixin):
    _LITERAL = 'remove'


class TagTargetsListCommand(CommandLiteral):
    _LITERAL = 'list'


class TagTargetsAddRemoveTagCommand(CommandArguments):
    pass
