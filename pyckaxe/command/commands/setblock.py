from pyckaxe.command.abc.command import Command, CommandArguments, CommandLiteral


class SetblockCommand(CommandLiteral):
    _LITERAL = 'setblock'

    def __call__(self, position: str = None, block: str = None) -> 'SetblockPositionBlockCommand':
        return SetblockPositionBlockCommand(parent=self, args=(position, block))

    def position(self, position: str) -> 'SetblockPositionCommand':
        return SetblockPositionCommand(parent=self, args=(position,))


class SetblockPositionCommand(CommandArguments):
    def block(self, block: str) -> 'SetblockPositionBlockCommand':
        return SetblockPositionBlockCommand(parent=self._parent, args=(*self._args, block))


class SetblockPositionBlockCommand(CommandArguments):
    @property
    def destroy(self: Command) -> 'SetblockPositionBlockDestroyCommand':
        return SetblockPositionBlockDestroyCommand(parent=self)

    @property
    def keep(self: Command) -> 'SetblockPositionBlockKeepCommand':
        return SetblockPositionBlockKeepCommand(parent=self)

    @property
    def replace(self: Command) -> 'SetblockPositionBlockReplaceCommand':
        return SetblockPositionBlockReplaceCommand(parent=self)


class SetblockPositionBlockDestroyCommand(CommandLiteral):
    _LITERAL = 'destroy'


class SetblockPositionBlockKeepCommand(CommandLiteral):
    _LITERAL = 'keep'


class SetblockPositionBlockReplaceCommand(CommandLiteral):
    _LITERAL = 'replace'
