import textwrap

from pyckaxe import Position
from pyckaxe.lib.block import Block
from pyckaxe.lib.block_map import BlockMap


def test_block_map_using_tuple_for_size():
    bm = BlockMap(size=(3, 3, 3))
    assert bm.size == Position.from_xyz(3, 3, 3)


def test_block_map_set_block_with_position():
    bm = BlockMap(size=(3, 3, 3))
    bm[1, 1, 1] = Block("stone")
    assert bm[1, 1, 1] == Block("stone")


def test_block_map_printing_with_one_block_on_bottom_floor():
    bm = BlockMap(size=(3, 3, 3))
    bm[1, 0, 1] = Block("stone")
    s1 = str(bm)
    s2 = textwrap.dedent(
        """
                ...
                ...
                ...

                ...
                ...
                ...

                ...
                .0.
                ...
        """
    ).strip()
    assert s1 == s2


def test_block_map_printing_with_one_block_on_top_floor():
    bm = BlockMap(size=(3, 3, 3))
    bm[1, 2, 1] = Block("stone")
    s1 = str(bm)
    s2 = textwrap.dedent(
        """
                ...
                .0.
                ...

                ...
                ...
                ...

                ...
                ...
                ...
        """
    ).strip()
    assert s1 == s2


def test_block_map_printing_with_many_of_one_type_of_block():
    bm = BlockMap(size=(3, 3, 3))
    bm[1, 0, 1] = Block("stone")
    bm[1, 1, 1] = Block("stone")
    bm[1, 2, 1] = Block("stone")
    s1 = str(bm)
    s2 = textwrap.dedent(
        """
                ...
                .0.
                ...

                ...
                .0.
                ...

                ...
                .0.
                ...
        """
    ).strip()
    assert s1 == s2


def test_block_map_printing_with_different_blocks_in_a_row():
    bm = BlockMap(size=(3, 3, 3))
    bm[1, 1, 0] = Block("stone")
    bm[1, 1, 1] = Block("dirt")
    bm[1, 1, 2] = Block("grass")
    s1 = str(bm)
    s2 = textwrap.dedent(
        """
                ...
                ...
                ...

                ...
                012
                ...

                ...
                ...
                ...
        """
    ).strip()
    assert s1 == s2


def test_block_map_printing_with_different_blocks_in_a_column():
    bm = BlockMap(size=(3, 3, 3))
    bm[0, 1, 1] = Block("stone")
    bm[1, 1, 1] = Block("dirt")
    bm[2, 1, 1] = Block("grass")
    s1 = str(bm)
    s2 = textwrap.dedent(
        """
                ...
                ...
                ...

                .0.
                .1.
                .2.

                ...
                ...
                ...
        """
    ).strip()
    assert s1 == s2


def test_block_map_printing_with_different_blocks_in_a_floor():
    bm = BlockMap(size=(3, 3, 3))
    bm[1, 0, 1] = Block("stone")
    bm[1, 1, 1] = Block("dirt")
    bm[1, 2, 1] = Block("grass")
    s1 = str(bm)
    s2 = textwrap.dedent(
        """
                ...
                .2.
                ...

                ...
                .1.
                ...

                ...
                .0.
                ...
        """
    ).strip()
    assert s1 == s2
