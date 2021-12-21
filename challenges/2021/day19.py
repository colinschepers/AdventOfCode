from collections import defaultdict
from itertools import combinations
from typing import Tuple, Sequence, List

from utils import get_input, split_lines, manhattan

Coordinate = Tuple[int, int, int]
MATCH_COUNT = 12


class Scanner:
    def __init__(self, coordinates: List[Coordinate]):
        self.absolute_location = (0, 0, 0)
        self.coordinates = coordinates
        self._permutations = list(get_permutations(coordinates))

    def match(self, other: 'Scanner') -> bool:
        for permutation in self._permutations:
            translations = ((x1 - x2, y1 - y2, z1 - z2)
                            for x1, y1, z1 in other.coordinates for x2, y2, z2 in permutation)
            match_counts = defaultdict(int)
            for translation in translations:
                match_counts[translation] += 1
                if match_counts[translation] >= MATCH_COUNT:
                    self.absolute_location = tuple(map(sum, zip(self.absolute_location, translation)))
                    self.coordinates = [tuple(map(sum, zip(c, translation))) for c in permutation]
                    return True
        return False


def rotate(coordinates: Sequence[Coordinate]) -> Sequence[Coordinate]:
    return [(-y, x, z) for x, y, z in coordinates]


def flip(coordinates: Sequence[Coordinate]) -> Sequence[Coordinate]:
    return [(x, z, -y) for x, y, z in coordinates]


def get_permutations(coordinates: Sequence[Coordinate]) -> Sequence[Coordinate]:
    for _ in range(2):
        for _ in range(3):
            yield coordinates
            coordinates = rotate(coordinates)
            for _ in range(3):
                yield coordinates
                coordinates = flip(coordinates)
        coordinates = rotate(flip(rotate(coordinates)))


scanners = [Scanner([tuple(map(int, line.split(','))) for line in lines[1:]])
            for lines in split_lines(get_input(year=2021, day=19))]

base_scanner, remaining_scanners = scanners[0], scanners[1:]
while remaining_scanners:
    for scanner in list(remaining_scanners):
        if scanner.match(base_scanner):
            base_scanner.coordinates = list(set(base_scanner.coordinates + scanner.coordinates))
            remaining_scanners.remove(scanner)

print(len(base_scanner.coordinates))
print(max(manhattan(a.absolute_location, b.absolute_location) for a, b in combinations(scanners, 2)))
