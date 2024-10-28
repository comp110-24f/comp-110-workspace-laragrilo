"""Defining unit tests for utils.py"""

__author__ = "730602202"

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index

# thinking of uses cases was harder than I thought, I had to play aorund with the
# funcitons to think of tests

"""Testing only_evens"""


def test_only_evens_empty_list() -> None:
    """testing empty list"""
    assert only_evens([]) == []


def test_only_evens_odd_numbers() -> None:
    """testing if all odd numbers"""
    assert only_evens([1, 3, 5, 7, 9]) == []


def test_only_evens_mixed() -> None:
    """testing if numbers a re mixed between even and odd"""
    assert only_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


"""Testing sub"""


def test_sub_empty_list() -> None:
    """testing empty list"""
    assert sub([10, 20, 30], -2, 2) == [10, 20]


def test_sub_end_index_greater__than_length():
    """testing when index is greater than the length of the list"""
    assert sub([1, 2, 3], 1, 10) == [2, 3]


def test_sub_negative_start_index():
    """testing if index is negative"""
    assert sub([10, 20, 30], -2, 2) == [10, 20]


"""Testing add_at_index"""


def test_add_at_index_regular_case():
    """testing inserting a value at an index in the list"""
    list = [1, 2, 4]
    add_at_index(list, 3, 2)
    assert list == [1, 2, 3, 4]


def test_add_at_index_raises_indexerror():
    """testing that an IndexError is raised when the index is out of bounds"""
    list = [1, 2, 3]
    with pytest.raises(IndexError):
        add_at_index(list, 10, 10)


def test_add_at_index_edge_case_start():
    """testing inserting a value at the beginning of the list (index 0)"""
    list = [2, 3, 4]
    add_at_index(list, 1, 0)
    assert list == [1, 2, 3, 4]
