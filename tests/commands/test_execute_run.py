from pyckaxe import blocks, commands, positions, selectors


def test_execute_run():
    assert 'execute run' == str(commands.execute.run)


def test_execute_run_something_with_no_args():
    assert 'execute run execute' == str(commands.execute.run.execute)


def test_execute_run_something_with_one_arg():
    assert 'execute run say hi' == str(commands.execute.run.say('hi'))


def test_execute_run_something_with_several_args():
    assert 'execute run setblock ~ ~ ~ minecraft:dirt' == str(
        commands.execute.run.setblock(positions.relative, blocks.dirt))


def test_execute_run_something_with_optional_args():
    assert 'execute run clear @a' == str(commands.execute.run.clear.targets(selectors.all_players))


def test_execute_run_something_nested():
    assert 'execute run time query gametime' == str(commands.execute.run.time.query.gametime)
