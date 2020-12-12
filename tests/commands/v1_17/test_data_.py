from pyckaxe import positions, selectors
from pyckaxe import commands


def test_data():
    assert "data" == str(commands.data)


# data get


def test_data_get():
    assert "data get" == str(commands.data.get)


def test_data_get_block():
    assert "data get block" == str(commands.data.get.block)


def test_data_get_block_position():
    assert "data get block ~ ~ ~" == str(commands.data.get.block.position(positions.relative))


def test_data_get_block_position_path():
    assert "data get block ~ ~ ~ Item.Count" == str(
        commands.data.get.block.position(positions.relative).path("Item.Count")
    )


def test_data_get_block_position_path_scale():
    assert "data get block ~ ~ ~ Item.Count 0.5" == str(
        commands.data.get.block.position(positions.relative).path("Item.Count").scale(0.5)
    )


def test_data_get_block_call():
    assert "data get block ~ ~ ~ Item.Count 0.5" == str(
        commands.data.get.block(positions.relative, "Item.Count", 0.5)
    )


def test_data_get_entity():
    assert "data get entity" == str(commands.data.get.entity)


def test_data_get_entity_target():
    assert "data get entity @r" == str(commands.data.get.entity.target(selectors.random))


def test_data_get_entity_target_path():
    assert "data get entity @r UUIDLeast" == str(
        commands.data.get.entity.target(selectors.random).path("UUIDLeast")
    )


def test_data_get_entity_target_path_scale():
    assert "data get entity @r UUIDLeast 0.001" == str(
        commands.data.get.entity.target(selectors.random).path("UUIDLeast").scale(0.001)
    )


def test_data_get_entity_call():
    assert "data get entity @r UUIDLeast 0.001" == str(
        commands.data.get.entity(selectors.random, "UUIDLeast", 0.001)
    )


# data merge


def test_data_merge():
    assert "data merge" == str(commands.data.merge)


def test_data_merge_block():
    assert "data merge block" == str(commands.data.merge.block)


def test_data_merge_block_position():
    assert "data merge block ~ ~ ~" == str(commands.data.merge.block.position(positions.relative))


def test_data_merge_block_position_nbt():
    assert "data merge block ~ ~ ~ {auto:1b}" == str(
        commands.data.merge.block.position(positions.relative).nbt("{auto:1b}")
    )


def test_data_merge_block_call():
    assert "data merge block ~ ~ ~ {auto:1b}" == str(
        commands.data.merge.block(positions.relative, "{auto:1b}")
    )


def test_data_merge_entity():
    assert "data merge entity" == str(commands.data.merge.entity)


def test_data_merge_entity_target():
    assert "data merge entity @r" == str(commands.data.merge.entity.target(selectors.random))


def test_data_merge_entity_target_nbt():
    assert "data merge entity @r {Motion:[0.0f,0.5f,0.0f]}" == str(
        commands.data.merge.entity.target(selectors.random).nbt("{Motion:[0.0f,0.5f,0.0f]}")
    )


def test_data_merge_entity_call():
    assert "data merge entity @r {Motion:[0.0f,0.5f,0.0f]}" == str(
        commands.data.merge.entity(selectors.random, "{Motion:[0.0f,0.5f,0.0f]}")
    )


# data remove


def test_data_remove():
    assert "data remove" == str(commands.data.remove)


def test_data_remove_block():
    assert "data remove block" == str(commands.data.remove.block)


def test_data_remove_block_position():
    assert "data remove block ~ ~ ~" == str(commands.data.remove.block.position(positions.relative))


def test_data_remove_block_position_path():
    assert "data remove block ~ ~ ~ Item" == str(
        commands.data.remove.block.position(positions.relative).path("Item")
    )


def test_data_remove_block_call():
    assert "data remove block ~ ~ ~ Item" == str(
        commands.data.remove.block(positions.relative, "Item")
    )


def test_data_remove_entity():
    assert "data remove entity" == str(commands.data.remove.entity)


def test_data_remove_entity_target():
    assert "data remove entity @r" == str(commands.data.remove.entity.target(selectors.random))


def test_data_remove_entity_target_path():
    assert "data remove entity @r Items" == str(
        commands.data.remove.entity.target(selectors.random).path("Items")
    )


def test_data_remove_entity_call():
    assert "data remove entity @r Items" == str(
        commands.data.remove.entity(selectors.random, "Items")
    )
