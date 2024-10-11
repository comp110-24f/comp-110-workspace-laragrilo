"""Excercise 4"""

__author__ = "730602202"


def all(list1: list[int], numbers: int) -> bool:
    """Returns True if all integers in list match the target integer"""
    idx = 0
    # check if the list is empty, return False if it is
    if len(list1) == 0:
        return False
    # iterating through the list and compare each element with integer target
    while idx < len(list1):
        if list1[idx] != numbers:
            return False
        idx += 1
    return True


def max(list2: list[int]) -> int:
    """Returns highest value integer in list"""
    if len(list2) == 0:
        raise ValueError("max() arg is an empty List")
    # I'll start by assuming the first element is the largest
    highest_idx = list2[0]
    idx = 0
    while idx < len(list2):
        if list2[idx] > highest_idx:
            highest_idx = list2[idx]
        idx += 1
    return highest_idx


# for this function i used the same intuition we built for the lowest card in the deck excercise in class
# instead of having the lowest index it was simply changing it to the highest input and havign a local variable to store that info


def is_equal(list_int1: list[int], list_int2: list[int]) -> bool:
    """Returns True if both lists are deeply equal"""
    if len(list_int1) != len(list_int2):
        return False
    idx = 0
    while idx < len(list_int1):
        if list_int1[idx] != list_int2[idx]:
            return False
        idx += 1
    return True


def extend(list_int1: list[int], list_int2: list[int]) -> None:
    idx = 0
    # mutating by appending elements of list2 to list1
    while idx < len(list_int2):
        list_int1.append(list_int2[idx])
        idx += 1
