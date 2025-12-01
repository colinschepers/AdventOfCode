import re
from collections.abc import Mapping
from operator import or_, and_, xor
from typing import Tuple

import graphviz

from utils import get_input, split_lines

Wires = dict[str, int]
Gate = Tuple[str, ...]

OPERATORS = {"OR": or_, "AND": and_, "XOR": xor}
SHAPES = {"AND": "box", "XOR": "diamond", "OR": "triangle", 0: "doubleoctagon", 1: "doublecircle"}
COLORS = {0: "lightgray", 1: "darkgrey"}


def get_value(name: str, wires: Mapping[str, int], gates: Mapping[str, Gate]) -> int:
    if name in wires:
        return wires[name]
    left, operation, right = gates[name]
    return OPERATORS[operation](get_value(left, wires, gates), get_value(right, wires, gates))


def get_z(wires: Mapping[str, int], gates: Mapping[str, Gate]) -> int:
    z_gates = sorted(name for name in gates if name.startswith("z"))
    bits = (get_value(name, wires, gates) for name in z_gates)
    return sum(bit << significance for significance, bit in enumerate(bits))


def is_error(name: str, gates: dict[str, Gate]) -> bool:
    left, operation, right = gates[name]

    if left == "x00" or right == "x00" or name == "z45":
        return False
    if name.startswith("z") and operation != "XOR":
        return True
    if operation == "XOR":
        return (
            not ({name[0], left[0], right[0]} & {"x", "y", "z"})
            or any((name == l or name == r) and op == "OR" for l, op, r in gates.values())
        )
    if operation == "AND":
        return any((name == l or name == r) and op != "OR" for l, op, r in gates.values())

    return False


def plot_graph(wires: Mapping[str, int], gates: Mapping[str, Gate]) -> None:
    viz_graph = graphviz.Digraph()

    wire_values = [(wire, value) for wire, value in wires.items()]
    gate_values = [(name, operation) for name, (_, operation, _) in gates.items()]
    for name, operation in wire_values + gate_values:
        viz_graph.attr(
            'node',
            style='filled',
            shape=SHAPES[operation],
            color=COLORS[get_value(name, wires, gates)]
        )
        viz_graph.node(name)

    for name, (left, operation, right) in gates.items():
        viz_graph.edge(name, left)
        viz_graph.edge(name, right)

    viz_graph.render('binary_tree', view=True, format='png')


value_lines, gate_lines = split_lines(get_input(2024, 24))
wires = {line.split(":")[0]: int(line[-1]) for line in value_lines}
gates = {m[-1]: tuple(m[:-1]) for line in gate_lines if (m := re.findall(r"\w+", line))}

print(get_z(wires, gates))
print(",".join(sorted(name for name in gates if is_error(name, gates))))
