from pyckaxe import commands, selectors


def test_tp():
    assert "tp" == str(commands.tp)


def test_tp_thoroughly():
    assert "tp @a ~ ~ ~ facing entity @r" == str(
        commands.tp(selectors.all_players, [0, 0, 0]).facing.entity.entity(selectors.random)
    )
