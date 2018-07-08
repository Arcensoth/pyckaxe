from pyckaxe.command.abc.command import Command, CommandArguments, CommandLiteral


class SetblockPositionBlockCommandMixin:
    @property
    def destroy(self: Command) -> 'SetblockPositionBlockDestroyCommand':
        return SetblockPositionBlockDestroyCommand(parent=self)

    @property
    def keep(self: Command) -> 'SetblockPositionBlockKeepCommand':
        return SetblockPositionBlockKeepCommand(parent=self)

    @property
    def replace(self: Command) -> 'SetblockPositionBlockReplaceCommand':
        return SetblockPositionBlockReplaceCommand(parent=self)


class SetblockCommand(CommandLiteral):
    _LITERAL = 'setblock'

    def __call__(self, position: str = None, block: str = None) -> 'SetblockPositionBlockCommand':
        return SetblockPositionBlockCommand(parent=self, args=(position, block))


class SetblockPositionBlockCommand(CommandArguments, SetblockPositionBlockCommandMixin):
    @property
    def position(self) -> str:
        return self._args[0]

    @property
    def block(self) -> str:
        return self._args[1]


class SetblockPositionBlockDestroyCommand(CommandLiteral):
    _LITERAL = 'destroy'


class SetblockPositionBlockKeepCommand(CommandLiteral):
    _LITERAL = 'keep'


class SetblockPositionBlockReplaceCommand(CommandLiteral):
    _LITERAL = 'replace'
