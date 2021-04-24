from pyckaxe.command.abc.command_node import CommandArgument, CommandLiteral
from pyckaxe.types import (
    AdvancementCriteria,
    AdvancementResourceLocation,
    CommandTarget,
)


class AdvancementCommand(CommandLiteral):
    _LITERAL = "advancement"

    @property
    def grant(self) -> "AdvancementGrantCommand":
        return AdvancementGrantCommand(self)

    @property
    def revoke(self) -> "AdvancementRevokeCommand":
        return AdvancementRevokeCommand(self)


class AdvancementGRCommandLiteralBase(CommandLiteral):
    def __call__(self, targets: CommandTarget) -> "AdvancementGRTargetsCommand":
        return self.targets(targets)

    def targets(self, targets: CommandTarget) -> "AdvancementGRTargetsCommand":
        return AdvancementGRTargetsCommand(self, targets)


class AdvancementGrantCommand(AdvancementGRCommandLiteralBase):
    _LITERAL = "grant"


class AdvancementRevokeCommand(AdvancementGRCommandLiteralBase):
    _LITERAL = "revoke"


class AdvancementGRTargetsCommand(CommandArgument):
    @property
    def everything(self) -> "AdvancementGRTargetsEverythingCommand":
        return AdvancementGRTargetsEverythingCommand(self)

    @property
    def from_(self) -> "AdvancementGRTargetsFromCommand":
        return AdvancementGRTargetsFromCommand(self)

    @property
    def only(self) -> "AdvancementGRTargetsOnlyCommand":
        return AdvancementGRTargetsOnlyCommand(self)

    @property
    def through(self) -> "AdvancementGRTargetsThroughCommand":
        return AdvancementGRTargetsThroughCommand(self)

    @property
    def until(self) -> "AdvancementGRTargetsUntilCommand":
        return AdvancementGRTargetsUntilCommand(self)


class AdvancementGRTargetsEverythingCommand(CommandLiteral):
    _LITERAL = "everything"


class AdvancementGRTargetsFTUCommandLiteralBase(CommandLiteral):
    def __call__(
        self, advancement: AdvancementResourceLocation
    ) -> "AdvancementGRTargetsFTUAdvancementCommand":
        return self.advancement(advancement)

    def advancement(
        self, advancement: AdvancementResourceLocation
    ) -> "AdvancementGRTargetsFTUAdvancementCommand":
        return AdvancementGRTargetsFTUAdvancementCommand(self, advancement)


class AdvancementGRTargetsFromCommand(AdvancementGRTargetsFTUCommandLiteralBase):
    _LITERAL = "from"


class AdvancementGRTargetsOnlyCommand(CommandLiteral):
    _LITERAL = "only"

    def __call__(
        self, advancement: AdvancementResourceLocation, criteria: AdvancementCriteria
    ) -> "AdvancementGRTargetsOnlyAdvancementCriteriaCommand":
        return self.advancement(advancement).criteria(criteria)

    def advancement(
        self, advancement: AdvancementResourceLocation
    ) -> "AdvancementGRTargetsOnlyAdvancementCommand":
        return AdvancementGRTargetsOnlyAdvancementCommand(self, advancement)


class AdvancementGRTargetsOnlyAdvancementCommand(CommandArgument):
    def criteria(
        self, criteria: AdvancementCriteria
    ) -> "AdvancementGRTargetsOnlyAdvancementCriteriaCommand":
        return AdvancementGRTargetsOnlyAdvancementCriteriaCommand(self, criteria)


class AdvancementGRTargetsOnlyAdvancementCriteriaCommand(CommandArgument):
    pass


class AdvancementGRTargetsThroughCommand(AdvancementGRTargetsFTUCommandLiteralBase):
    _LITERAL = "through"


class AdvancementGRTargetsUntilCommand(AdvancementGRTargetsFTUCommandLiteralBase):
    _LITERAL = "until"


class AdvancementGRTargetsFTUAdvancementCommand(CommandArgument):
    pass
