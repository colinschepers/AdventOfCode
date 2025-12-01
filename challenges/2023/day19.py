import re
from math import prod
from typing import Sequence, Tuple, Mapping

from more_itertools import first

from utils import get_input, split_lines

Workflow = Tuple[str, str, int, str]
Part = Mapping[str, int]
PartRanges = Mapping[str, Tuple[int, int]]


def _parse(lines: Sequence[str]) -> Tuple[Mapping[str, Workflow], Sequence[Part]]:
    workflow_lines, part_lines = split_lines(lines)
    workflows = {
        workflow_line.split("{")[0]: (
                [(m[1], m[2], int(m[3]), m[4]) for m in re.finditer(r"(\w)([<>])(\d+):(\w+)", workflow_line)] +
                [(None, None, None, re.search(r",(\w+)}", workflow_line)[1])]
        ) for workflow_line in workflow_lines
    }
    parts = [{m[1]: int(m[2]) for m in re.finditer(r"(\w+)=(\d+)", part_line)} for part_line in part_lines]
    return workflows, parts


def _is_accepted(part: Part) -> bool:
    workflow_name = "in"
    while workflow := workflows.get(workflow_name):
        workflow_name = first(
            target for category, sign, value, target in workflow
            if not sign or sign == "<" and part[category] < value or sign == ">" and part[category] > value
        )
    return workflow_name == 'A'


def _split(part_ranges: PartRanges, category: str, value: int) -> Tuple[PartRanges, PartRanges]:
    return ({cat: (start, value if cat == category else end) for cat, (start, end) in part_ranges.items()},
            {cat: (value if cat == category else start, end) for cat, (start, end) in part_ranges.items()})


def _get_accepted_count(workflow_name: str, part_ranges: PartRanges) -> int:
    if workflow_name == 'R' or not all(end - start > 0 for start, end in part_ranges.values()):
        return 0
    if workflow_name == 'A':
        return prod(start - end for start, end in part_ranges.values())

    total = 0
    for category, sign, value, target in workflows[workflow_name]:
        accepted = part_ranges
        if sign == "<":
            accepted, part_ranges = _split(part_ranges, category, value)
        elif sign == ">":
            part_ranges, accepted = _split(part_ranges, category, value + 1)
        total += _get_accepted_count(target, accepted)
    return total


workflows, parts = _parse(get_input(year=2023, day=19))
print(sum(sum(part.values()) for part in parts if _is_accepted(part)))
print(_get_accepted_count("in", {"x": (1, 4001), "m": (1, 4001), "a": (1, 4001), "s": (1, 4001)}))
