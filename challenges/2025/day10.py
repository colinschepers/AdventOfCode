from dataclasses import dataclass

import numpy as np

from utils import get_input
from scipy.optimize import milp, LinearConstraint, Bounds


@dataclass
class Machine:
    lights: tuple[bool, ...]
    buttons: tuple[set[int], ...]
    joltage: tuple[int, ...]

    @classmethod
    def from_string(cls, line: str) -> "Machine":
        lights, *buttons, joltage = line.split()
        return Machine(
            lights=tuple(l == "#" for l in lights.strip("[]")),
            buttons=tuple({int(l.strip("()")) for l in b.split(",")} for b in buttons),
            joltage=tuple(map(int, joltage.strip("{}").split(",")))
        )


def get_min_lights(buttons: tuple[set[int], ...], lights: tuple[bool, ...]) -> int:
    if not buttons:
        return 9_999_999 if any(lights) else 0
    return min(
        get_min_lights(buttons[1:], tuple(l ^ (i in buttons[0]) for i, l in enumerate(lights))) + 1,
        get_min_lights(buttons[1:], lights)
    )


def get_min_joltage(buttons: tuple[set[int], ...], joltages: tuple[int, ...]) -> int:
    button_constraints = [[int(i in b) for b in buttons] + [0] for i in range(len(joltages))]
    minimize_constraint = [[1 for _ in buttons] + [-1]]
    constraints = LinearConstraint(
        np.array(button_constraints + minimize_constraint),
        lb=np.array(list(joltages) + [0]),
        ub=np.array(list(joltages) + [0])
    )
    result = milp(
        c=np.array([0] * len(buttons) + [1]),
        constraints=constraints,
        integrality=np.ones(len(buttons) + 1),
        bounds=Bounds(0)
    )
    return int(result.fun)


machines = [Machine.from_string(line) for line in get_input(2025, 10)]
print(sum(get_min_lights(machine.buttons, machine.lights) for machine in machines))
print(sum(get_min_joltage(machine.buttons, machine.joltage) for machine in machines))
