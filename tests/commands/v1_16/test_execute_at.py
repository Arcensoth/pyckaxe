from pyckaxe import selectors
from pyckaxe.commands.v1_16 import commands


def test_execute_at():
    assert "execute at" == str(commands.execute.at)


def test_execute_at_targets():
    assert "execute at @a" == str(commands.execute.at.targets(selectors.all_players))


def test_execute_at_call():
    assert "execute at @a" == str(commands.execute.at(selectors.all_players))
