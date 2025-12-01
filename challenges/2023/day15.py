import re
from collections import OrderedDict
from functools import reduce
from typing import Sequence

from utils import get_input


def _hash(step: str) -> int:
    return reduce(lambda total, x: ((total + x) * 17) % 256, map(ord, step), 0)


def _get_focusing_power(steps: Sequence[str]) -> int:
    boxes = [OrderedDict() for _ in range(256)]
    for step in steps:
        label, suffix = re.split(r"[-=]", step)
        box = boxes[_hash(label)]
        if suffix:
            box[label] = int(suffix)
        else:
            box.pop(label, None)

    return sum(
        box_nr * slot_nr * focal_len
        for box_nr, box in enumerate(boxes, start=1)
        for slot_nr, focal_len in enumerate(box.values(), start=1)
    )


steps = get_input(year=2023, day=15)[0].split(",")
print(sum(map(_hash, steps)))
print(_get_focusing_power(steps))
