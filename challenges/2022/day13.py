from functools import cmp_to_key
from itertools import zip_longest, starmap
from math import prod
from typing import Optional, Union

from more_itertools import chunked

from utils import get_input

Packet = Optional[Union[int, list]]


def compare(left: Packet, right: Packet) -> int:
    if left is None or right is None:
        return -1 if left is None else 1
    elif isinstance(left, list) or isinstance(right, list):
        pairs = zip_longest([left] if isinstance(left, int) else left, [right] if isinstance(right, int) else right)
        return next(filter(bool, starmap(compare, pairs)), 0)
    return (left > right) - (left < right)


packets = [eval(line) for line in get_input(year=2022, day=13) if line]
print(sum(i for i, pair in enumerate(chunked(packets, 2), start=1) if compare(*pair) < 0))

divider_packets = [[[2]], [[6]]]
sorted_packets = sorted(packets + divider_packets, key=cmp_to_key(compare))
print(prod(i for i, packet in enumerate(sorted_packets, start=1) if packet in divider_packets))
