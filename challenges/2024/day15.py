from collections.abc import Iterable

from utils import get_input, Grid, Coordinate, iter_grid, split_lines

DIRS = {"<": (0, -1), "^": (-1, 0), ">": (0, 1), "v": (1, 0)}


def to_str(grid: Grid) -> str:
    return "\n".join("".join(row) for row in grid) + "\n"


def expand_line(line: str) -> str:
    return line.replace("#", "##").replace("O", "[]").replace(".", "..").replace("@", "@.")


def get_next_coordinate(coord: Coordinate, dir: Coordinate) -> Coordinate:
    return coord[0] + dir[0], coord[1] + dir[1]


def get_previous_coordinate(coord: Coordinate, dir: Coordinate) -> Coordinate:
    return coord[0] - dir[0], coord[1] - dir[1]


def left(coord: Coordinate) -> Coordinate:
    return get_next_coordinate(coord, DIRS["<"])


def right(coord: Coordinate) -> Coordinate:
    return get_next_coordinate(coord, DIRS[">"])


def is_horizontal(dir: Coordinate) -> bool:
    return dir[0] == 0


def apply_move(grid: Grid, from_coord: Coordinate, to_coord: Coordinate) -> None:
    grid[to_coord[0]][to_coord[1]] = grid[from_coord[0]][from_coord[1]]
    grid[from_coord[0]][from_coord[1]] = "."


def get_next_coordinates(
    grid: Grid, coordinates: set[Coordinate], dir: Coordinate
) -> set[Coordinate]:
    to_coordinates = set()
    for coordinate in coordinates:
        value = grid[coordinate[0]][coordinate[1]]
        next_coordinate = get_next_coordinate(coordinate, dir)

        if value == "@" or value == "O" or (value in ("[", "]") and is_horizontal(dir)):
            to_coordinates.add(next_coordinate)
        elif value == "[":
            to_coordinates.update((next_coordinate, right(next_coordinate)))
        elif value == "]":
            to_coordinates.update((left(next_coordinate), next_coordinate))

    return to_coordinates


def push_to(grid: Grid, coordinates: set[Coordinate], dir: Coordinate) -> bool:
    if all(grid[coord[0]][coord[1]] == "." for coord in coordinates):
        return True
    if any(grid[coord[0]][coord[1]] == "#" for coord in coordinates):
        return False

    next_coordinates = get_next_coordinates(grid, coordinates, dir)
    if push_to(grid, next_coordinates, dir):
        for next_coordinate in next_coordinates:
            apply_move(grid, get_previous_coordinate(next_coordinate, dir), next_coordinate)
        return True

    return False


def simulate(grid: Grid, moves: Iterable[str]) -> None:
    robot = next(iter(iter_grid(grid, lambda x: x == "@")))
    for move in moves:
        if push_to(grid, {robot}, DIRS[move]):
            robot = get_next_coordinate(robot, DIRS[move])


grid_lines, move_lines = split_lines(get_input(2024, 15))
moves = [char for move_line in move_lines for char in move_line]

grid = [[char for char in line] for line in grid_lines]
simulate(grid, moves)
print(sum(r * 100 + c for r, c in iter_grid(grid, lambda x: x == "O")))

grid = [[char for char in expand_line(line)] for line in grid_lines]
simulate(grid, moves)
print(sum(r * 100 + c for r, c in iter_grid(grid, lambda x: x == "[")))
