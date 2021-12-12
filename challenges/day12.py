from collections import defaultdict
from typing import Set

from utils import get_input


def count_paths(current: str, visited: Set[str], may_visit_twice: bool) -> int:
    cnt = 0
    for dest in connections[current]:
        if dest == 'start':
            continue
        elif dest == 'end':
            cnt += 1
        elif dest[0].isupper() or dest not in visited:
            cnt += count_paths(dest, visited | {dest}, may_visit_twice)
        elif may_visit_twice:
            cnt += count_paths(dest, visited | {dest}, False)
    return cnt


data = get_input(day=12)

connections = defaultdict(list)
for line in data:
    c1, c2 = line.split("-")
    connections[c1].append(c2)
    connections[c2].append(c1)

print(count_paths('start', set(), False))
print(count_paths('start', set(), True))
