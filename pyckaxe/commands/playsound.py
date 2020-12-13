from pyckaxe.command.abc.command import CommandArgument, CommandLiteral
from pyckaxe.position import Position
from pyckaxe.types import CommandTarget, Sound, SoundSource


class PlaysoundCommand(CommandLiteral):
    _LITERAL = "playsound"

    def __call__(
        self,
        sound: Sound,
        source: SoundSource,
        targets: CommandTarget,
        position: Position.Thing,
        volume: float,
        pitch: float,
        min_volume: float,
    ) -> "PlaysoundSoundSourceTargetsPositionVolumePitchMonVolumeCommand":
        return (
            self.sound(sound)
            .source(source)
            .targets(targets)
            .position(position)
            .volume(volume)
            .pitch(pitch)
            .min_volume(min_volume)
        )

    def sound(self, sound: Sound) -> "PlaysoundSoundCommand":
        return PlaysoundSoundCommand(self, sound)


class PlaysoundSoundCommand(CommandArgument):
    def source(self, source: SoundSource) -> "PlaysoundSoundSourceCommand":
        return PlaysoundSoundSourceCommand(self, source)


class PlaysoundSoundSourceCommand(CommandArgument):
    def targets(self, targets: CommandTarget) -> "PlaysoundSoundSourceTargetsCommand":
        return PlaysoundSoundSourceTargetsCommand(self, targets)


class PlaysoundSoundSourceTargetsCommand(CommandArgument):
    def position(self, position: Position.Thing) -> "PlaysoundSoundSourceTargetsPositionCommand":
        return PlaysoundSoundSourceTargetsPositionCommand(self, position)


class PlaysoundSoundSourceTargetsPositionCommand(CommandArgument):
    _TYPE = Position

    def volume(self, volume: float) -> "PlaysoundSoundSourceTargetsPositionVolumeCommand":
        return PlaysoundSoundSourceTargetsPositionVolumeCommand(self, volume)


class PlaysoundSoundSourceTargetsPositionVolumeCommand(CommandArgument):
    def pitch(self, pitch: float) -> "PlaysoundSoundSourceTargetsPositionVolumePitchCommand":
        return PlaysoundSoundSourceTargetsPositionVolumePitchCommand(self, pitch)


class PlaysoundSoundSourceTargetsPositionVolumePitchCommand(CommandArgument):
    def min_volume(
        self, min_volume: float
    ) -> "PlaysoundSoundSourceTargetsPositionVolumePitchMonVolumeCommand":
        return PlaysoundSoundSourceTargetsPositionVolumePitchMonVolumeCommand(self, min_volume)


class PlaysoundSoundSourceTargetsPositionVolumePitchMonVolumeCommand(CommandArgument):
    pass
