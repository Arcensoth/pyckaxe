from pyckaxe import commands, effects, selectors


def test_effect():
    assert 'effect' == str(commands.effect)


def test_effect_clear():
    assert 'effect clear' == str(commands.effect.clear)


def test_effect_clear_targets():
    assert 'effect clear @a' == str(commands.effect.clear.targets(selectors.all_players))


def test_effect_clear_targets_effect():
    assert 'effect clear @a minecraft:slowness' == str(
        commands.effect.clear.targets(selectors.all_players).effect(effects.slowness))


def test_effect_clear_call():
    assert 'effect clear @a minecraft:slowness' == str(commands.effect.clear(selectors.all_players, effects.slowness))


def test_effect_give():
    assert 'effect give' == str(commands.effect.give)


def test_effect_give_targets():
    assert 'effect give @a' == str(commands.effect.give.targets(selectors.all_players))


def test_effect_give_targets_effect():
    assert 'effect give @a minecraft:slowness' == str(
        commands.effect.give.targets(selectors.all_players).effect(effects.slowness))


def test_effect_give_targets_effect_seconds():
    assert 'effect give @a minecraft:slowness 30' == str(
        commands.effect.give.targets(selectors.all_players).effect(effects.slowness).seconds(30))


def test_effect_give_targets_effect_seconds_amplifier():
    assert 'effect give @a minecraft:slowness 30 2' == str(
        commands.effect.give.targets(selectors.all_players).effect(effects.slowness).seconds(30).amplifier(2))


def test_effect_give_targets_effect_seconds_amplifier_hide_particles():
    assert 'effect give @a minecraft:slowness 30 2 true' == str(
        commands.effect.give.targets(selectors.all_players).effect(effects.slowness).seconds(30).amplifier(2)
            .hide_particles(True))


def test_effect_give_call():
    assert 'effect give @a minecraft:slowness 30 2 true' == str(
        commands.effect.give(selectors.all_players, effects.slowness, 30, 2, True))
