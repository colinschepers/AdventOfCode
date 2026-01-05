from utils import get_input, Coordinate


def is_accessible(row: int, col: int, rolls: set[Coordinate]) -> bool:
    neighbors = (
        (row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col - 1), (row, col + 1),
        (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)
    )
    return sum(neighbor in rolls for neighbor in neighbors) < 4


def remove_rolls(rolls: set[Coordinate]) -> set[Coordinate]:
    while roll_to_remove := {roll for roll in rolls if is_accessible(*roll, rolls)}:
        rolls -= roll_to_remove
    return rolls


lines = get_input(2025, 4)
rolls = {(r, c) for r, line in enumerate(lines) for c, char in enumerate(line) if char == "@"}
print(sum(is_accessible(r, c, rolls) for r, c in rolls))
print(len(rolls) - len(remove_rolls(rolls)))
