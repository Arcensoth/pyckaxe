from pyckaxe.commands.v1_16 import commands


def test_execute_if_entity():
    assert "execute if entity" == str(commands.execute.if_.entity)


def test_execute_unless_entity():
    assert "execute unless entity" == str(commands.execute.unless.entity)
