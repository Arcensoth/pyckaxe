from pyckaxe import commands, positions, selectors


def test_tp():
    assert 'tp' == str(commands.tp)


def test_tp_thoroughly():
    assert 'tp @a ~ ~ ~ facing entity @r' == str(
        commands.tp(selectors.all_players, positions.relative).facing.entity.entity(selectors.random))
