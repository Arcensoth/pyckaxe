from pyckaxe import blocks, positions
from pyckaxe.commands.v1_16 import commands


def test_execute_if_block():
    assert "execute if block" == str(commands.execute.if_.block)


def test_execute_if_block_position():
    assert "execute if block ~ ~ ~" == str(commands.execute.if_.block.position(positions.relative))


def test_execute_if_block_position_block():
    assert "execute if block ~ ~ ~ minecraft:grass" == str(
        commands.execute.if_.block.position(positions.relative).block(blocks.grass)
    )


def test_execute_if_block_call():
    assert "execute if block ~ ~ ~ minecraft:grass" == str(
        commands.execute.if_.block(positions.relative, blocks.grass)
    )


def test_execute_unless_block():
    assert "execute unless block" == str(commands.execute.unless.block)


def test_execute_unless_block_position():
    assert "execute unless block ~ ~ ~" == str(
        commands.execute.unless.block.position(positions.relative)
    )


def test_execute_unless_block_position_block():
    assert "execute unless block ~ ~ ~ minecraft:grass" == str(
        commands.execute.unless.block.position(positions.relative).block(blocks.grass)
    )


def test_execute_unless_block_call():
    assert "execute unless block ~ ~ ~ minecraft:grass" == str(
        commands.execute.unless.block(positions.relative, blocks.grass)
    )
