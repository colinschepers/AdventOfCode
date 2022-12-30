from math import ceil

from more_itertools import first

from utils import get_input

WIDTH = 7
ROCKS = (
    int('1111000', 2) << (3 * WIDTH) >> 2,
    int('010000011100000100000', 2) << (3 * WIDTH) >> 2,
    int('001000000100001110000', 2) << (3 * WIDTH) >> 2,
    int('1000000100000010000001000000', 2) << (3 * WIDTH) >> 2,
    int('11000001100000', 2) << (3 * WIDTH) >> 2
)
LEFT = int('1000000' * 999999, 2)
RIGHT = int('0000001' * 999999, 2)
JETS = tuple(c == "<" for c in first(get_input(year=2022, day=17)))
CACHE_MAX_ROWS = 15


def get_height(total_rocks: int):
    num_rocks, rock_idx, jet_idx, height, cache = 0, 0, 0, 1, {}
    rock = ROCKS[rock_idx] << WIDTH
    mask = int('1111111', 2)

    while num_rocks < total_rocks:
        key = (rock_idx, jet_idx, mask >> (max(0, height - CACHE_MAX_ROWS) * WIDTH))
        if key in cache:
            old_num_rocks, old_height = cache[key]
            factor = (total_rocks - num_rocks) // (num_rocks - old_num_rocks)
            height += factor * (height - old_height)
            num_rocks += factor * (num_rocks - old_num_rocks)

        if JETS[jet_idx] and not rock & LEFT:
            rock_left = rock << 1
            rock = rock if rock_left & mask else rock_left
        elif not JETS[jet_idx] and not rock & RIGHT:
            rock_right = rock >> 1
            rock = rock if rock_right & mask else rock_right
        jet_idx = (jet_idx + 1) % len(JETS)

        rock_down = rock >> WIDTH
        if not rock_down & mask:
            rock = rock_down
        else:
            height_mask = ceil((mask.bit_length()) / WIDTH)
            height_rock = ceil((rock.bit_length()) / WIDTH)
            height += max(height_rock - height_mask, 0)
            cache[key] = num_rocks, height
            mask |= rock
            num_rocks += 1
            rock_idx = (rock_idx + 1) % len(ROCKS)
            rock = ROCKS[rock_idx] << (max(height_rock, height_mask) * WIDTH)

    return height - 1


print(get_height(2022))
print(get_height(1000000000000))
