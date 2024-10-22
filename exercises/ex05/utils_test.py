"""defining unit tests for utils.py"""

__author__ = "730602202"

import pytest
from exercises.ex05.utils import only_evens, sub, add_at_index

"""Testing only_evens"""


def test_only_evens_empty_list() -> None:
    assert only_evens([]) == []


def test_only_evens_odd_numbers() -> None:
    assert only_evens([1, 3, 5, 7, 9]) == []


def test_only_evens_mixed() -> None:
    assert only_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


"""Testing sub"""


def test_sub_empty_list() -> None:
    assert sub([10, 20, 30], -2, 2) == [10, 20]


def test_sub_end_index_beyond_length():
    assert sub([1, 2, 3], 1, 10) == [2, 3]


"""Testing add_at_index"""


def test_add_at_index_regular_case():
    list = [1, 2, 4]
    add_at_index(list, 3, 2)
    assert list == [1, 2, 3, 4]


def test_add_at_index_raises_indexerror():
    list = [1, 2, 3]
    with pytest.raises(IndexError):
        add_at_index(list, 10, 10)


def test_add_at_index_edge_case_start():
    list = [2, 3, 4]
    add_at_index(list, 1, 0)
    assert list == [1, 2, 3, 4]
