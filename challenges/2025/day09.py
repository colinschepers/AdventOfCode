from bisect import bisect
from collections.abc import Sequence
from dataclasses import dataclass
from itertools import islice, takewhile

from more_itertools import first

from utils import get_input


@dataclass
class Coordinate:
    x: int
    y: int


@dataclass
class Line:
    a: Coordinate
    b: Coordinate

    def __post_init__(self):
        if self.a.x > self.b.x or self.a.y > self.b.y:
            self.a, self.b = self.b, self.a

    @property
    def is_horizontal(self) -> bool:
        return self.a.y == self.b.y

    def intersects(self, other: "Line") -> bool:
        if self.is_horizontal and not other.is_horizontal:
            return self.a.x < other.a.x < self.b.x and other.a.y < self.a.y < other.b.y
        if not self.is_horizontal and other.is_horizontal:
            return other.a.x < self.a.x < other.b.x and self.a.y < other.a.y < self.b.y
        return False


@dataclass
class Square:
    a: Coordinate
    b: Coordinate

    def __post_init__(self):
        if self.a.x > self.b.x:
            self.a, self.b = self.b, self.a

    @property
    def area(self) -> int:
        return (abs(self.a.x - self.b.x) + 1) * (abs(self.a.y - self.b.y) + 1)

    @property
    def top(self) -> Line:
        return Line(Coordinate(self.a.x, self.a.y), Coordinate(self.b.x, self.a.y))

    @property
    def bottom(self) -> Line:
        return Line(Coordinate(self.a.x, self.b.y), Coordinate(self.b.x, self.b.y))

    @property
    def left(self) -> Line:
        return Line(Coordinate(self.a.x, self.a.y), Coordinate(self.a.x, self.b.y))

    @property
    def right(self) -> Line:
        return Line(Coordinate(self.b.x, self.a.y), Coordinate(self.b.x, self.b.y))

    def shrink(self) -> "Square":
        return Square(
            Coordinate(self.a.x + 1, self.a.y + 1 if self.a.y < self.b.y else self.a.y - 1),
            Coordinate(self.b.x - 1, self.b.y - 1 if self.a.y < self.b.y else self.b.y + 1),
        )


def is_vertically_intersected(square: Square, vertical_lines: Sequence[Line]) -> bool:
    top, bottom = square.top, square.bottom
    start = bisect(vertical_lines, top.a.x, key=lambda line: line.a.x)
    return any(
        (line.a.y <= top.a.y <= line.b.y) or
        (line.a.y <= bottom.a.y <= line.b.y)
        for line in takewhile(lambda l: l.a.x < top.b.x, islice(vertical_lines, start, None))
    )


def is_horizontally_intersected(square: Square, horizontal_lines: Sequence[Line]) -> bool:
    left, right = square.left, square.right
    start = bisect(horizontal_lines, left.a.y, key=lambda line: line.a.y)
    return any(
        (line.a.x <= left.a.x <= line.b.x) or
        (line.a.x <= right.a.x <= line.b.x)
        for line in takewhile(lambda l: l.a.y < left.b.y, islice(horizontal_lines, start, None))
    )


def get_largest_area(red_tiles: list[Coordinate], strict: bool) -> int:
    squares = (
        Square(red_tiles[i], red_tiles[j])
        for i in range(len(red_tiles))
        for j in range(i + 1, len(red_tiles))
    )

    if not strict:
        return max(square.area for square in squares)

    border = [Line(a, b) for a, b in zip(red_tiles, red_tiles[1:] + [red_tiles[0]])]
    vertical_lines = sorted((line for line in border if line.a.x == line.b.x), key=lambda line: line.a.x)
    horizontal_lines = sorted((line for line in border if line.a.y == line.b.y), key=lambda line: line.a.y)

    return first(
        square.area
        for square in sorted(squares, key=lambda s: s.area, reverse=True)
        if not is_vertically_intersected(square.shrink(), vertical_lines)
        and not is_horizontally_intersected(square.shrink(), horizontal_lines)
    )


line_nrs = (line.split(",") for line in get_input(2025, 9))
red_tiles = [Coordinate(int(x), int(y)) for x, y in line_nrs]

print(get_largest_area(red_tiles, strict=False))
print(get_largest_area(red_tiles, strict=True))
