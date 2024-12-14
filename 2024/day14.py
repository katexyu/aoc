from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3

"""

with open('day14.txt', 'r') as f:
    actual = f.read()

def compute_safety(m, max_x=11, max_y=7):
    q1, q2, q3, q4 = 0,0,0,0
    for x in range(max_x//2):
        for y in range(max_y//2):
            q1 += m[(x,y)]
    for x in range(max_x//2+1, max_x):
        for y in range(max_y//2):
            q2 += m[(x,y)]
    for x in range(max_x//2+1, max_x):
        for y in range(max_y//2+1, max_y):
            q3 += m[(x,y)]

    for x in range(max_x//2):
        for y in range(max_y//2+1, max_y):
            q4 += m[(x,y)]
    return q1 * q2 * q3 * q4



def solve1(inp, max_x, max_y):
    inp = inp.strip().split('\n')
    robots = []
    for l in inp:
        l, r = l.strip("p=").split(" v=")
        p = [int(x) for x in l.split(",")]
        v = [int(x) for x in r.split(",")]
        robots.append((p,v))


    grid = dict()
    for x in range(max_x):
        for y in range(max_y):
            grid[(x,y)] = 0

    for p, v in robots:
        final_px = (p[0] + (v[0]*100)) % max_x
        final_py = (p[1] + (v[1]*100)) % max_y
        grid[(final_px, final_py)] += 1

    print_grid_map(grid)

    return compute_safety(grid, max_x, max_y)


def print_grid(mapping):
    """
    Given a mapping of coordinate to value, print it out
    """
    max_y = max(k[1] for k in mapping.keys()) + 1
    max_x = max(k[0] for k in mapping.keys()) + 1

    for y in range(max_y):
        row = ''
        for x in range(max_x):
            v = mapping[(x,y)]
            if v > 0:
                row += "x"
            else:
                row += "."
        print(row)


def analyze_grid(grid):
    pairs = combinations(grid.keys(), 2)
    counts = defaultdict(int)
    for p1, p2 in pairs:
        diff = abs(p2[0] - p1[0]) + abs(p2[1] - p1[0])
        counts[diff] += 1
    return counts


def solve2(inp, max_x, max_y):
    inp = inp.strip().split('\n')
    robots = []
    for l in inp:
        l, r = l.strip("p=").split(" v=")
        p = [int(x) for x in l.split(",")]
        v = [int(x) for x in r.split(",")]
        robots.append((p,v))

    for n in range(100000):
        grid = defaultdict(int)
        for p, v in robots:
            final_px = (p[0] + (v[0]*n)) % max_x
            final_py = (p[1] + (v[1]*n)) % max_y
            grid[(final_px, final_py)] += 1

        counts = analyze_grid(grid)

        # Check if stars are clustered close together
        if counts[0] + counts[1] + counts[2] > 500:
            print(f"After {n} seconds:")
            print(f"0 = {counts[0]}, 1 = {counts[1]}, 2 = {counts[2]}")
            print_grid(grid)


if __name__=='__main__':
    example_ans = solve1(example, max_x=11, max_y=7)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual, max_x=101, max_y=103)
    print(f'actual 1:\n {actual_ans}')

    actual_ans = solve2(actual, max_x=101, max_y=103)
    print(f'actual 2:\n {actual_ans}')

