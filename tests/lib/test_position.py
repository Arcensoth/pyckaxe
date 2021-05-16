from pyckaxe import Position


def test_position_from_xyz():
    assert str(Position.from_xyz(1, 2, 3)) == "1 2 3"


def test_position_from_tuple():
    assert str(Position.from_tuple((1, 2, 3))) == "1 2 3"


def test_position_from_list():
    assert str(Position.from_list([1, 2, 3])) == "~1 ~2 ~3"
