from pyckaxe.command.abc.command import CommandArgument, CommandLiteral


class TimeCommand(CommandLiteral):
    _LITERAL = "time"

    @property
    def add(self) -> "TimeAddCommand":
        return TimeAddCommand(self)

    @property
    def query(self) -> "TimeQueryCommand":
        return TimeQueryCommand(self)

    @property
    def set(self) -> "TimeSetCommand":
        return TimeSetCommand(self)


class TimeAddCommand(CommandLiteral):
    _LITERAL = "add"

    def __call__(self, time: int) -> "TimeAddTimeCommand":
        return self.time(time)

    def time(self, time: int) -> "TimeAddTimeCommand":
        return TimeAddTimeCommand(self, time)


class TimeAddTimeCommand(CommandArgument):
    pass


class TimeQueryCommand(CommandLiteral):
    _LITERAL = "query"

    @property
    def day(self) -> "TimeQueryDayCommand":
        return TimeQueryDayCommand(self)

    @property
    def daytime(self) -> "TimeQueryDaytimeCommand":
        return TimeQueryDaytimeCommand(self)

    @property
    def gametime(self) -> "TimeQueryGametimeCommand":
        return TimeQueryGametimeCommand(self)


class TimeQueryDayCommand(CommandLiteral):
    _LITERAL = "day"


class TimeQueryDaytimeCommand(CommandLiteral):
    _LITERAL = "daytime"


class TimeQueryGametimeCommand(CommandLiteral):
    _LITERAL = "gametime"


class TimeSetCommand(CommandLiteral):
    _LITERAL = "set"

    def __call__(self, time: int) -> "TimeSetTimeCommand":
        return self.time(time)

    def time(self, time: int) -> "TimeSetTimeCommand":
        return TimeSetTimeCommand(self, time)

    @property
    def day(self) -> "TimeSetDayCommand":
        return TimeSetDayCommand(self)

    @property
    def midnight(self) -> "TimeSetMidnightCommand":
        return TimeSetMidnightCommand(self)

    @property
    def night(self) -> "TimeSetNightCommand":
        return TimeSetNightCommand(self)

    @property
    def noon(self) -> "TimeSetNoonCommand":
        return TimeSetNoonCommand(self)


class TimeSetTimeCommand(CommandArgument):
    pass


class TimeSetDayCommand(CommandLiteral):
    _LITERAL = "day"


class TimeSetMidnightCommand(CommandLiteral):
    _LITERAL = "midnight"


class TimeSetNightCommand(CommandLiteral):
    _LITERAL = "night"


class TimeSetNoonCommand(CommandLiteral):
    _LITERAL = "noon"
