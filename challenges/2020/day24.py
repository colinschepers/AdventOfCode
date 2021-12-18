import re
import time


tiles = open('./data/day24.txt').read().strip().split('\n')


def get_black_tiles(tiles):
    black_tiles = []
    for tile in tiles:
        x, y = 0, 0
        for m in re.findall('[sn]?[we]', tile):
            if m == 'e':
                x += 2
            elif m == 'w':
                x -= 2
            elif m[-1] == 'e':
                x += 1
            elif m[-1] == 'w':
                x -= 1
            if m[0] == 's':
                y += 1
            elif m[0] == 'n':
                y -= 1
        coord = (x, y)
        if coord in black_tiles:
            black_tiles.remove(coord)
        else:
            black_tiles.append(coord)
    return set(black_tiles)


start_time = time.time()
black_tiles = get_black_tiles(tiles)
print(len(black_tiles), f"\t{time.time() - start_time}s")


def get_neighbors(coord):
    return [
        (coord[0] + 2, coord[1]),
        (coord[0] - 2, coord[1]),
        (coord[0] + 1, coord[1] + 1),
        (coord[0] + 1, coord[1] - 1),
        (coord[0] - 1, coord[1] + 1),
        (coord[0] - 1, coord[1] - 1)
    ]


def evolve(black_tiles, n):
    for _ in range(n):
        new_black_tiles = set()
        white_tiles = set()

        for coord in black_tiles:
            neighbors = get_neighbors(coord)
            white_neighbors = [n for n in neighbors if n not in black_tiles] 
            white_tiles.update(white_neighbors)

            black_cnt = 6 - len(white_neighbors)
            if black_cnt == 1 or black_cnt == 2:
                new_black_tiles.add(coord)
            
        for coord in white_tiles:
            neighbors = get_neighbors(coord)
            black_cnt = sum(n in black_tiles for n in neighbors)
            if black_cnt == 2:
                new_black_tiles.add(coord)

        black_tiles = new_black_tiles
    return black_tiles


start_time = time.time()
black_tiles = evolve(black_tiles, 100)
print(len(black_tiles), f"\t{time.time() - start_time}s")