from utils import get_input, Grid


def _slide_north(grid: Grid) -> Grid:
    new_grid = [[char for char in row] for row in grid]
    for c in range(len(new_grid[0])):
        free_row_idx = 0
        for r in range(len(new_grid)):
            if new_grid[r][c] == ".":
                free_row_idx = min(free_row_idx, r)
            elif new_grid[r][c] == "#":
                free_row_idx = r + 1
            elif new_grid[r][c] == "O":
                new_grid[r][c] = "."
                new_grid[free_row_idx][c] = "O"
                free_row_idx += 1
    return new_grid


def _get_total_load(grid: Grid) -> int:
    return sum(len(grid) - r for r, row in enumerate(grid) for char in row if char == "O")


def _get_total_load_cycles(grid: Grid, num_cycles: int) -> int:
    cache = {}
    total_loads = [_get_total_load(grid)]

    for cycle_nr in range(num_cycles):
        for rotation in range(4):
            grid = _slide_north(grid)
            grid = tuple(tuple(reversed(x)) for x in zip(*grid))

        if grid in cache:
            cycle_start = cache[grid]
            cycle_idx = (num_cycles - cycle_start) % (cycle_nr - cycle_start)
            return total_loads[cycle_start + cycle_idx]

        cache[grid] = cycle_nr
        total_loads.append(_get_total_load(grid))

    return total_loads[-1]


grid = [list(line) for line in get_input(year=2023, day=14)]
print(_get_total_load(_slide_north(grid)))
print(_get_total_load_cycles(grid, num_cycles=1000000000))
