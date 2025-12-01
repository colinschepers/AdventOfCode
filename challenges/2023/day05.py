import re
from typing import Sequence, Tuple

from utils import get_input

Ranges = Sequence[Tuple[int, int]]
Map = Sequence[Tuple[int, int, int]]


def _parse(lines: Sequence[str]) -> Tuple[Sequence[int], Ranges, Sequence[Map]]:
    seeds = [int(m.group()) for m in re.finditer(r"\d+", lines[0])]
    seed_ranges = [(start, start + range_) for start, range_ in zip(seeds[::2], seeds[1::2])]

    maps = []
    for line in lines:
        if re.match(r"(\w+)-to-(\w+) map:", line):
            maps.append([])
        elif match := re.match(r"(\d+) (\d+) (\d+)", line):
            dest_start, source_start, range_len = map(int, match.groups())
            maps[-1].append((source_start, source_start + range_len, dest_start - source_start))

    for i in range(len(maps)):
        maps[i] = sorted(maps[i])

    return seeds, seed_ranges, maps


def _get_next_ranges(map: Map, ranges: Ranges) -> Ranges:
    next_ranges = []

    for start, end in ranges:
        for source_start, source_end, delta in map:
            if start < source_start and end < source_start:
                next_ranges.append((start, end))
                break
            elif start < source_start and end < source_end:
                next_ranges.append((start, source_start))
                next_ranges.append((source_start + delta, end + delta))
                break
            elif start < source_start and end >= source_end:
                next_ranges.append((start, source_start))
                next_ranges.append((source_start + delta, end + delta))
                start = source_end
            elif start < source_end and end < source_end:
                next_ranges.append((start + delta, end + delta))
                break
            elif start < source_end and end >= source_end:
                next_ranges.append((start + delta, source_end + delta))
                start = source_end
        else:
            if start < end:
                next_ranges.append((start, end))

    return next_ranges


def _get_location_ranges(ranges: Ranges) -> Ranges:
    for map in maps:
        ranges = _get_next_ranges(map, ranges)
    return ranges


seeds, seed_ranges, maps = _parse(get_input(year=2023, day=5))

print(min(start for start, _ in _get_location_ranges([(s, s) for s in seeds])))
print(min(start for start, _ in _get_location_ranges(seed_ranges)))
