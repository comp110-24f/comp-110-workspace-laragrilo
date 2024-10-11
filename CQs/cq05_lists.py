"""Mutating Functions"""

__author__ = "730602202"


def manual_append(list1: list[int], number: int) -> None:
    """Appending something to a list"""
    list1.append(number)
    return


def double(list2: list[int]) -> None:
    """doubling list items"""
    idx = 0
    while idx < len(list2):
        list2[idx] *= 2
        idx += 1
    return


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
double(list_2)
print(list_1)
print(list_2)
# list_1 will print 2, 4, 6
# list_2 will print 2, 4, 6
