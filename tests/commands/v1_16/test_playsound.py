from pyckaxe import positions, selectors, sound_sources
from pyckaxe.commands.v1_16 import commands


def test_playsound():
    assert "playsound" == str(commands.playsound)


def test_playsound_sound():
    assert "playsound ambient.cave" == str(commands.playsound.sound("ambient.cave"))


def test_playsound_sound_source():
    assert "playsound ambient.cave ambient" == str(
        commands.playsound.sound("ambient.cave").source(sound_sources.ambient)
    )


def test_playsound_sound_source_targets():
    assert "playsound ambient.cave ambient @a" == str(
        commands.playsound.sound("ambient.cave")
        .source(sound_sources.ambient)
        .targets(selectors.all_players)
    )


def test_playsound_sound_source_targets_position():
    assert "playsound ambient.cave ambient @a ~ ~ ~" == str(
        commands.playsound.sound("ambient.cave")
        .source(sound_sources.ambient)
        .targets(selectors.all_players)
        .position(positions.relative)
    )


def test_playsound_sound_source_targets_position_volume():
    assert "playsound ambient.cave ambient @a ~ ~ ~ 2.0" == str(
        commands.playsound.sound("ambient.cave")
        .source(sound_sources.ambient)
        .targets(selectors.all_players)
        .position(positions.relative)
        .volume(2.0)
    )


def test_playsound_sound_source_targets_position_volume_pitch():
    assert "playsound ambient.cave ambient @a ~ ~ ~ 2.0 1.5" == str(
        commands.playsound.sound("ambient.cave")
        .source(sound_sources.ambient)
        .targets(selectors.all_players)
        .position(positions.relative)
        .volume(2.0)
        .pitch(1.5)
    )


def test_playsound_sound_source_targets_position_volume_pitch_min_volume():
    assert "playsound ambient.cave ambient @a ~ ~ ~ 2.0 1.5 0.5" == str(
        commands.playsound.sound("ambient.cave")
        .source(sound_sources.ambient)
        .targets(selectors.all_players)
        .position(positions.relative)
        .volume(2.0)
        .pitch(1.5)
        .min_volume(0.5)
    )


def test_playsound_call():
    assert "playsound ambient.cave ambient @a ~ ~ ~ 2.0 1.5 0.5" == str(
        commands.playsound(
            "ambient.cave",
            sound_sources.ambient,
            selectors.all_players,
            positions.relative,
            2.0,
            1.5,
            0.5,
        )
    )