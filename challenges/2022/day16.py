import re
from collections import deque
from functools import lru_cache
from typing import Dict, Tuple, Iterable

from utils import get_input


def get_tunnels() -> Dict[int, Dict[int, int]]:
    tunnels = {src: {dest: float('inf') for dest in valves.values()} for src in range(len(valves))}
    stack = deque((src, dest, 1) for src, conns in enumerate(connections) for dest in conns)
    while stack:
        src, dest, length = stack.popleft()
        if length < tunnels[src][dest]:
            tunnels[src][dest] = length
            stack.extend((src, nxt, length + 1) for nxt in connections[dest])
    return {src: {dest: tunnels[src][dest] for dest in tunnels[src] if src != dest and flow_rates[dest]}
            for src in tunnels if src == 0 or flow_rates[src]}


@lru_cache(maxsize=None)
def get_best(t: int, valve: int = 0, opened: int = 0) -> int:
    return max((
        flow_rates[dest] * (t - length - 1) + get_best(t - length - 1, dest, opened | (1 << dest))
        for dest, length in tunnels[valve].items()
        if t - length - 1 > 0 and opened & (1 << dest) == 0
    ), default=0)


@lru_cache(maxsize=None)
def get_all(t: int, valve: int = 0, opened: int = 0) -> Iterable[Tuple[int, int]]:
    return [(opened, 0)] + [
        (result_opened, flow_rates[dest] * (t - length - 1) + pressure_release)
        for dest, length in tunnels[valve].items()
        if t - length - 1 > 0 and opened & (1 << dest) == 0
        for result_opened, pressure_release in get_all(t - length - 1, dest, opened | (1 << dest))
    ]


def get_best_with_elephant(t: int) -> int:
    results_without_duplicates = {opened: pressure_release for opened, pressure_release in sorted(get_all(t))}
    results_sorted = list(sorted(results_without_duplicates.items(), reverse=True, key=lambda r: r[1]))

    best_pressure_release = 0
    for my_opened, my_pressure_release in results_sorted:
        for elephant_opened, elephant_pressure_release in results_sorted:
            if my_pressure_release + elephant_pressure_release < best_pressure_release:
                break
            if my_opened & elephant_opened == 0:
                best_pressure_release = my_pressure_release + elephant_pressure_release
    return best_pressure_release


lines = get_input(year=2022, day=16)
parsed = sorted([re.findall("[A-Z]{2}|\\d+", line) for line in lines])
valves = {value[0]: i for i, value in enumerate(parsed)}
flow_rates = [int(value[1]) for value in parsed]
connections = [[valves[c] for c in value[2:]] for value in parsed]
tunnels = get_tunnels()

print(get_best(30))
print(get_best_with_elephant(26))
