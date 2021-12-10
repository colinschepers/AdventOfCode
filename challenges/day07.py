from functools import partial
from typing import Sequence, Callable

from utils import get_input


class LazyList(list):
    def __getitem__(self, key):
        item = super().__getitem__(key)
        if callable(item):
            item = item()
            super().__setitem__(key, item)
        return item


def fuel_metric_constant(x: int, y: int) -> int:
    return abs(x - y)


def fuel_metric_increment(x: int, y: int) -> int:
    dis = abs(x - y)
    return dis * (dis + 1) // 2


def get_fuel_cost(fuel_metric: Callable[[int, int], int], position: int):
    return sum(fuel_metric(crab, position) for crab in crabs)


def binary_search(seq: Sequence):
    left, right = 0, len(seq) - 1
    mid = int(left + (right - left) / 2)
    while left < mid < right:
        if seq[mid - 1] < seq[mid]:
            right = mid
        else:
            left = mid
        mid = int(left + (right - left) / 2)
    return seq[mid]


data = get_input(day=7)
crabs = sorted(list(map(int, data[0].split(','))))

costs = LazyList(partial(get_fuel_cost, fuel_metric_constant, pos) for pos in range(crabs[0], crabs[-1] + 1))
print(binary_search(costs))

costs = LazyList(partial(get_fuel_cost, fuel_metric_increment, pos) for pos in range(crabs[0], crabs[-1] + 1))
print(binary_search(costs))
