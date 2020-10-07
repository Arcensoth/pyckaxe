from pyckaxe import positions, selectors
from pyckaxe.commands.v1_16 import commands


def test_tp():
    assert "tp" == str(commands.tp)


def test_tp_thoroughly():
    assert "tp @a ~ ~ ~ facing entity @r" == str(
        commands.tp(selectors.all_players, positions.relative).facing.entity.entity(
            selectors.random
        )
    )
