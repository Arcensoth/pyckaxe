from pyckaxe import blocks, positions
from pyckaxe.commands.v1_16 import commands


def test_fill():
    assert "fill" == str(commands.fill)


def test_fill_from():
    assert "fill ~ ~ ~" == str(commands.fill.from_(positions.relative))


def test_fill_from_to():
    assert "fill ~ ~ ~ ~ ~ ~" == str(commands.fill.from_(positions.relative).to(positions.relative))


def test_fill_from_to_block():
    assert "fill ~ ~ ~ ~ ~ ~ minecraft:grass" == str(
        commands.fill.from_(positions.relative).to(positions.relative).block(blocks.grass)
    )


def test_fill_call():
    assert "fill ~ ~ ~ ~ ~ ~ minecraft:grass" == str(
        commands.fill(positions.relative, positions.relative, blocks.grass)
    )


def test_fill_call_destroy():
    assert "fill ~ ~ ~ ~ ~ ~ minecraft:grass destroy" == str(
        commands.fill(positions.relative, positions.relative, blocks.grass).destroy
    )


def test_fill_call_hollow():
    assert "fill ~ ~ ~ ~ ~ ~ minecraft:grass hollow" == str(
        commands.fill(positions.relative, positions.relative, blocks.grass).hollow
    )


def test_fill_call_keep():
    assert "fill ~ ~ ~ ~ ~ ~ minecraft:grass keep" == str(
        commands.fill(positions.relative, positions.relative, blocks.grass).keep
    )


def test_fill_call_outline():
    assert "fill ~ ~ ~ ~ ~ ~ minecraft:grass outline" == str(
        commands.fill(positions.relative, positions.relative, blocks.grass).outline
    )


def test_fill_call_replace():
    assert "fill ~ ~ ~ ~ ~ ~ minecraft:grass replace" == str(
        commands.fill(positions.relative, positions.relative, blocks.grass).replace
    )


def test_fill_call_replace_filter():
    assert "fill ~ ~ ~ ~ ~ ~ minecraft:grass replace minecraft:dirt" == str(
        commands.fill(positions.relative, positions.relative, blocks.grass).replace.filter(
            blocks.dirt
        )
    )


def test_fill_call_replace_call():
    assert "fill ~ ~ ~ ~ ~ ~ minecraft:grass replace minecraft:dirt" == str(
        commands.fill(positions.relative, positions.relative, blocks.grass).replace(blocks.dirt)
    )