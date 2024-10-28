"""Building list utility functions"""

__author__ = "730602202"


def only_evens(list1: list[int]) -> list[int]:
    """Function returns only even numbers in a list"""
    even_list = []
    # i struggled here for a bit, thinking about whether i should use
    # a while loop or for loop because i'm not confident in using for loops yet but
    # decided to give them a try
    # because they're shorter and visually less complex as some while loops

    for number in list1:
        if number % 2 == 0:
            even_list.append(number)
            # i completely forgot about the append operator and was trying to do this
            # using += operators but nothing seemed to quite work
            # went over las couple class slides and remembered about append and it made
            # this process smoother and easier
    return even_list


def sub(list2: list[int], start_index: int, end_index: int) -> list[int]:
    """Function generates list, subset of the input list, between the start index and end index - 1"""
    sub_list = []

    if len(list2) == 0:
        return sub_list

    if start_index < 0:
        start_index = 0

    if end_index > len(list2):
        # spent a bit of time figuring out whether it should be `>=` or just `>`
        end_index = len(list2)

    for number in range(len(list2)):
        if number >= start_index:
            if number < end_index:
                sub_list.append(list2[number])
        number = +1
    return sub_list


def add_at_index(list3: list[int], added_int: int, add_idx: int) -> None:
    """Function modifies the input list to place the element at the given index"""
    # I struggled with the idea of inserting at an index since i initially tried
    # `list3[add_idx] = added_int`. Realized I need to shift
    # everything to the right first
    list3.append(0)

    if add_idx < 0 or add_idx > len(list3):
        raise IndexError("Index is out of bounds for the input list")

    for number in range(len(list3) - 1, add_idx, -1):
        list3[number] = list3[number - 1]
        # took me a few tries to realize this loop needs to go backward
        # starting from the end of the list

    list3[add_idx] = added_int
