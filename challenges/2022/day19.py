import re
from math import prod
from typing import Tuple, Dict, List

from utils import get_input

Materials = Tuple[int, ...]
Costs = Tuple[Materials, ...]


def buy(costs: Costs, income: Materials, resources: Materials, robot_bought: int) -> Tuple[Materials, Materials]:
    return tuple(income[i] + int(i == robot_bought) for i in range(4)), \
           tuple(resources[i] + income[i] - costs[robot_bought][i] for i in range(4))


def solve(t: int, costs: Costs, cache: Dict[Tuple[int, Materials], Materials], best: List[int],
          income: Materials = (1, 0, 0, 0), resources: Materials = (0, 0, 0, 0)) -> int:
    if t == 1:
        return resources[-1] + income[-1]

    upper_bound = resources[-1] + (income[-1] + t) * (income[-1] + t + 1) // 2 - (income[-1] - 1) * income[-1] // 2
    if upper_bound <= best[0]:
        return -1

    key = (t, income)
    if key in cache and all(resources[i] <= cache[key][i] for i in range(4)):
        return -1
    cache[key] = tuple(max(resources[i], cache.get(key, resources)[i]) for i in range(4))

    if costs[3][0] <= resources[0] and costs[3][2] <= resources[2]:
        return solve(t - 1, costs, cache, best, *buy(costs, income, resources, 3))
    if costs[2][0] <= resources[0] and costs[2][1] <= resources[1] and income[2] < costs[3][2]:
        best[0] = max(best[0], solve(t - 1, costs, cache, best, *buy(costs, income, resources, 2)))
    if costs[1][0] <= resources[0] and income[1] < costs[2][1]:
        best[0] = max(best[0], solve(t - 1, costs, cache, best, *buy(costs, income, resources, 1)))
    if costs[0][0] <= resources[0] and not all(income[0] >= costs[r2][0] for r2 in range(4)):
        best[0] = max(best[0], solve(t - 1, costs, cache, best, *buy(costs, income, resources, 0)))
    return max(best[0], solve(t - 1, costs, cache, best, income, tuple(resources[i] + income[i] for i in range(4))))


blueprints = [((x[1], 0, 0, 0), (x[2], 0, 0, 0), (x[3], x[4], 0, 0), (x[5], 0, x[6], 0))
              for x in (list(map(int, re.findall(r"\d+", line))) for line in get_input(year=2022, day=19))]
print(sum(bp * solve(24, blueprint, {}, [0]) for bp, blueprint in enumerate(blueprints, start=1)))
print(prod(solve(32, blueprint, {}, [0]) for blueprint in blueprints[:3]))
