from pyckaxe import blocks, commands


def test_setblock():
    assert "setblock" == str(commands.setblock)


def test_setblock_position():
    assert "setblock ~ ~ ~" == str(commands.setblock.position([0, 0, 0]))


def test_setblock_position_block():
    assert "setblock ~ ~ ~ minecraft:dirt" == str(
        commands.setblock.position([0, 0, 0]).block(blocks.dirt)
    )


def test_setblock_call():
    assert "setblock ~ ~ ~ minecraft:dirt" == str(commands.setblock([0, 0, 0], blocks.dirt))


def test_setblock_position_block_destroy():
    assert "setblock ~ ~ ~ minecraft:dirt destroy" == str(
        commands.setblock.position([0, 0, 0]).block(blocks.dirt).destroy
    )


def test_setblock_position_block_keep():
    assert "setblock ~ ~ ~ minecraft:dirt keep" == str(
        commands.setblock.position([0, 0, 0]).block(blocks.dirt).keep
    )


def test_setblock_position_block_replace():
    assert "setblock ~ ~ ~ minecraft:dirt replace" == str(
        commands.setblock.position([0, 0, 0]).block(blocks.dirt).replace
    )


def test_setblock_call_destroy():
    assert "setblock ~ ~ ~ minecraft:dirt destroy" == str(
        commands.setblock([0, 0, 0], blocks.dirt).destroy
    )


def test_setblock_call_keep():
    assert "setblock ~ ~ ~ minecraft:dirt keep" == str(
        commands.setblock([0, 0, 0], blocks.dirt).keep
    )


def test_setblock_call_replace():
    assert "setblock ~ ~ ~ minecraft:dirt replace" == str(
        commands.setblock([0, 0, 0], blocks.dirt).replace
    )
