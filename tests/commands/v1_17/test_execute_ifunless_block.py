from pyckaxe import blocks, commands


def test_execute_if_block():
    assert "execute if block" == str(commands.execute.if_.block)


def test_execute_if_block_position():
    assert "execute if block ~ ~ ~" == str(commands.execute.if_.block.position([0, 0, 0]))


def test_execute_if_block_position_block():
    assert "execute if block ~ ~ ~ minecraft:grass" == str(
        commands.execute.if_.block.position([0, 0, 0]).block(blocks.grass)
    )


def test_execute_if_block_call():
    assert "execute if block ~ ~ ~ minecraft:grass" == str(
        commands.execute.if_.block([0, 0, 0], blocks.grass)
    )


def test_execute_unless_block():
    assert "execute unless block" == str(commands.execute.unless.block)


def test_execute_unless_block_position():
    assert "execute unless block ~ ~ ~" == str(commands.execute.unless.block.position([0, 0, 0]))


def test_execute_unless_block_position_block():
    assert "execute unless block ~ ~ ~ minecraft:grass" == str(
        commands.execute.unless.block.position([0, 0, 0]).block(blocks.grass)
    )


def test_execute_unless_block_call():
    assert "execute unless block ~ ~ ~ minecraft:grass" == str(
        commands.execute.unless.block([0, 0, 0], blocks.grass)
    )
