def print_grid(g):
    for l in g:
        print(l)


def foreach_grid(grid, fn):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            fn(grid, i, j)


def foreach_grids(grid, fn):
    s = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            s += fn(grid, i, j)
    return s
 

def neighbors(grid, x, y):
    for i in range(max(0, x-1), min(len(grid), x+2)):
        for j in range(max(0, y-1), min(len(grid[0]), y+2)):
            yield (i, j)


def foreach_neighbor(grid, x, y, fn):
    for i in range(max(0, x-1), min(len(grid), x+2)):
        for j in range(max(0, y-1), min(len(grid[0]), y+2)):
            fn(grid, x, y, i, j) 


def foreach_neighbors(grid, x, y, fn):
    s = 0
    for i in range(max(0, x-1), min(len(grid), x+2)):
        for j in range(max(0, y-1), min(len(grid[0]), y+2)):
            s += fn(grid, x, y, i, j) 
    return s


def parse_digits_grid(filename):
    with open(filename, 'r') as f:
        return [[int(c) for c in line.strip()] for line in f]


def parse_csv_grid(filename):
    with open(filename, 'r') as f:
        return [[int(c) for c in line.strip().split(',')] for line in f]


def parse_lines(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f]

