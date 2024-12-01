def to_grid_map(inp):
    """
    Converts a list of input lines to a dict of coordinates to values.
    """
    mapping = dict()
    for j, line in enumerate(inp):
        for i, c in enumerate(line):
            mapping[(i, j)] = c
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

