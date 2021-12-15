from collections import defaultdict
from typing import Set

from utils import get_input


def count_paths(current: str, small_visited: Set[str], may_visit_twice: bool) -> int:
    cnt = 0
    for dest in connections[current]:
        if dest == 'start':
            continue
        elif dest == 'end':
            cnt += 1
        elif dest in big_caves:
            cnt += count_paths(dest, small_visited, may_visit_twice)
        elif dest not in small_visited:
            cnt += count_paths(dest, small_visited | {dest}, may_visit_twice)
        elif may_visit_twice:
            cnt += count_paths(dest, small_visited, False)
    return cnt


data = get_input(day=12)

connections = defaultdict(list)
for line in data:
    c1, c2 = line.split("-")
    connections[c1].append(c2)
    connections[c2].append(c1)
big_caves = {x for x in connections if x[0].isupper()}

print(count_paths('start', set(), False))
print(count_paths('start', set(), True))
