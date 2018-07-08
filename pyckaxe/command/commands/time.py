from pyckaxe.command.abc.command import Command, CommandArguments, CommandLiteral


class TimeCommandMixin:
    @property
    def add(self: Command) -> 'TimeAddCommand':
        return TimeAddCommand(parent=self)

    @property
    def query(self: Command) -> 'TimeQueryCommand':
        return TimeQueryCommand(parent=self)

    @property
    def set_(self: Command) -> 'TimeSetCommand':
        return TimeSetCommand(parent=self)


class TimeAddCommandMixin:
    def time(self: Command, time: int) -> 'TimeAddTimeCommand':
        return TimeAddTimeCommand(parent=self, args=(time,))


class TimeQueryCommandMixin:
    @property
    def day(self: Command) -> 'TimeQueryDayCommand':
        return TimeQueryDayCommand(parent=self)

    @property
    def daytime(self: Command) -> 'TimeQueryDaytimeCommand':
        return TimeQueryDaytimeCommand(parent=self)

    @property
    def gametime(self: Command) -> 'TimeQueryGametimeCommand':
        return TimeQueryGametimeCommand(parent=self)


class TimeSetCommandMixin:
    def time(self: Command, time: int) -> 'TimeSetTimeCommand':
        return TimeSetTimeCommand(parent=self, args=(time,))

    @property
    def day(self: Command) -> 'TimeSetDayCommand':
        return TimeSetDayCommand(parent=self)

    @property
    def midnight(self: Command) -> 'TimeSetMidnightCommand':
        return TimeSetMidnightCommand(parent=self)

    @property
    def night(self: Command) -> 'TimeSetNightCommand':
        return TimeSetNightCommand(parent=self)

    @property
    def noon(self: Command) -> 'TimeSetNoonCommand':
        return TimeSetNoonCommand(parent=self)


class TimeCommand(CommandLiteral, TimeCommandMixin):
    _LITERAL = 'time'


class TimeAddCommand(CommandLiteral, TimeAddCommandMixin):
    _LITERAL = 'add'

    def __call__(self, time: int = None) -> 'TimeAddTimeCommand':
        return TimeAddTimeCommand(parent=self, args=(time,))


class TimeAddTimeCommand(CommandArguments):
    pass


class TimeQueryCommand(CommandLiteral, TimeQueryCommandMixin):
    _LITERAL = 'query'


class TimeQueryDayCommand(CommandLiteral):
    _LITERAL = 'day'


class TimeQueryDaytimeCommand(CommandLiteral):
    _LITERAL = 'daytime'


class TimeQueryGametimeCommand(CommandLiteral):
    _LITERAL = 'gametime'


class TimeSetCommand(CommandLiteral, TimeSetCommandMixin):
    _LITERAL = 'set'

    def __call__(self, time: int = None) -> 'TimeSetTimeCommand':
        return TimeSetTimeCommand(parent=self, args=(time,))


class TimeSetTimeCommand(CommandArguments):
    pass


class TimeSetDayCommand(CommandLiteral):
    _LITERAL = 'day'


class TimeSetMidnightCommand(CommandLiteral):
    _LITERAL = 'midnight'


class TimeSetNightCommand(CommandLiteral):
    _LITERAL = 'night'


class TimeSetNoonCommand(CommandLiteral):
    _LITERAL = 'noon'
