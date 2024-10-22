"""implementign list utility functions"""

__author__ = "730602202"


def only_evens(list1: list[int]) -> list[int]:
    even_list = []

    for number in list1:
        if number % 2 == 0:
            even_list.append(number)
    return even_list


def sub(list2: list[int], start_index: int, end_index: int) -> list[int]:
    sub_list = []

    if len(list2) == 0:
        return sub_list

    if start_index < 0:
        start_index = 0

    if end_index > len(list2):
        end_index = len(list2)

    for number in range(len(list2)):
        if number >= start_index:
            if number < end_index:
                sub_list.append(list2[number])
        number = +1
    return sub_list


def add_at_index(list3: list[int], added_int: int, add_idx: int) -> None:
    list3.append(0)

    if add_idx < 0 or add_idx > len(list3):
        raise IndexError("Index is out of bounds for the input list")

    for number in range(len(list3) - 1, add_idx, -1):
        list3[number] = list3[number - 1]

    list3[add_idx] = added_int
