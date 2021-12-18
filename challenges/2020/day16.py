import re
from math import prod
from typing import Tuple, Sequence, Mapping

from utils import get_input

Ticket = Sequence[int]
Fields = Mapping[str, Tuple[Tuple[int, int], Tuple[int, int]]]


def load(data: Sequence[str]) -> Tuple[Fields, Ticket, Sequence[Ticket]]:
    fields = {}
    my_ticket = None
    tickets = []

    for i in range(len(data)):
        m = re.match('^([^:]+): (\d+)-(\d+) or (\d+)-(\d+)', data[i])
        if m:
            fields[m.group(1)] = ((int(m.group(2)), int(m.group(3))), (int(m.group(4)), int(m.group(5))))
        elif data[i - 1] == 'your ticket:':
            my_ticket = [int(x) for x in data[i].split(',')]
        elif my_ticket and re.match('^[\d,]+$', data[i]):
            tickets.append([int(x) for x in data[i].split(',')])

    return fields, my_ticket, tickets


def in_ranges(value: int, ranges: Sequence[Tuple[int, int]]) -> bool:
    return any(range[0] <= value <= range[1] for range in ranges)


def get_scanning_error_rate() -> int:
    result = 0
    all_ranges = [range for field_ranges in fields.values() for range in field_ranges]
    for value in [value for ticket in tickets for value in ticket]:
        if not in_ranges(value, all_ranges):
            result += value
    return result


def get_valid_tickets():
    all_ranges = [range for field_ranges in fields.values() for range in field_ranges]
    for ticket in tickets:
        if all((in_ranges(value, all_ranges) for value in ticket)):
            yield ticket


def get_mapping(tickets: Sequence[Ticket]):
    mapping = [[] for _ in range(len(tickets[0]))]
    for fi in range(len(tickets[0])):
        values = [ticket[fi] for ticket in tickets]
        for field_name, ranges in fields.items():
            if all(in_ranges(value, ranges) for value in values):
                mapping[fi].append(field_name)
    while any(len(m) > 1 for m in mapping):
        fixed = set([m[0] for m in mapping if len(m) == 1])
        for i in range(len(mapping)):
            mapping[i] = [field_name for field_name in mapping[i] if len(mapping[i]) == 1 or field_name not in fixed]
    return {m[0]: i for i, m in enumerate(mapping)}


fields, my_ticket, tickets = load(get_input(year=2020, day=16))
print(get_scanning_error_rate())

mapping = get_mapping(list(get_valid_tickets()))
print(prod(my_ticket[mapping[f]] for f in fields if f.startswith('departure')))
