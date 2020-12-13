from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.types import (
    ScoreboardCriteria,
    ScoreboardObjective,
    ScoreboardOperation,
    ScoreboardSlot,
    ScoreHolder,
    TextComponent,
)


class ScoreboardPlayersARSMixin:
    def __call__(
        self, targets: ScoreHolder, objective: ScoreboardObjective, score: int
    ) -> "ScoreboardPlayersARSTargetsObjectiveScoreCommand":
        return self.targets(targets).objective(objective).score(score)

    def targets(self, targets: ScoreHolder) -> "ScoreboardPlayersARSTargetsCommand":
        return ScoreboardPlayersARSTargetsCommand(self, targets)


class ScoreboardPlayersEGRMixin:
    def __call__(
        self, targets: ScoreHolder, objective: ScoreboardObjective
    ) -> "ScoreboardPlayersEGTargetsObjectiveCommand":
        return self.targets(targets).objective(objective)

    def targets(self, targets: ScoreHolder) -> "ScoreboardPlayersEGTargetsCommand":
        return ScoreboardPlayersEGTargetsCommand(self, targets)


class ScoreboardCommand(CommandLiteral):
    _LITERAL = "scoreboard"

    @property
    def objectives(self) -> "ScoreboardObjectivesCommand":
        return ScoreboardObjectivesCommand(self)

    @property
    def players(self) -> "ScoreboardPlayersCommand":
        return ScoreboardPlayersCommand(self)


# scoreboard objectives


class ScoreboardObjectivesCommand(CommandLiteral):
    _LITERAL = "objectives"

    @property
    def add(self) -> "ScoreboardObjectivesAddCommand":
        return ScoreboardObjectivesAddCommand(self)

    @property
    def list(self) -> "ScoreboardObjectivesListCommand":
        return ScoreboardObjectivesListCommand(self)

    @property
    def modify(self) -> "ScoreboardObjectivesModifyCommand":
        return ScoreboardObjectivesModifyCommand(self)

    @property
    def remove(self) -> "ScoreboardObjectivesRemoveCommand":
        return ScoreboardObjectivesRemoveCommand(self)

    @property
    def setdisplay(self) -> "ScoreboardObjectivesSetdisplayCommand":
        return ScoreboardObjectivesSetdisplayCommand(self)


class ScoreboardObjectivesAddCommand(CommandLiteral):
    _LITERAL = "add"

    def __call__(
        self,
        objective: ScoreboardObjective,
        criteria: ScoreboardCriteria,
        display_name: TextComponent,
    ) -> "ScoreboardObjectivesAddObjectiveCriteriaDisplayNameCommand":
        return self.objective(objective).criteria(criteria).display_name(display_name)

    def objective(
        self, objective: ScoreboardObjective
    ) -> "ScoreboardObjectivesAddObjectiveCommand":
        return ScoreboardObjectivesAddObjectiveCommand(self, objective)


class ScoreboardObjectivesAddObjectiveCommand(CommandArgument):
    def criteria(
        self, criteria: ScoreboardCriteria
    ) -> "ScoreboardObjectivesAddObjectiveCriteriaCommand":
        return ScoreboardObjectivesAddObjectiveCriteriaCommand(self, criteria)


class ScoreboardObjectivesAddObjectiveCriteriaCommand(CommandArgument):
    def display_name(
        self, display_name: TextComponent
    ) -> "ScoreboardObjectivesAddObjectiveCriteriaDisplayNameCommand":
        return ScoreboardObjectivesAddObjectiveCriteriaDisplayNameCommand(self, display_name)


class ScoreboardObjectivesAddObjectiveCriteriaDisplayNameCommand(CommandArgument):
    pass


class ScoreboardObjectivesListCommand(CommandLiteral):
    _LITERAL = "list"


class ScoreboardObjectivesModifyCommand(CommandLiteral):
    _LITERAL = "modify"

    def __call__(
        self, objective: ScoreboardObjective
    ) -> "ScoreboardObjectivesModifyObjectiveCommand":
        return self.objective(objective)

    def objective(
        self, objective: ScoreboardObjective
    ) -> "ScoreboardObjectivesModifyObjectiveCommand":
        return ScoreboardObjectivesModifyObjectiveCommand(self, objective)


