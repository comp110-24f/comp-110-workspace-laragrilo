"""Testing While Loops"""

__author__ = "730602202"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    track: int = 0
    while track < len(phrase):
        if phrase[track] == search_char:
            count += 1
        track += 1

    return count
