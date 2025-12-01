import re
from collections import deque
from dataclasses import dataclass
from math import prod, lcm
from typing import Sequence, Tuple, Mapping, Iterable

from more_itertools import first

from utils import get_input


@dataclass
class Module:
    name: str
    type: str
    memory: bool | dict[str, bool]
    outputs: tuple[str]


def _parse(lines: Sequence[str]) -> Mapping[str, Module]:
    modules = {
        m[2]: Module(m[2], m[1], {} if m[1] == "&" else False, tuple(m[3].split(", ")))
        for line in lines if (m := re.match(r"([%&]?)(\w+) -> ([\w, ]+)", line))
    }
    for module in modules.values():
        for output_name in module.outputs:
            if output_name in modules and modules[output_name].type == "&":
                modules[output_name].memory[module.name] = False
    return {"button": Module("button", "", False, ("broadcaster",))} | modules


def get_pulse(module: Module, received_pulse: bool, received_from: str) -> bool:
    if module.type == "%" and isinstance(module.memory, bool):
        module.memory = not module.memory
        return module.memory
    elif module.type == "&" and isinstance(module.memory, dict):
        module.memory[received_from] = received_pulse
        return not all(module.memory.values())
    return False


def _generate(modules: Mapping[str, Module], button_count: int) -> Iterable[Tuple[int, str, bool, str]]:
    for button_press in range(1, button_count + 1):
        queue = deque([("button", False, "broadcaster")])
        while queue:
            received_from, received_pulse, name = queue.popleft()
            yield button_press, received_from, received_pulse, name
            if name not in modules or (modules[name].type == "%" and received_pulse):
                continue
            pulse = get_pulse(modules[name], received_pulse, received_from)
            queue.extend(((name, pulse, output) for output in modules[name].outputs))


def _get_pulse_counts(modules: Mapping[str, Module], button_count: int) -> Tuple[int, int]:
    pulses = list(pulse for _, _, pulse, _ in _generate(modules, button_count))
    return sum(pulses), sum(not p for p in pulses)


def _get_button_presses(modules: Mapping[str, Module], final_module: str) -> int:
    final_conjunction = first((m for m in modules.values() if final_module in m.outputs))
    final_input_triggers = {m: [] for m in final_conjunction.memory}
    for button_press, received_from, received_pulse, name in _generate(modules, button_count=1000000):
        if name == final_conjunction.name and received_pulse:
            final_input_triggers[received_from].append(button_press)
            if all(len(x) >= 2 for x in final_input_triggers.values()):
                cycles = [x[0] - x[1] for x in final_input_triggers.values()]
                return lcm(*cycles)


modules = _parse(get_input(year=2023, day=20))
print(prod(_get_pulse_counts(modules, button_count=1000)))
print(_get_button_presses(modules, final_module="rx"))
