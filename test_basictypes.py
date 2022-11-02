#!/usr/bin/python

from typing import Any, List, Tuple

# str
def string_comp(s1: str, s2: str) -> bool:
    return s1 == s2


# int, float, complex
def add_integers(a: int, b: int) -> int:
    return a + b


def add_floats(a: float, b: float) -> float:
    return round(a + b, 2)


def add_complex(a: complex, b: complex) -> complex:
    return a + b


# list, tuple, range
def check_list_member(elem: Any, list_: List) -> bool:
    return elem in list_


def check_tuple_member(elem: Any, tuple_: Tuple) -> bool:
    return elem in tuple_


def check_range_member(elem: int, range_: range) -> bool:
    return elem in range_


# dict
def check_dict_key(dict_: dict, key_: Any) -> bool:
    return key_ in dict_.keys()


# set
def check_set_member(set_: set, elem: Any) -> bool:
    return elem in set_


# bool
def check_bool(b1: bool, b2: bool) -> bool:
    return b1 == b2


# NoneType
def check_none(elem: Any) -> bool:
    return elem == None


# pytest test functions
def test_str_t():
    assert string_comp("Hello", "Hello") == True


def test_str_f():
    assert string_comp("Hello", "Goodbye") == True


def test_int_t():
    assert add_integers(2, 2) == 4


def test_int_f():
    assert add_integers(2, 2) == 5


def test_float_t():
    assert add_floats(1.0, 3.14) == 4.14


def test_float_f():
    assert add_floats(1.0, 2.0) == 5.0


def test_complex_t():
    assert add_complex(3 + 6j, 1 + 1j) == 4 + 7j


def test_complex_f():
    assert add_complex(3 + 6j, 1 + 1j) == 1 - 2j


def test_list_t():
    temp_list = ["a", "b", "c", "d", "e", "f", "g"]
    assert check_list_member("a", temp_list) == True


def test_list_f():
    temp_list = ["a", "b", "c", "d", "e", "f", "g"]
    assert check_list_member("z", temp_list) == True


def test_tuple_t():
    temp_tuple = (1, 2, 3, 4, 5)
    assert check_tuple_member(1, temp_tuple) == True


def test_tuple_f():
    temp_tuple = (1, 2, 3, 4, 5)
    assert check_tuple_member(7, temp_tuple) == True


def test_range_t():
    temp_range = range(10)
    assert check_range_member(1, temp_range) == True


def test_range_f():
    temp_range = range(10)
    assert check_range_member(11, temp_range) == True


def test_dict_t():
    temp_dict = {"name": "Lancelot", "color": "blue", "quest": "holy grail"}
    assert check_dict_key(temp_dict, "quest") == True


def test_dict_f():
    temp_dict = {"name": "Lancelot", "color": "blue"}
    assert check_dict_key(temp_dict, "quest") == True


def test_set_t():
    temp_set = {1, 2, 3, 7}
    assert check_set_member(temp_set, 2) == True


def test_set_f():
    temp_set = {1, 2, 3, 7}
    assert check_set_member(temp_set, 9) == True


def test_bool_t():
    assert check_bool(True, True) == True


def test_bool_f():
    assert check_bool(True, False) == True


def test_none_t():
    a = None
    assert check_none(a) == True


def test_none_f():
    a = 3
    assert check_none(a) == True
