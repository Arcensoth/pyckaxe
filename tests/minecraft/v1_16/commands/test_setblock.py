from pyckaxe.minecraft import blocks, commands


def test_setblock():
    c1 = commands.setblock
    assert str(c1) == "setblock"


def test_setblock_dot_position():
    c1 = commands.setblock.position([1, 2, 3])
    assert str(c1) == "setblock ~1 ~2 ~3"


def test_setblock_dot_position_dot_block():
    c1 = commands.setblock.position([1, 2, 3]).block(blocks.air)
    assert str(c1) == "setblock ~1 ~2 ~3 minecraft:air"


def test_setblock_dot_position_dot_block_dot_destroy():
    c1 = commands.setblock.position([1, 2, 3]).block(blocks.air).destroy
    assert str(c1) == "setblock ~1 ~2 ~3 minecraft:air destroy"


def test_setblock_dot_position_dot_block_dot_keep():
    c1 = commands.setblock.position([1, 2, 3]).block(blocks.air).keep
    assert str(c1) == "setblock ~1 ~2 ~3 minecraft:air keep"


def test_setblock_dot_position_dot_block_dot_replace():
    c1 = commands.setblock.position([1, 2, 3]).block(blocks.air).replace
    assert str(c1) == "setblock ~1 ~2 ~3 minecraft:air replace"


def test_setblock_call_position_block():
    c1 = commands.setblock([1, 2, 3], blocks.air)
    assert str(c1) == "setblock ~1 ~2 ~3 minecraft:air"


def test_setblock_call_position_block_dot_destroy():
    c1 = commands.setblock([1, 2, 3], blocks.air).destroy
    assert str(c1) == "setblock ~1 ~2 ~3 minecraft:air destroy"


def test_setblock_call_position_block_dot_keep():
    c1 = commands.setblock([1, 2, 3], blocks.air).keep
    assert str(c1) == "setblock ~1 ~2 ~3 minecraft:air keep"


def test_setblock_call_position_block_dot_replace():
    c1 = commands.setblock([1, 2, 3], blocks.air).replace
    assert str(c1) == "setblock ~1 ~2 ~3 minecraft:air replace"
