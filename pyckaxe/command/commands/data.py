from pyckaxe.command.abc.command import CommandLiteral


class DataCommand(CommandLiteral):
    _LITERAL = 'data'


# data get


class DataGetCommand(CommandLiteral):
    _LITERAL = 'get'


class DataGetBlockCommand(CommandLiteral):
    _LITERAL = 'block'


class DataGetEntityCommand(CommandLiteral):
    _LITERAL = 'entity'


# data merge


class DataMergeCommand(CommandLiteral):
    _LITERAL = 'merge'


class DataMergeBlockCommand(CommandLiteral):
    _LITERAL = 'block'


class DataMergeEntityCommand(CommandLiteral):
    _LITERAL = 'entity'


# data remove


class DataRemoveCommand(CommandLiteral):
    _LITERAL = 'remove'


class DataRemoveBlockCommand(CommandLiteral):
    _LITERAL = 'block'


class DataRemoveEntityCommand(CommandLiteral):
    _LITERAL = 'entity'
