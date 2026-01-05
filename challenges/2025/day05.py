from collections.abc import Iterable

from utils import get_input, split_lines


def merge_ranges(ranges: Iterable[tuple[int, int]]) -> list[tuple[int, int]]:
    merged: list[tuple[int, int]] = []
    for left, right in sorted(ranges):
        if not merged or left > merged[-1][1]:
            merged.append((left, right))
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], right))
    return merged


def is_fresh(ingredient: int, id_ranges: list[tuple[int, int]]) -> bool:
    return any(left <= ingredient <= right for left, right in id_ranges)


range_lines, ingredient_lines = split_lines(get_input(2025, 5))
id_ranges = merge_ranges((int(s[0]), int(s[1])) for line in range_lines if (s := line.split("-")))

print(sum(is_fresh(int(ingredient_line), id_ranges) for ingredient_line in ingredient_lines))
print(sum(right - left + 1  for left, right in id_ranges))
