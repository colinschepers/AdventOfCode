from functools import cache
from itertools import chain
from typing import Tuple

from utils import Coordinate, get_input

NUMERIC_KEYPAD = (("7", "8", "9"), ("4", "5", "6"), ("1", "2", "3"), ("", "0", "A"))
DIRECTIONAL_KEYPAD = (("", "^", "A"), ("<", "v", ">"))


@cache
def get_coordinate(button: str, is_numeric: bool) -> Coordinate:
    keypad = NUMERIC_KEYPAD if is_numeric else DIRECTIONAL_KEYPAD
    return next(iter(
        (r, c) for r, row in enumerate(keypad) for c, char in enumerate(row) if char == button
    ))


@cache
def get_paths(position: Coordinate, target: Coordinate, is_numeric: bool) -> Tuple[str, ...]:
    if position == get_coordinate("", is_numeric):
        return tuple()
    if position == target:
        return tuple("A")
    return tuple(chain(
        ("^" + s for s in get_paths((position[0] - 1, position[1]), target, is_numeric))
        if position[0] - target[0] > 0 else (),
        ("v" + s for s in get_paths((position[0] + 1, position[1]), target, is_numeric))
        if position[0] - target[0] < 0 else (),
        ("<" + s for s in get_paths((position[0], position[1] - 1), target, is_numeric))
        if position[1] - target[1] > 0 else (),
        (">" + s for s in get_paths((position[0], position[1] + 1), target, is_numeric))
        if position[1] - target[1] < 0 else (),
    ))


@cache
def get_button_presses(
    current: str, code: str, master: str = "A", depth: int = 0, is_numeric: bool = True
) -> int:
    if depth == 0:
        return len(code)
    if len(code) == 0:
        return 0
    
    return min(
        get_button_presses(
            current=master, code=path, master="A", depth=depth - 1, is_numeric=False
        )
        + get_button_presses(
            current=code[0], code=code[1:], master=master, depth=depth, is_numeric=is_numeric
        )
        for path in get_paths(
            position=get_coordinate(current, is_numeric),
            target=get_coordinate(code[0], is_numeric),
            is_numeric=is_numeric
        )
    )


codes = get_input(2024, 21)
print(sum(get_button_presses("A", code, depth=3) * int(code[:-1]) for code in codes))
print(sum(get_button_presses("A", code, depth=26) * int(code[:-1]) for code in codes))
