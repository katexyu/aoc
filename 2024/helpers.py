def to_grid_map(inp):
    """
    Converts a list of input lines to a dict of coordinates to values.
    """
    mapping = dict()
    for j, line in enumerate(inp):
        for i, c in enumerate(line):
            mapping[(i, j)] = c
    return mapping

def to_int_grid_map(inp):
    """
    Converts a list of input lines to a dict of coordinates to values cast to int.
    """
    mapping = dict()
    for j, line in enumerate(inp):
        for i, c in enumerate(line):
            mapping[(i, j)] = int(c)
    return mapping


def print_grid_map(mapping):
    """
    Given a mapping of coordinate to value, print it out
    """
    max_y = max(k[1] for k in mapping.keys()) + 1
    max_x = max(k[0] for k in mapping.keys()) + 1

    for y in range(max_y):
        print(''.join(mapping[(x, y)] for x in range(max_x)))


def print_sparse_grid_map(mapping):
    """
    Given a sparse mapping of coordinate to value, print it out
    """
    min_y = min(k[0] for k in mapping.keys())
    max_y = max(k[1] for k in mapping.keys()) + 1
    min_x = min(k[0] for k in mapping.keys())
    max_x = max(k[0] for k in mapping.keys()) + 1

    for y in range(min_y, max_y):
        print(''.join(mapping.get((x, y), ' ') for x in range(min_x, max_x)))


def print_grid(g):
    for l in g:
        print(l)


DELTAS4 = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1],
]


def valid_neighbors4(m, x, y):
    for dx, dy in DELTAS4:
        if (x+dx, y+dy) in m:
            yield (x+dx, y+dy)


def valid_neighbors8(m, x, y):
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            if (x+dx, y+dy) in m:
                yield (x+dx, y+dy)