class ScoreboardObjectivesModifyObjectiveCommand(CommandArgument):
    @property
    def displayname(self) -> "ScoreboardObjectivesModifyObjectiveDisplaynameCommand":
        return ScoreboardObjectivesModifyObjectiveDisplaynameCommand(self)


class ScoreboardObjectivesModifyObjectiveDisplaynameCommand(CommandLiteral):
    _LITERAL = "displayname"

    def __call__(
        self, display_name: TextComponent
    ) -> "ScoreboardObjectivesModifyObjectiveDisplaynameDisplayNameCommand":
        return self.display_name(display_name)

    def display_name(
        self, display_name: TextComponent
    ) -> "ScoreboardObjectivesModifyObjectiveDisplaynameDisplayNameCommand":
        return ScoreboardObjectivesModifyObjectiveDisplaynameDisplayNameCommand(self, display_name)


class ScoreboardObjectivesModifyObjectiveDisplaynameDisplayNameCommand(CommandArgument):
    pass


class ScoreboardObjectivesRemoveCommand(CommandLiteral):
    _LITERAL = "remove"

    def __call__(
        self, objective: ScoreboardObjective
    ) -> "ScoreboardObjectivesRemoveObjectiveCommand":
        return self.objective(objective)

    def objective(
        self, objective: ScoreboardObjective
    ) -> "ScoreboardObjectivesRemoveObjectiveCommand":
        return ScoreboardObjectivesRemoveObjectiveCommand(self, objective)


class ScoreboardObjectivesRemoveObjectiveCommand(CommandArgument):
    pass


class ScoreboardObjectivesSetdisplayCommand(CommandLiteral):
    _LITERAL = "setdisplay"

    def __call__(
        self, slot: ScoreboardSlot, objective: ScoreboardObjective
    ) -> "ScoreboardObjectivesSetdisplaySlotObjectiveCommand":
        return self.slot(slot).objective(objective)

    def slot(self, slot: ScoreboardSlot) -> "ScoreboardObjectivesSetdisplaySlotCommand":
        return ScoreboardObjectivesSetdisplaySlotCommand(self, slot)


class ScoreboardObjectivesSetdisplaySlotCommand(CommandArgument):
    def objective(
        self, objective: ScoreboardObjective
    ) -> "ScoreboardObjectivesSetdisplaySlotObjectiveCommand":
        return ScoreboardObjectivesSetdisplaySlotObjectiveCommand(self, objective)


class ScoreboardObjectivesSetdisplaySlotObjectiveCommand(CommandArgument):
    pass


# scoreboard players


class ScoreboardPlayersCommand(CommandLiteral):
    _LITERAL = "players"

    @property
    def add(self) -> "ScoreboardPlayersAddCommand":
        return ScoreboardPlayersAddCommand(self)

    @property
    def enable(self) -> "ScoreboardPlayersEnableCommand":
        return ScoreboardPlayersEnableCommand(self)

    @property
    def get(self) -> "ScoreboardPlayersGetCommand":
        return ScoreboardPlayersGetCommand(self)

    @property
    def list(self) -> "ScoreboardPlayersListCommand":
        return ScoreboardPlayersListCommand(self)

    @property
    def operation(self) -> "ScoreboardPlayersOperationCommand":
        return ScoreboardPlayersOperationCommand(self)

    @property
    def remove(self) -> "ScoreboardPlayersRemoveCommand":
        return ScoreboardPlayersRemoveCommand(self)

    @property
    def reset(self) -> "ScoreboardPlayersResetCommand":
        return ScoreboardPlayersResetCommand(self)

    @property
    def set(self) -> "ScoreboardPlayersSetCommand":
        return ScoreboardPlayersSetCommand(self)


class ScoreboardPlayersAddCommand(CommandLiteral, ScoreboardPlayersARSMixin):
    _LITERAL = "add"


class ScoreboardPlayersEnableCommand(CommandLiteral, ScoreboardPlayersEGRMixin):
    _LITERAL = "enable"


class ScoreboardPlayersGetCommand(CommandLiteral, ScoreboardPlayersEGRMixin):
    _LITERAL = "get"


