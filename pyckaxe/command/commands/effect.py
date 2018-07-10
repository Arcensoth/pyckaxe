from pyckaxe.command.abc.command import CommandArgument, CommandLiteral


class EffectCommand(CommandLiteral):
    _LITERAL = 'effect'

    @property
    def clear(self) -> 'EffectClearCommand':
        return EffectClearCommand(self)

    @property
    def give(self) -> 'EffectGiveCommand':
        return EffectGiveCommand(self)


class EffectClearCommand(CommandLiteral):
    _LITERAL = 'clear'

    def __call__(self, targets: str, effect: str) -> 'EffectClearTargetsEffectCommand':
        return self.targets(targets).effect(effect)

    def targets(self, targets: str) -> 'EffectClearTargetsCommand':
        return EffectClearTargetsCommand(self, targets)


class EffectClearTargetsCommand(CommandArgument):
    def effect(self, effect: str) -> 'EffectClearTargetsEffectCommand':
        return EffectClearTargetsEffectCommand(self, effect)


class EffectClearTargetsEffectCommand(CommandArgument):
    pass


class EffectGiveCommand(CommandLiteral):
    _LITERAL = 'give'

    def __call__(
            self, targets: str, effect: str, seconds: int, amplifier: int, hide_particles: bool
    ) -> 'EffectGiveTargetsEffectSecondsAmplifierHideParticlesCommand':
        return self.targets(targets).effect(effect).seconds(seconds).amplifier(amplifier).hide_particles(hide_particles)

    def targets(self, targets: str) -> 'EffectGiveTargetsCommand':
        return EffectGiveTargetsCommand(self, targets)


class EffectGiveTargetsCommand(CommandArgument):
    def effect(self, effect: str) -> 'EffectGiveTargetsEffectCommand':
        return EffectGiveTargetsEffectCommand(self, effect)


class EffectGiveTargetsEffectCommand(CommandArgument):
    def seconds(self, seconds: int) -> 'EffectGiveTargetsEffectSecondsCommand':
        return EffectGiveTargetsEffectSecondsCommand(self, seconds)


class EffectGiveTargetsEffectSecondsCommand(CommandArgument):
    def amplifier(self, amplifier: int) -> 'EffectGiveTargetsEffectSecondsAmplifierCommand':
        return EffectGiveTargetsEffectSecondsAmplifierCommand(self, amplifier)


class EffectGiveTargetsEffectSecondsAmplifierCommand(CommandArgument):
    def hide_particles(self, hide_particles: bool) -> 'EffectGiveTargetsEffectSecondsAmplifierHideParticlesCommand':
        return EffectGiveTargetsEffectSecondsAmplifierHideParticlesCommand(self, hide_particles)


class EffectGiveTargetsEffectSecondsAmplifierHideParticlesCommand(CommandArgument):
    pass
