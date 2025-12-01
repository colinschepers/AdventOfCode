from collections.abc import Iterable, Set
from itertools import chain

from utils import get_input, Grid, Coordinate

Region = Set[Coordinate]


def is_inside(garden: Grid, row: int, col: int) -> bool:
    return 0 <= row < len(garden) and 0 <= col < len(garden[0])


def get_region_at(garden: Grid, coordinate: Coordinate) -> Region:
    region: set[Coordinate] = set()
    stack = [coordinate]
    while stack:
        r, c = stack.pop()
        region.add((r, c))
        stack.extend(
            (nr, nc)
            for nr, nc in ((r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1))
            if (nr, nc) not in region and is_inside(garden, nr, nc)
            and garden[r][c] == garden[nr][nc]
        )
    return region


def get_regions(garden: Grid) -> Iterable[Region]:
    seen: set[Coordinate] = set()
    coordinates = ((r, c) for r in range(len(garden)) for c in range(len(garden[r])))
    for coordinate in coordinates:
        if coordinate not in seen:
            region = get_region_at(garden, coordinate)
            yield region
            seen.update(region)


def get_price(region: Region, discounted: bool = False) -> int:
    fences_north = {
        (r, c) for r, c in region if not is_inside(garden, r - 1, c) or (r - 1, c) not in region
    }
    fences_south = {
        (r, c) for r, c in region if not is_inside(garden, r + 1, c) or (r + 1, c) not in region
    }
    fences_west = {
        (r, c) for r, c in region if not is_inside(garden, r, c - 1) or (r, c - 1) not in region
    }
    fences_east = {
        (r, c) for r, c in region if not is_inside(garden, r, c + 1) or (r, c + 1) not in region
    }
    fences = list(chain(
        ((r, c) for r, c in fences_north if (r, c - 1) not in fences_north),
        ((r, c) for r, c in fences_south if (r, c - 1) not in fences_south),
        ((r, c) for r, c in fences_west if (r - 1, c) not in fences_west),
        ((r, c) for r, c in fences_east if (r - 1, c) not in fences_east)
    )) if discounted else list(chain(fences_north, fences_south, fences_west, fences_east))

    return len(region) * len(fences)


garden = [[char for char in line] for line in get_input(2024, 12)]
regions = list(get_regions(garden))

print(sum(get_price(region) for region in regions))
print(sum(get_price(region, discounted=True) for region in regions))
