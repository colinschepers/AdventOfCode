import re
from functools import cache

from utils import get_input, split_lines


@cache
def get_num_ways(pattern: str, towels: frozenset[str]) -> int:
    if len(pattern) == 0:
        return 1
    sub_patterns = (pattern[:i] for i in range(len(pattern)) if pattern[i:] in towels)
    return sum((get_num_ways(sub_pattern, towels) for sub_pattern in sub_patterns), 0)


towel_lines, patterns = split_lines(get_input(2024, 19))
towels = frozenset(re.findall(r"[a-z]+", towel_lines[0]))

print(sum(get_num_ways(pattern, towels) > 0 for pattern in patterns))
print(sum(get_num_ways(pattern, towels) for pattern in patterns))
