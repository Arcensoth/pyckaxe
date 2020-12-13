from pyckaxe import Position, blocks, commands


def test_execute_if_block():
    assert "execute if block" == str(commands.execute.if_.block)


def test_execute_if_block_position():
    assert "execute if block ~ ~ ~" == str(commands.execute.if_.block.position(~Position.zero()))


def test_execute_if_block_position_block():
    assert "execute if block ~ ~ ~ minecraft:grass" == str(
        commands.execute.if_.block.position(~Position.zero()).block(blocks.grass)
    )


def test_execute_if_block_call():
    assert "execute if block ~ ~ ~ minecraft:grass" == str(
        commands.execute.if_.block(~Position.zero(), blocks.grass)
    )


def test_execute_unless_block():
    assert "execute unless block" == str(commands.execute.unless.block)


def test_execute_unless_block_position():
    assert "execute unless block ~ ~ ~" == str(
        commands.execute.unless.block.position(~Position.zero())
    )


def test_execute_unless_block_position_block():
    assert "execute unless block ~ ~ ~ minecraft:grass" == str(
        commands.execute.unless.block.position(~Position.zero()).block(blocks.grass)
    )


def test_execute_unless_block_call():
    assert "execute unless block ~ ~ ~ minecraft:grass" == str(
        commands.execute.unless.block(~Position.zero(), blocks.grass)
    )
