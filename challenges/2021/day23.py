from functools import lru_cache
from typing import Tuple

from utils import get_input

Hallway = Tuple[int, ...]
Rooms = Tuple[Tuple[int, ...], ...]

HALLWAY = (0, 1, 3, 5, 7, 9, 10)
COSTS = (0, 1, 10, 100, 1000)
WIN = ((1, 1), (2, 2), (3, 3), (4, 4))
CHECK_INDICES = {
    (idx, room_nr): list(range(room_nr + 1, idx, -1)) if idx < room_nr + 2 else range(room_nr + 2, idx)
    for room_nr in range(4) for idx in range(7)
}


def to_value(char: str) -> int:
    return ord(char) - 64 if char != '.' else 0


def is_room_ok(rooms: Rooms, room_nr: int) -> bool:
    return all(not x or x == room_nr + 1 for x in rooms[room_nr])


def is_path_free(hallway: Hallway, idx: int, room_nr: int) -> bool:
    return not any(hallway[i] for i in CHECK_INDICES[(idx, room_nr)])


def move_to_room(hallway: Hallway, rooms: Rooms, idx: int, room_nr: int) -> Tuple[Hallway, Rooms, int]:
    value = hallway[idx]
    entry_idx = value * 2
    idx_in_room = list(i for i, x in enumerate(rooms[room_nr]) if not x)[-1]
    new_hallway = tuple(0 if i == idx else x for i, x in enumerate(hallway))
    new_room = tuple(value if i == idx_in_room else x for i, x in enumerate(rooms[room_nr]))
    new_rooms = tuple(new_room if i == room_nr else x for i, x in enumerate(rooms))
    steps = abs(entry_idx - HALLWAY[idx]) + idx_in_room + 1
    cost = steps * COSTS[value]
    return new_hallway, new_rooms, cost


def move_to_hallway(hallway: Hallway, rooms: Rooms, room_nr: int, idx: int) -> Tuple[Hallway, Rooms, int]:
    entry_idx = (room_nr + 1) * 2
    idx_in_room, value = next((i, x) for i, x in enumerate(rooms[room_nr]) if x)
    new_hallway = tuple(value if i == idx else x for i, x in enumerate(hallway))
    new_room = tuple(0 if i == idx_in_room else x for i, x in enumerate(rooms[room_nr]))
    new_rooms = tuple(new_room if i == room_nr else x for i, x in enumerate(rooms))
    steps = abs(entry_idx - HALLWAY[idx]) + idx_in_room + 1
    cost = steps * COSTS[value]
    return new_hallway, new_rooms, cost


@lru_cache(maxsize=None)
def solve(hallway: Hallway, rooms: Rooms) -> int:
    if rooms == WIN:
        return 0

    for idx in filter(lambda i: hallway[i], range(len(hallway))):
        room_nr = hallway[idx] - 1
        if is_room_ok(rooms, room_nr) and is_path_free(hallway, idx, room_nr):
            new_hallway, new_rooms, cost = move_to_room(hallway, rooms, idx, room_nr)
            return cost + solve(new_hallway, new_rooms)

    min_cost = float('inf')
    for room_nr in filter(lambda i: not is_room_ok(rooms, i), range(len(rooms))):
        for idx in (i for i, x in enumerate(hallway) if not x):
            if is_path_free(hallway, idx, room_nr):
                new_hallway, new_rooms, cost = move_to_hallway(hallway, rooms, room_nr, idx)
                min_cost = min(min_cost, cost + solve(new_hallway, new_rooms))

    return min_cost


data = get_input(year=2021, day=23)
hallway = (to_value(data[1][1]), *(to_value(data[1][c]) for c in range(2, 11, 2)), to_value(data[1][11]))
rooms = tuple((to_value(data[2][c]), to_value(data[3][c])) for c in (3, 5, 7, 9))
print(solve(hallway, rooms))

rooms = ((rooms[0][0], 4, 4, rooms[0][1]), (rooms[1][0], 3, 2, rooms[1][1]),
         (rooms[2][0], 2, 1, rooms[2][1]), (rooms[3][0], 1, 3, rooms[3][1]))
WIN = ((1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 3), (4, 4, 4, 4))
print(solve(hallway, rooms))
