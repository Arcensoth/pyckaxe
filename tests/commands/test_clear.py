from pyckaxe import commands, items, selectors


def test_clear():
    assert 'clear' == str(commands.clear)


def test_clear_targets():
    assert 'clear @a' == str(commands.clear.targets(selectors.all_players))


def test_clear_targets_item():
    assert 'clear @a minecraft:diamond' == str(commands.clear.targets(selectors.all_players).item(items.diamond))


def test_clear_targets_item_max_count():
    assert 'clear @a minecraft:diamond 64' == str(
        commands.clear.targets(selectors.all_players).item(items.diamond).max_count(64))


def test_clear_call():
    assert 'clear @a minecraft:diamond 64' == str(commands.clear(selectors.all_players, items.diamond, 64))
