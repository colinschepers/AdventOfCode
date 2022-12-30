from typing import Iterable

from utils import get_input


def up(r: int, c: int) -> Iterable[int]:
    yield from (forest[_r][c] for _r in range(r - 1, -1, -1))


def down(r: int, c: int) -> Iterable[int]:
    yield from (forest[_r][c] for _r in range(r + 1, len(forest)))


def left(r: int, c: int) -> Iterable[int]:
    yield from (forest[r][_c] for _c in range(c - 1, -1, -1))


def right(r: int, c: int) -> Iterable[int]:
    yield from (forest[r][_c] for _c in range(c + 1, len(forest[r])))


def is_visible(r: int, c: int) -> int:
    return r == 0 or r == len(forest) - 1 or c == 0 or c == len(forest[r]) - 1 or \
           all(t < forest[r][c] for t in left(r, c)) or all(t < forest[r][c] for t in right(r, c)) or \
           all(t < forest[r][c] for t in up(r, c)) or all(t < forest[r][c] for t in down(r, c))


def count_seen(tree_size: int, trees: Iterable[int]) -> int:
    cnt = 0
    for tree in trees:
        cnt += 1
        if tree >= tree_size:
            break
    return cnt


def scenic_score(r: int, c: int) -> int:
    return count_seen(forest[r][c], left(r, c)) * count_seen(forest[r][c], right(r, c)) * \
           count_seen(forest[r][c], up(r, c)) * count_seen(forest[r][c], down(r, c))


forest = [[int(c) for c in line] for line in get_input(year=2022, day=8)]
print(sum(is_visible(r, c) for r in range(len(forest)) for c in range(len(forest[r]))))
print(max(scenic_score(r, c) for r in range(len(forest)) for c in range(len(forest[r]))))
