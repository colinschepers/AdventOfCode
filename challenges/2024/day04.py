from collections.abc import Sequence

from utils import get_input


def rotate_90(grid: Sequence[str]) -> Sequence[str]:
    return ["".join(reversed(x)) for x in zip(*grid)]


def diagonals(grid: Sequence[str]) -> Sequence[str]:
    return [
        "".join(
            grid[row][row + diff] for row in
            range(max(0, -diff), min(len(grid), len(grid) - diff))
        )
        for diff in range(-len(grid) + 1, len(grid))
    ]


def count_xmas(grid: Sequence[str]) -> int:
    return (
        sum(row.count("XMAS") + row.count("SAMX") for row in grid) +
        sum(row.count("XMAS") + row.count("SAMX") for row in rotate_90(grid)) +
        sum(row.count("XMAS") + row.count("SAMX") for row in diagonals(grid)) +
        sum(row.count("XMAS") + row.count("SAMX") for row in diagonals(rotate_90(grid)))
    )


def count_x_mas(grid: Sequence[str]) -> int:
    return sum(
        grid[r][c] == "A" and
        {grid[r - 1][c - 1], grid[r + 1][c + 1]} == {"M", "S"} and
        {grid[r - 1][c + 1], grid[r + 1][c - 1]} == {"M", "S"}
        for r in range(1, len(grid) - 1)
        for c in range(1, len(grid[r]) - 1)
    )


input = get_input(2024, 4)
print(count_xmas(input))
print(count_x_mas(input))
