from pyckaxe import commands


def test_execute_in():
    assert 'execute in' == str(commands.execute.in_)


def test_execute_in_overworld():
    assert 'execute in overworld' == str(commands.execute.in_.overworld)


def test_execute_in_the_end():
    assert 'execute in the_end' == str(commands.execute.in_.the_end)


def test_execute_in_the_nether():
    assert 'execute in the_nether' == str(commands.execute.in_.the_nether)
