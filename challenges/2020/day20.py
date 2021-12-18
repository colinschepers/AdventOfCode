
inputs = open('./data/day20.txt').read().split('\n\n')
 

def get_edges(data):
    return [
        to_decimal(data[0]), 
        to_decimal(row[-1] for row in data),
        to_decimal(data[-1][::-1]),
        to_decimal(row[0] for row in data[::-1]),
    ]

def get_inv_edges(data):
    return [
        to_decimal(data[0][::-1]), 
        to_decimal(row[-1] for row in data[::-1]),
        to_decimal(data[-1]),
        to_decimal(row[0] for row in data),
    ]

def flipped(data):
    return [x[::-1] for x in data]

def rotated(data, n):
    for i in range(n):
        data = list(zip(*data[::-1]))
    return data

def to_decimal(binary):
    bin_str = ''.join(str(x) for x in binary)
    return int(bin_str, 2)


class Tile():
    def __init__(self, id, data):
        self.id = id
        self.data = data
        self.edges = get_edges(data) + get_edges(flipped(data))
        self.inv_edges = get_inv_edges(data) + get_inv_edges(flipped(data))
        self.rotation = 0
        self.is_flipped = False

    def h_fit(self, tile):
        return tile.east() == self.inv_west()

    def v_fit(self, tile):
        return tile.south() == self.inv_north()

    def rotate(self, n=1):
        self.rotation += n
        self.rotation %= 4

    def flip(self):
        self.is_flipped = not self.is_flipped

    def north(self):
        return self.edges[((0 - self.rotation) % 4) + (4 if self.is_flipped else 0)]

    def east(self):
        return self.edges[((1 - self.rotation) % 4) + (4 if self.is_flipped else 0)]

    def south(self):
        return self.edges[((2 - self.rotation) % 4) + (4 if self.is_flipped else 0)]

    def west(self):
        return self.edges[((3 - self.rotation) % 4) + (4 if self.is_flipped else 0)]

    def inv_north(self):
        return self.inv_edges[((0 - self.rotation) % 4) + (4 if self.is_flipped else 0)]

    def inv_east(self):
        return self.inv_edges[((1 - self.rotation) % 4) + (4 if self.is_flipped else 0)]

    def inv_south(self):
        return self.inv_edges[((2 - self.rotation) % 4) + (4 if self.is_flipped else 0)]

    def inv_west(self):
        return self.inv_edges[((3 - self.rotation) % 4) + (4 if self.is_flipped else 0)]

    def __str__(self):
        result = f'Tile {self.id}:\n'
        data = flipped(self.data) if self.is_flipped else self.data
        data = rotated(data, self.rotation)
        for row in data:
            result += ''.join(['#' if p else '.' for p in row]) + '\n'
        return result
    
    def __repr__(self):
        return f'Tile{self.id}[r={self.rotation}{(",f" if self.is_flipped else ",n")}]'


tiles = []
for input in inputs:
    lines = input.split('\n')
    id = int(lines.pop(0).split(' ')[1].strip(':'))
    pixels = [[int(c == '#') for c in line] for line in lines if line]
    tiles.append(Tile(id, pixels))


def print_grid(grid):
    for row in grid:
        for tile in row:
            if not tile:
                print('.' * 15, end=' ')
            else:
                print(tile.__repr__(), end=' ')
        print('')
    print()

def print_grid_full(grid):
    for row in grid:
        for r in range(10):
            for tile in row:
                if not tile:
                    print('.' * 10, end=' ')
                else:
                    lines = str(tile).split('\n')
                    print(lines[r+1], end=' ')
            print('')
        print('')
    print()

def solve(grid, row=0, col=0, visited=set()):
    # print(f"row = {row} \t col = {col}")
    # print_grid(grid)
    # print_grid_full(grid)
    
    if row >= len(grid):
        return grid
    if col >= len(grid[0]):
        return solve(grid, row + 1, 0, visited)

    for tile in tiles:
        if tile.id in visited:
            continue
        for _ in range(2):
            for _ in range(4):
                if (col == 0 or tile.h_fit(grid[row][col-1]) and \
                   (row == 0 or tile.v_fit(grid[row-1][col]))):

                    grid[row][col] = tile
                    visited.add(tile.id)
                    solution = solve(grid, row, col + 1, visited)

                    if solution:
                        return solution

                    visited.remove(tile.id)
                    grid[row][col] = None

                tile.rotate(1)
            tile.flip()


size = int(len(tiles) ** 0.5)
grid = [[None for _ in range(size)] for _ in range(size)]
solution = solve(grid)

print(solution[0][0].id * solution[0][-1].id * solution[-1][0].id * solution[-1][-1].id)


def create_image(grid):
    image = ''
    for row in grid:
        for r in range(1, 9):
            for tile in row:
                lines = str(tile).split('\n')
                image += lines[r+1][1:-1]
            image += '\n'
    return image.strip()

def rotate_img(image):
    lines = image.split('\n')
    lines = list(''.join(x) for x in zip(*lines[::-1]))
    return '\n'.join(lines)

def flip_img(image):
    lines = image.split('\n')
    lines = [''.join(x[::-1]) for x in lines]
    return '\n'.join(lines)

def find_sea_monsters(image):
    sm_width = 20
    sm_height = 3
    sea_monster ="""
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
"""

    img_size = len(image.split('\n'))
    input = image.replace('\n', '')

    mask = []
    for line_nr, line in enumerate(sea_monster.strip('\n').split('\n')):
        mask += [line_nr * img_size + i for i, c in enumerate(line) if c == '#']


    for row in range(img_size - sm_height):
        for col in range(img_size - sm_width):
            idx = row * img_size + col
            for m in mask:
                if input[idx + m] != '#':
                    break
            else:
                yield idx


image = create_image(solution)

for _ in range(2):
    for _ in range(4):
        # print(image)

        sea_monsters = list(find_sea_monsters(image))

        if sea_monsters:
            solution = sum(c == '#' for c in image) - 15 * len(sea_monsters)
            print(solution)

        image = rotate_img(image)
    image = flip_img(image)