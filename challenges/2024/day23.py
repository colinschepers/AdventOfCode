from collections import defaultdict
from collections.abc import Sequence, Iterable, Set
from itertools import combinations
from typing import Tuple, Mapping

from utils import get_input


def get_graph(lines: Sequence[str]) -> Mapping[str, Set[str]]:
    graph: dict[str, set[str]] = defaultdict(set)
    for line in lines:
        pc_a, pc_b = line.split("-")
        graph[pc_a].add(pc_b)
        graph[pc_b].add(pc_a)
    return graph


def get_t_triplets(graph: Mapping[str, Set[str]]) -> Set[Tuple[str, ...]]:
    triplets: set[Tuple[str, ...]] = set()
    for vertex, neigbors in graph.items():
        if not vertex.startswith("t"):
            continue
        for neighbor_1, neighbor_2 in combinations(neigbors, 2):
            if neighbor_2 in graph[neighbor_1]:
                triplets.add(tuple(sorted((vertex, neighbor_1, neighbor_2))))
    return triplets


def bron_kerbosch(
    graph: Mapping[str, Set[str]], reported: set[str], potential: set[str], excluded: set[str]
) -> Iterable[set[str]]:
    if not potential and not excluded:
        yield reported
        return

    pivot = next(iter(potential | excluded))
    for vertex in list(potential - graph[pivot]):
        yield from bron_kerbosch(
            graph,
            reported | {vertex},
            potential & graph[vertex],
            excluded & graph[vertex],
        )
        potential.remove(vertex)
        excluded.add(vertex)


def get_password(graph: Mapping[str, Set[str]]):
    max_cliques = bron_kerbosch(graph, set(), set(graph), set())
    max_clique = max(max_cliques, key=len)
    return ",".join(sorted(max_clique))


graph = get_graph(get_input(2024, 23))
print(len(get_t_triplets(graph)))
print(get_password(graph))
