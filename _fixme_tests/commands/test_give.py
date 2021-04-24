from pyckaxe import items, selectors
from pyckaxe import commands


def test_give():
    assert "give" == str(commands.give)


def test_give_targets():
    assert "give @a" == str(commands.give.targets(selectors.all_players))


def test_give_targets_item():
    assert "give @a minecraft:diamond" == str(
        commands.give.targets(selectors.all_players).item(items.diamond)
    )


def test_give_targets_item_count():
    assert "give @a minecraft:diamond 64" == str(
        commands.give.targets(selectors.all_players).item(items.diamond).count(64)
    )


def test_give_call():
    assert "give @a minecraft:diamond 64" == str(
        commands.give(selectors.all_players, items.diamond, 64)
    )
