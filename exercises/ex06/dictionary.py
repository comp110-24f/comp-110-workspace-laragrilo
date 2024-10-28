"""Ex06"""

__author__ = "730602202"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    invert_dict: dict[str, str] = {}
    for key in dict1:
        value = dict1[key]
        if value in invert_dict:
            raise KeyError("There are duplicate keys in inverted dictionary.")
        invert_dict[value] = key

    return invert_dict


def favorite_colors(dict2: dict[str, str]) -> str:
    color_count: dict[str, int] = {}
    for name in dict2:
        color = dict2[name]
        if color not in color_count:
            color_count[color] = 0
        color_count[color] += 1

    highest_count = 0
    frequent_color = ""
    for color in color_count:
        if color_count[color] > highest_count:
            highest_count = color_count[color]
            frequent_color = color
    return frequent_color


def count(list1: list[str]) -> dict[str, int]:
    result_dict: dict[str, int] = {}
    for input in list1:
        if input in result_dict:
            result_dict[input] += 1
        else:
            result_dict[input] = 1
    return result_dict


def alphabetizer(list2: list[str]) -> dict[str, list[str]]:
    alpha_dict: dict[str, list[str]] = {}

    for word in list2:
        lower_case_word = word.lower()
        first_letter = lower_case_word[0]

        if first_letter in alpha_dict:
            alpha_dict[first_letter].append(word)
        else:
            alpha_dict[first_letter] = [word]
    return alpha_dict


def update_attendance(
    dict4: dict[str, list[str]], day_of_week: str, student_present: str
) -> None:
    if day_of_week in dict4:
        dict4[day_of_week].append(student_present)
    else:
        dict4[day_of_week] = [student_present]
    return None