class ScoreboardPlayersListCommand(CommandLiteral):
    _LITERAL = "list"

    def __call__(self, targets: ScoreHolder) -> "ScoreboardPlayersListTargetsCommand":
        return self.targets(targets)

    def targets(self, targets: ScoreHolder) -> "ScoreboardPlayersListTargetsCommand":
        return ScoreboardPlayersListTargetsCommand(self, targets)


class ScoreboardPlayersListTargetsCommand(CommandArgument):
    pass


class ScoreboardPlayersOperationCommand(CommandLiteral):
    _LITERAL = "operation"

    def __call__(
        self,
        targets: ScoreHolder,
        target_objective: ScoreboardObjective,
        operation: ScoreboardOperation,
        source: ScoreHolder,
        source_objective: ScoreboardObjective,
    ) -> "ScoreboardPlayersOperationTargetsObjectiveOperationSourceObjectiveCommand":
        return (
            self.targets(targets)
            .objective(target_objective)
            .operation(operation)
            .source(source)
            .objective(source_objective)
        )

    def targets(self, targets: ScoreHolder) -> "ScoreboardPlayersOperationTargetsCommand":
        return ScoreboardPlayersOperationTargetsCommand(self, targets)


class ScoreboardPlayersOperationTargetsCommand(CommandArgument):
    def objective(
        self, objective: ScoreboardObjective
    ) -> "ScoreboardPlayersOperationTargetsObjectiveCommand":
        return ScoreboardPlayersOperationTargetsObjectiveCommand(self, objective)


class ScoreboardPlayersOperationTargetsObjectiveCommand(CommandArgument):
    def operation(
        self, operation: ScoreboardOperation
    ) -> "ScoreboardPlayersOperationTargetsObjectiveOperationCommand":
        return ScoreboardPlayersOperationTargetsObjectiveOperationCommand(self, operation)


class ScoreboardPlayersOperationTargetsObjectiveOperationCommand(CommandArgument):
    def source(
        self, source: ScoreHolder
    ) -> "ScoreboardPlayersOperationTargetsObjectiveOperationSourceCommand":
        return ScoreboardPlayersOperationTargetsObjectiveOperationSourceCommand(self, source)


class ScoreboardPlayersOperationTargetsObjectiveOperationSourceCommand(CommandArgument):
    def objective(
        self, objective: ScoreboardObjective
    ) -> "ScoreboardPlayersOperationTargetsObjectiveOperationSourceObjectiveCommand":
        return ScoreboardPlayersOperationTargetsObjectiveOperationSourceObjectiveCommand(
            self, objective
        )


class ScoreboardPlayersOperationTargetsObjectiveOperationSourceObjectiveCommand(CommandArgument):
    pass


class ScoreboardPlayersRemoveCommand(CommandLiteral, ScoreboardPlayersARSMixin):
    _LITERAL = "remove"


class ScoreboardPlayersResetCommand(CommandLiteral, ScoreboardPlayersEGRMixin):
    _LITERAL = "reset"


class ScoreboardPlayersSetCommand(CommandLiteral, ScoreboardPlayersARSMixin):
    _LITERAL = "set"


# scoreboard players add/remove/set


class ScoreboardPlayersARSTargetsCommand(CommandArgument):
    def objective(
        self, objective: ScoreboardObjective
    ) -> "ScoreboardPlayersARSTargetsObjectiveCommand":
        return ScoreboardPlayersARSTargetsObjectiveCommand(self, objective)


class ScoreboardPlayersARSTargetsObjectiveCommand(CommandArgument):
    def score(self, score: int) -> "ScoreboardPlayersARSTargetsObjectiveScoreCommand":
        return ScoreboardPlayersARSTargetsObjectiveScoreCommand(self, score)


class ScoreboardPlayersARSTargetsObjectiveScoreCommand(CommandArgument):
    pass


# scoreboard players enable/get/reset


class ScoreboardPlayersEGTargetsCommand(CommandArgument):
    def objective(
        self, objective: ScoreboardObjective
    ) -> "ScoreboardPlayersEGTargetsObjectiveCommand":
        return ScoreboardPlayersEGTargetsObjectiveCommand(self, objective)


class ScoreboardPlayersEGTargetsObjectiveCommand(CommandArgument):
    pass
