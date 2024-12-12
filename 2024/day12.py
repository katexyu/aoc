from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""
example1 = r"""
AAAA
BBCD
BBCC
EEEC
"""


with open('day12.txt', 'r') as f:
    actual = f.read()


def compute_perimeter(coords):
    perimeter = 0
    for x, y in coords:
        for dx, dy in DELTAS4:
            xx, yy = x+dx, y+dy
            if (xx, yy) not in coords:
                perimeter +=1
    return perimeter


def find_groups(m):
    visited = set()
    ccs = []
    for c, v in m.items():
        if c in visited:
            continue
        x, y = c
        cc = find_connected_component(m, x, y)
        visited.update(cc)
        ccs.append((m[(x,y)], cc))
    return ccs


def find_connected_component(m, x, y):
    visited = set()
    v = m[(x,y)]
    q = [(x,y)]
    visited.add((x,y))
    while q:
        x, y = q.pop(0)
        for xx, yy in valid_neighbors4(m, x, y):
            if m[(xx, yy)] == v and (xx, yy) not in visited:
                q.append((xx, yy))
                visited.add((xx,yy))
    return visited


def solve1(inp):
    inp = inp.strip().split('\n')
    m = to_grid_map(inp)
    groups = find_groups(m)

    price = 0
    for v, coords in groups:
        area = len(coords)
        perimeter = compute_perimeter(coords)
        price += area * perimeter
    return price


def num_corners(coords):
    tot = 0
    for x, y in coords:
        for dx in [1, -1]:
            for dy in [1, -1]:
                # adjacent
                x1, y1 = x+dx, y
                x2, y2 = x, y+dy

                # diagonal
                x3, y3 = x+dx, y+dy

                # outer corner
                if (x1, y1) not in coords and (x2, y2) not in coords:
                    tot += 1

                # inner corner
                if (x1, y1) in coords and (x2, y2) in coords and (x3, y3) not in coords:
                    tot += 1

    return tot


def solve2(inp):
    inp = inp.strip().split('\n')
    m = to_grid_map(inp)
    groups = find_groups(m)

    price = 0
    for v, coords in groups:
        area = len(coords)
        sides = num_corners(coords)
        price += area * sides

    return price


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

