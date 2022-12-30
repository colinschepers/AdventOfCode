from collections import defaultdict
from functools import lru_cache
from pathlib import Path
from typing import List, Sequence, DefaultDict

from utils import get_input


def build_filesystem(lines: Sequence[str]) -> DefaultDict[str, List]:
    filesystem = defaultdict(list)
    path = Path()
    for line in lines:
        parts = line.split(" ")
        if parts[0] == "$" and parts[1] == "cd":
            if parts[2] == "..":
                path = path.parent
            else:
                path /= parts[2]
        elif parts[0] != "$":
            if parts[0] == "dir":
                filesystem[str(path)].append(str(path / parts[1]))
            else:
                filesystem[str(path)].append(int(parts[0]))
    return filesystem


@lru_cache(maxsize=None)
def get_size(path: str) -> int:
    return sum(item if isinstance(item, int) else get_size(item) for item in filesystem[path])


filesystem = build_filesystem(get_input(year=2022, day=7))
print(sum(get_size(path) for path in list(filesystem) if get_size(path) < 100000))

unused = 70000000 - get_size(next(iter(filesystem)))
needed = 30000000 - unused
print(min(get_size(path) for path in list(filesystem) if get_size(path) >= needed))
