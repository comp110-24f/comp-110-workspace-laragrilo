"""Find and remove the ma number in a list"""

__author__ = "730602202"


def find_and_remove_max(list1: list[int]) -> int:
    """returns highest value integer in list"""
    if len(list1) == 0:
        return -1
    # I'll start by assuming the first element is the largest and iterating through list
    max_idx = list1[0]
    idx = 0
    while idx < len(list1):
        if list1[idx] > max_idx:
            max_idx = list1[idx]
        idx += 1
    # removing instances of max with pop
    idx = 0
    while idx < len(list1):
        if list1[idx] == max_idx:
            list1.pop(idx)
        else:
            idx += 1
    return max_idx
