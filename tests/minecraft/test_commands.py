from pyckaxe.minecraft import commands


def test_root_returns_different_instances():
    c1 = commands.setblock
    c2 = commands.setblock
    assert id(c1) != id(c2)
