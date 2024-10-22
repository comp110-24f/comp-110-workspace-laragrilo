"""Unit tests that test find_and_remove_max function"""

__author__ = "730602202"

from CQs.cq07.find_max import find_and_remove_max


def test_returns_correct_max_value() -> None:
    """testing that function returns the largest number"""
    list1 = [3, 1, 4, 1, 5, 9]
    assert find_and_remove_max(list1) == 9


def test_mutates_input_list() -> None:
    """test that function removes all instances of max"""
    list2 = [3, 1, 4, 4, 5, 4]
    find_and_remove_max(list2)
    assert list2 == [3, 1, 4, 4, 4]


def test_all_elements_same() -> None:
    """test that the function removes all instances when all elements are the same"""
    list3 = [5, 5, 5, 5]
    assert find_and_remove_max(list3) == 5
    assert list3 == []
