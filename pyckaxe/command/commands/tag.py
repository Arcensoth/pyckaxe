from pyckaxe.command.abc.command import Command, CommandArguments, CommandLiteral


class TagTargetsCommandMixin:
    @property
    def add(self: Command) -> 'TagTargetsAddCommand':
        return TagTargetsAddCommand(parent=self)

    @property
    def remove(self: Command) -> 'TagTargetsRemoveCommand':
        return TagTargetsRemoveCommand(parent=self)

    @property
    def list(self: Command) -> 'TagTargetsListCommand':
        return TagTargetsListCommand(parent=self)


class TagCommand(CommandLiteral):
    _LITERAL = 'tag'

    def __call__(self, targets: str) -> 'TagTargetsCommand':
        return TagTargetsCommand(parent=self, args=(targets,))

    def targets(self, targets: str) -> 'TagTargetsCommand':
        return TagTargetsCommand(parent=self, args=(targets,))


class TagTargetsCommand(CommandArguments, TagTargetsCommandMixin):
    pass


class TagTargetsAddCommand(CommandLiteral):
    _LITERAL = 'add'

    def __call__(self, tag: str) -> 'TagTargetsAddTagCommand':
        return TagTargetsAddTagCommand(parent=self, args=(tag,))

    def tag(self, tag: str) -> 'TagTargetsAddTagCommand':
        return TagTargetsAddTagCommand(parent=self, args=(tag,))


class TagTargetsRemoveCommand(CommandLiteral):
    _LITERAL = 'remove'

    def __call__(self, tag: str) -> 'TagTargetsRemoveTagCommand':
        return TagTargetsRemoveTagCommand(parent=self, args=(tag,))

    def tag(self, tag: str) -> 'TagTargetsRemoveTagCommand':
        return TagTargetsRemoveTagCommand(parent=self, args=(tag,))


class TagTargetsListCommand(CommandLiteral):
    _LITERAL = 'list'


class TagTargetsAddTagCommand(CommandArguments):
    pass


class TagTargetsRemoveTagCommand(CommandArguments):
    pass
