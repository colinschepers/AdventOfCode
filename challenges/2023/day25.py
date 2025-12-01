import re
from itertools import combinations
from typing import Sequence

import networkx as nx

from utils import get_input


def _parse(lines: Sequence[str]) -> nx.DiGraph:
    edges = ((nodes[0], dest) for line in lines if (nodes := re.findall(r"\w+", line)) for dest in nodes[1:])
    graph = nx.DiGraph()
    for src, dest in edges:
        graph.add_edge(src, dest, capacity=1)
        graph.add_edge(dest, src, capacity=1)
    return graph


def _solve(graph: nx.DiGraph) -> int:
    nodes = list(graph.nodes())
    for source, sink in combinations(nodes, 2):
        cut_value, (group1, group2) = nx.minimum_cut(graph, source, sink)
        if cut_value == 3:
            return len(group1) * len(group2)


print(_solve(_parse(get_input(year=2023, day=25))))
