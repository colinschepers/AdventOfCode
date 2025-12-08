from collections import Counter
from collections.abc import Sequence
from math import dist, prod

from utils import get_input

CoordinateId = int
CircuitId = int
Coordinate = tuple[int, int, int]
Distance = tuple[float, CoordinateId, CoordinateId]

TOP_CIRCUITS = 3


def solve(coordinates: Sequence[Coordinate], sorted_distances: Sequence[Distance]) -> int:
    circuits: dict[CoordinateId, CircuitId] = {}
    max_circuit_nr = 0

    for _, i, j in sorted_distances:
        if i in circuits and j in circuits:
            circuit_nr_to_merge = circuits[j]
            for idx, circuit_nr in circuits.items():
                if circuit_nr == circuit_nr_to_merge:
                    circuits[idx] = circuits[i]
        elif i in circuits:
            circuits[j] = circuits[i]
        elif j in circuits:
            circuits[i] = circuits[j]
        else:
            circuits[i] = max_circuit_nr
            circuits[j] = max_circuit_nr
            max_circuit_nr += 1

        if len(circuits) == len(coordinates):
            return coordinates[i][0] * coordinates[j][0]

    circuit_counts = [cnt for _, cnt in Counter(circuits.values()).most_common()]
    return prod(circuit_counts[:TOP_CIRCUITS])


line_nrs = [line.split(",") for line in get_input(2025, 8)]
coordinates = [(int(x), int(y), int(z)) for x, y, z in line_nrs]
is_example = len(coordinates) < 100
connection_count = 10 if is_example else 1000

sorted_distances = sorted(
    (dist(coordinates[i], coordinates[j]), i, j)
    for i in range(len(coordinates) - 1)
    for j in range(i + 1, len(coordinates))
)

print(solve(coordinates, sorted_distances[:connection_count]))
print(solve(coordinates, sorted_distances))
