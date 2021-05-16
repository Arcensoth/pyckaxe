from pyckaxe import Position

# @@ NEGATIVE (-)


def test_position_neg_with_positive_coords():
    p1 = Position.from_xyz(1, 2, 3)
    assert str(p1) == "1 2 3"
    p2 = -p1
    assert str(p2) == "-1 -2 -3"


def test_position_neg_with_negative_coords():
    p1 = Position.from_xyz(-1, -2, -3)
    assert str(p1) == "-1 -2 -3"
    p2 = -p1
    assert str(p2) == "1 2 3"


def test_position_neg_with_mixed_coords():
    p1 = Position.from_xyz(-1, 2, -3)
    assert str(p1) == "-1 2 -3"
    p2 = -p1
    assert str(p2) == "1 -2 3"


# @@ POSITIVE (+)


def test_position_pos_turns_coord_sign_absolute():
    p1 = ~Position.from_xyz(1, 2, 3)
    assert str(p1) == "~1 ~2 ~3"
    p2 = +p1
    assert str(p2) == "1 2 3"


# @@ ABSOLUTE (abs())


def test_position_abs():
    p1 = Position.from_xyz(-1, 2, -3)
    assert str(p1) == "-1 2 -3"
    p2 = abs(p1)
    assert str(p2) == "1 2 3"


def test_position_abs_does_not_turn_coord_sign_absolute():
    p1 = ~Position.from_xyz(1, 2, 3)
    assert str(p1) == "~1 ~2 ~3"
    p2 = abs(p1)
    assert str(p2) == "~1 ~2 ~3"


# @@ INVERT (~)


def test_position_invert_turns_coord_sign_relative():
    p1 = Position.from_xyz(1, 2, 3)
    assert str(p1) == "1 2 3"
    p2 = ~p1
    assert str(p2) == "~1 ~2 ~3"


# @@ ADDITION (+)


def test_add_two_positions():
    p1 = Position.from_xyz(1, 2, 3)
    p2 = Position.from_xyz(4, 5, 6)
    assert str(p1 + p2) == "5 7 9"


def test_add_tuple_to_position():
    p1 = Position.from_xyz(1, 2, 3)
    p2 = (4, 5, 6)
    assert str(p1 + p2) == "5 7 9"


def test_add_position_to_tuple():
    p1 = (1, 2, 3)
    p2 = Position.from_xyz(4, 5, 6)
    assert str(p1 + p2) == "5 7 9"


def test_add_list_to_position():
    p1 = Position.from_xyz(1, 2, 3)
    p2 = [4, 5, 6]
    assert str(p1 + p2) == "5 7 9"


def test_add_position_to_list():
    p1 = [1, 2, 3]
    p2 = Position.from_xyz(4, 5, 6)
    assert str(p1 + p2) == "~5 ~7 ~9"


def test_add_absolute_position_to_relative_position():
    p1 = ~Position.from_xyz(1, 2, 3)
    p2 = Position.from_xyz(4, 5, 6)
    assert str(p1 + p2) == "~5 ~7 ~9"


def test_add_relative_position_to_absolute_position():
    p1 = Position.from_xyz(1, 2, 3)
    p2 = ~Position.from_xyz(4, 5, 6)
    assert str(p1 + p2) == "5 7 9"


def test_add_relative_position_to_reltive_position():
    p1 = ~Position.from_xyz(1, 2, 3)
    p2 = ~Position.from_xyz(4, 5, 6)
    assert str(p1 + p2) == "~5 ~7 ~9"


# @@ SUBTRACTION (-)


def test_subtract_two_positions():
    p1 = Position.from_xyz(4, 5, 6)
    p2 = Position.from_xyz(3, 2, 1)
    assert str(p1 - p2) == "1 3 5"


def test_subtract_tuple_from_position():
    p1 = Position.from_xyz(4, 5, 6)
    p2 = (3, 2, 1)
    assert str(p1 - p2) == "1 3 5"


def test_subtract_list_from_position():
    p1 = Position.from_xyz(4, 5, 6)
    p2 = [3, 2, 1]
    assert str(p1 - p2) == "1 3 5"


def test_subtract_absolute_position_from_relative_position():
    p1 = ~Position.from_xyz(4, 5, 6)
    p2 = Position.from_xyz(3, 2, 1)
    assert str(p1 - p2) == "~1 ~3 ~5"


def test_subtract_relative_position_from_absolute_position():
    p1 = Position.from_xyz(4, 5, 6)
    p2 = ~Position.from_xyz(3, 2, 1)
    assert str(p1 - p2) == "1 3 5"


