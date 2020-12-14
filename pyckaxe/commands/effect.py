from pyckaxe.command.abc.command_node import CommandArgument, CommandLiteral
from pyckaxe.types import CommandTarget, Effect

# NOTE This command uses a different form of namespacing: nested classes.
# This results in class names with sane lengths, but conversely insane indentation. It also has the
# (arguably negligible) side-effect of polluting the namespace with sub-classes.


class EffectCommand(CommandLiteral):
    _LITERAL = "effect"

    class _Clear(CommandLiteral):
        _LITERAL = "clear"

        class _Targets(CommandArgument):
            class _Effect(CommandArgument):
                pass

            def effect(self, effect: Effect) -> _Effect:
                return self._Effect(self, effect)

        def __call__(self, targets: CommandTarget, effect: Effect) -> _Targets._Effect:
            return self.targets(targets).effect(effect)

        def targets(self, targets: CommandTarget) -> _Targets:
            return self._Targets(self, targets)

    @property
    def clear(self) -> _Clear:
        return self._Clear(self)

    class _Give(CommandLiteral):
        _LITERAL = "give"

        class _Targets(CommandArgument):
            class _Effect(CommandArgument):
                class _Seconds(CommandArgument):
                    class _Amplifier(CommandArgument):
                        class _HideParticles(CommandArgument):
                            pass

                        def hide_particles(self, hide_particles: bool) -> _HideParticles:
                            return self._HideParticles(self, hide_particles)

                    def amplifier(self, amplifier: int) -> _Amplifier:
                        return self._Amplifier(self, amplifier)

                def seconds(self, seconds: int) -> _Seconds:
                    return self._Seconds(self, seconds)

            def effect(self, effect: Effect) -> _Effect:
                return self._Effect(self, effect)

        def __call__(
            self,
            targets: CommandTarget,
            effect: Effect,
            seconds: int,
            amplifier: int,
            hide_particles: bool,
        ) -> _Targets._Effect._Seconds._Amplifier._HideParticles:
            return (
                self.targets(targets)
                .effect(effect)
                .seconds(seconds)
                .amplifier(amplifier)
                .hide_particles(hide_particles)
            )

        def targets(self, targets: CommandTarget) -> _Targets:
            return self._Targets(self, targets)

    @property
    def give(self) -> _Give:
        return self._Give(self)
