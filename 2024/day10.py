from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""

with open('day10.txt', 'r') as f:
    actual = f.read()


deltas = [(0,1), (1,0), (-1,0), (0,-1)]

def compute_score(m, x, y):
    score = 0

    visited = set()
    nxt = [(x,y)]
    reachable = set()
    while nxt:
        x, y = nxt.pop(0)
        if (x, y) in visited:
            continue
        v = m[(x,y)]

        visited.add((x,y))
        if v == 9:
            reachable.add((x,y))
            continue
        # check neighbors
        for dx, dy in deltas:
            nx, ny = x+dx, y+dy
            if (nx, ny) not in m:
                continue
            nv = m[(nx, ny)]
            if nv - v == 1:
                nxt.append((nx, ny))
    return len(reachable), reachable


def solve1(inp):
    inp = inp.strip().split('\n')
    th = []
    m = dict()
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            v = inp[y][x]
            if int(v) == 0:
                th.append((x,y))
            m[(x,y)] = int(v)

    return sum(compute_score(m, x, y)[0] for x, y in th)


cache = dict()

def compute_num_paths(m, sx, sy, ex, ey):
    if (sx, sy) == (ex, ey):
        return 1
    if (sx, sy, ex, ey) in cache:
        return cache[(sx, sy, ex, ey)]
    nxt = []
    v = m[(sx,sy)]
    for dx, dy in deltas:
        nx, ny = sx+dx, sy+dy
        if (nx, ny) not in m:
            continue
        nv = m[(nx, ny)]
        if nv - v == 1:
            nxt.append((nx, ny))
    
    ans = sum(compute_num_paths(m, nx, ny, ex, ey) for nx, ny in nxt)
    cache[(sx, sy, ex, ey)] = ans
    return ans


def compute_rating(m, x, y):
    _, reachable = compute_score(m, x, y)

    s = 0
    for ex, ey in reachable:
        s += compute_num_paths(m, x, y, ex, ey)

    return s


def solve2(inp):
    inp = inp.strip().split('\n')

    th = []
    m = dict()
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            v = inp[y][x]
            if int(v) == 0:
                th.append((x,y))
            m[(x,y)] = int(v)

    return sum(compute_rating(m, x, y) for x, y in th)


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

