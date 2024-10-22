def get_name(n: str) -> str:
    return n


def get_first(input: list[int]) -> int:
    """return first index of list [0]"""
    if len(input) == 0:
        raise IndexError
    return input[0]


def test_name_func() -> None:
    # other code can go here
    assert get_name(n="Lara") == "Lara"


def tes_get_first() -> None:
    assert get_first(input=[1, 2, 3]) == 1


print(get_first([]))
# can't get egg from empty egg carto --> edge case of empty list not accounted for
