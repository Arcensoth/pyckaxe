from pyckaxe.commands.v1_16 import commands


def test_execute_if_score():
    assert "execute if score" == str(commands.execute.if_.score)


def test_execute_unless_score():
    assert "execute unless score" == str(commands.execute.unless.score)
