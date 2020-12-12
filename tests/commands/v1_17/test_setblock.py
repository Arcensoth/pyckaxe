from pyckaxe import blocks, positions
from pyckaxe import commands


def test_setblock():
    assert "setblock" == str(commands.setblock)


def test_setblock_position():
    assert "setblock ~ ~ ~" == str(commands.setblock.position(positions.relative))


def test_setblock_position_block():
    assert "setblock ~ ~ ~ minecraft:dirt" == str(
        commands.setblock.position(positions.relative).block(blocks.dirt)
    )


def test_setblock_call():
    assert "setblock ~ ~ ~ minecraft:dirt" == str(
        commands.setblock(positions.relative, blocks.dirt)
    )


def test_setblock_position_block_destroy():
    assert "setblock ~ ~ ~ minecraft:dirt destroy" == str(
        commands.setblock.position(positions.relative).block(blocks.dirt).destroy
    )


def test_setblock_position_block_keep():
    assert "setblock ~ ~ ~ minecraft:dirt keep" == str(
        commands.setblock.position(positions.relative).block(blocks.dirt).keep
    )


def test_setblock_position_block_replace():
    assert "setblock ~ ~ ~ minecraft:dirt replace" == str(
        commands.setblock.position(positions.relative).block(blocks.dirt).replace
    )


def test_setblock_call_destroy():
    assert "setblock ~ ~ ~ minecraft:dirt destroy" == str(
        commands.setblock(positions.relative, blocks.dirt).destroy
    )


def test_setblock_call_keep():
    assert "setblock ~ ~ ~ minecraft:dirt keep" == str(
        commands.setblock(positions.relative, blocks.dirt).keep
    )


def test_setblock_call_replace():
    assert "setblock ~ ~ ~ minecraft:dirt replace" == str(
        commands.setblock(positions.relative, blocks.dirt).replace
    )
