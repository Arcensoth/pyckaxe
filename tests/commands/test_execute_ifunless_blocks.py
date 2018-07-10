from pyckaxe import commands


def test_execute_if_blocks():
    assert 'execute if blocks' == str(commands.execute.if_.blocks)


def test_execute_unless_blocks():
    assert 'execute unless blocks' == str(commands.execute.unless.blocks)
