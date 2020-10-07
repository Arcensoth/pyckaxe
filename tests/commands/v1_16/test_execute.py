from pyckaxe.commands.v1_16 import commands


def test_execute():
    assert "execute" == str(commands.execute)


def test_execute_if():
    assert "execute if" == str(commands.execute.if_)


def test_execute_unless():
    assert "execute unless" == str(commands.execute.unless)
