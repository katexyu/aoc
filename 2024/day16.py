from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""

example2 = r"""
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
"""

with open('day16.txt', 'r') as f:
    actual = f.read()


dirs = ['>', 'v', '<', '^']


def solve1(inp):
    inp = inp.strip().split('\n')
    m = to_grid_map(inp)
    sx, sy = find_starting_coords(m, 'S')
    ex, ey = find_starting_coords(m, 'E')

    visited = set()
    visited.add(('>', sx, sy))
    q = [(0, ('>', sx, sy))]

    while q:
        cost, pos = heappop(q)
        f, x, y = pos
        if (x, y) == (ex, ey):
            return cost

        dx, dy = DIRECTIONS[f]
        nx, ny = x+dx, y+dy

        v = m[(nx, ny)]
        if v != '#' and (f, nx, ny) not in visited:
            heappush(q, (cost+1, (f, nx, ny)))
            visited.add((f, nx, ny))

        # turn clockwise or counterclockwise
        di = dirs.index(f)

        for offset in [1, -1]:
            nf = dirs[(di + offset) % 4]
            if (nf, x, y) not in visited:
                heappush(q, (cost+1000, (nf, x, y)))
                visited.add((nf, x, y))

import sys

def solve2(inp):
    inp = inp.strip().split('\n')
    m = to_grid_map(inp)
    sx, sy = find_starting_coords(m, 'S')
    ex, ey = find_starting_coords(m, 'E')

    visited = set()
    visited.add(('>', sx, sy))
    q = [(0, ('>', sx, sy))]

    costs = dict()
    costs[('>', sx, sy)] = 0
    parents = defaultdict(list)

    ends = []
    best_cost = sys.maxsize
    while q:
        cost, pos = heappop(q)
        f, x, y = pos
        if (x, y) == (ex, ey):
            if cost > best_cost:
                break
            best_cost = cost
            ends.append((f, x, y))
            continue

        dx, dy = DIRECTIONS[f]
        nx, ny = x+dx, y+dy

        v = m[(nx, ny)]
        if v != '#':
            if (f, nx, ny) not in visited:
                heappush(q, (cost+1, (f, nx, ny)))
                parents[(f, nx, ny)].append((f, x, y))
                costs[(f, nx, ny)] = cost+1
                visited.add((f, nx, ny))
            elif costs[(f, nx, ny)] == cost+1:
                parents[(f, nx, ny)].append((f, x, y))

        # turn clockwise or counterclockwise
        di = dirs.index(f)
        for offset in [1, -1]:
            nf = dirs[(di + offset) % 4]
            if (nf, x, y) not in visited:
                heappush(q, (cost+1000, (nf, x, y)))
                visited.add((nf, x, y))
                parents[(nf, x, y)].append((f, x, y))
                costs[(nf, x, y)] = cost+1000
            elif costs[(nf, x, y)] == cost+1000:
                parents[(nf, x, y)].append((f, x, y))

    seats = dict()
    for f, x, y in ends:
        q = [(f, x, y)]
        seen = set()
        while q:
            f, x, y = q.pop(0)
            seats[(x, y)] = 'x'
            for ff, xx, yy in parents[(f, x, y)]:
                if (ff, xx, yy) not in seen:
                    q.append((ff, xx, yy))
                    seen.add((ff, xx, yy))

    return len(seats)


if __name__=='__main__':
    example_ans = solve1(example2)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

