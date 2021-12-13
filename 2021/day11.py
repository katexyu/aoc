from helpers import foreach_neighbor, foreach_neighbors, foreach_grid, foreach_grids, parse_digits_grid, print_grid as print_data


def inc_grid(data, x, y):
    data[x][y] += 1


def set_zero(data, x, y):
    if data[x][y] == -1:
        data[x][y] = 0


def flash(data, x, y):
    if data[x][y] > 9:
        return recursive_flash(data, x, y)
    return 0


def solve(data):
    flashes = 0
    target_num = len(data) * len(data[0])
    for i in range(100):
        foreach_grid(data, inc_grid)
        flashes += foreach_grids(data, flash)
        foreach_grid(data, set_zero)
    return flashes


def solveb(data):
    target_num = len(data) * len(data[0])
    round = 0
    while True:
        round += 1
        foreach_grid(data, inc_grid)
        f = foreach_grids(data, flash)
        if f == target_num:
            return round
        foreach_grid(data, set_zero)
    return -1
        

def do_flash(data, x, y, i, j):
    if i == x and j == y:
        data[x][y] = -1
    elif data[i][j] != -1:
        data[i][j] += 1   


def do_recursive_flash(data, x, y, i, j):
    if data[i][j] > 9:
        return recursive_flash(data, i, j)
    return 0


def recursive_flash(data, x, y):
    if data[x][y] == -1:
        return 0
    foreach_neighbor(data, x, y, do_flash)
    return 1 + foreach_neighbors(data, x, y, do_recursive_flash)


def get_data(filename='day11.txt'):
    return parse_digits_grid(filename)


if __name__=='__main__':
    data = get_data()
    print(solve(data))
    print(solveb(get_data()))