def test_subtract_relative_position_from_reltive_position():
    p1 = ~Position.from_xyz(4, 5, 6)
    p2 = ~Position.from_xyz(3, 2, 1)
    assert str(p1 - p2) == "~1 ~3 ~5"


# @@ MULTIPLICATION (*)


def test_multiply_position_by_int():
    p = Position.from_xyz(4, 5, 6)
    assert str(p * 5) == "20 25 30"


def test_multiply_position_by_float():
    p = Position.from_xyz(4, 5, 6)
    assert str(p * 2.5) == "10 12.5 15"


def test_multiply_int_by_position():
    p = Position.from_xyz(4, 5, 6)
    assert str(5 * p) == "20 25 30"


def test_multiply_float_by_position():
    p = Position.from_xyz(4, 5, 6)
    assert str(2.5 * p) == "10 12.5 15"


def test_multiply_position_with_relative_coords():
    p = ~Position.from_xyz(4, 5, 6)
    assert str(p * 5) == "~20 ~25 ~30"


def test_multiply_position_with_local_coords():
    p = Position.from_xyz(4, 5, 6).local()
    assert str(p * 5) == "^20 ^25 ^30"


# @@ TRUE DIVISION (/)


def test_truediv_position_by_int():
    p = Position.from_xyz(4, 5, 6)
    assert str(p / 10) == "0.4 0.5 0.6"


def test_truediv_position_by_big_float():
    p = Position.from_xyz(4, 5, 6)
    assert str(p / 2.5) == "1.6 2 2.4"


def test_truediv_position_by_small_float():
    p = Position.from_xyz(4, 5, 6)
    assert str(p / 0.5) == "8 10 12"


def test_truediv_position_with_relative_coords():
    p = ~Position.from_xyz(4, 5, 6)
    assert str(p / 10) == "~0.4 ~0.5 ~0.6"


def test_truediv_position_with_local_coords():
    p = Position.from_xyz(4, 5, 6).local()
    assert str(p / 10) == "^0.4 ^0.5 ^0.6"


# @@ FLOOR DIVISION (//)


def test_floordiv_position_by_int():
    p = Position.from_xyz(4, 5, 6)
    assert str(p // 10) == "0 0 0"


def test_floordiv_position_by_big_float():
    p = Position.from_xyz(4, 5, 6)
    assert str(p // 2.5) == "1 2 2"


def test_floordiv_position_by_small_float():
    p = Position.from_xyz(4, 5, 6)
    assert str(p // 0.5) == "8 10 12"


def test_floordiv_position_with_relative_coords():
    p = ~Position.from_xyz(4, 5, 6)
    assert str(p // 10) == "~ ~ ~"


def test_floordiv_position_with_local_coords():
    p = Position.from_xyz(4, 5, 6).local()
    assert str(p // 10) == "^ ^ ^"


# @@ MODULO (%)


def test_modulo_position_by_int():
    p = Position.from_xyz(4, 5, 6)
    assert str(p % 3) == "1 2 0"


def test_modulo_position_by_big_float():
    p = Position.from_xyz(4, 5, 6)
    assert str(p % 1.5) == "1 0.5 0"


def test_modulo_position_by_small_float():
    p = Position.from_xyz(4, 5, 6)
    assert str(p % 0.9) == "0.4 0.5 0.6"


def test_modulo_position_with_relative_coords():
    p = ~Position.from_xyz(4, 5, 6)
    assert str(p % 3) == "~1 ~2 ~"


def test_modulo_position_with_local_coords():
    p = Position.from_xyz(4, 5, 6).local()
    assert str(p % 3) == "^1 ^2 ^"


# @@ EXPONENTIATION (**)


def test_pow_position_by_int():
    p = Position.from_xyz(4, 9, 16)
    assert str(p ** 2) == "16 81 256"


def test_pow_position_by_big_float():
    p = Position.from_xyz(4, 9, 16)
    assert str(p ** 1.5) == "8 27 64"


def test_pow_position_by_small_float():
    p = Position.from_xyz(4, 9, 16)
    assert str(p ** 0.5) == "2 3 4"


def test_pow_position_with_relative_coords():
    p = ~Position.from_xyz(4, 9, 16)
    assert str(p ** 2) == "~16 ~81 ~256"


def test_pow_position_with_local_coords():
    p = Position.from_xyz(4, 9, 16).local()
    assert str(p ** 2) == "^16 ^81 ^256"
