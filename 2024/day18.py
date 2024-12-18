from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
"""

with open('day18.txt', 'r') as f:
    actual = f.read()


def solve1(inp, max_dim=6, max_steps=12):
    inp = inp.strip().split('\n')

    m = dict()

    for x in range(max_dim+1):
        for y in range(max_dim+1):
            m[(x,y)] = '.'

    i = 0
    while i < max_steps:
        x, y = [int(x) for x in inp[i].split(',')]
        m[(x,y)] = '#'
        i += 1

    ex, ey = max_dim, max_dim

    q = [(0,0,0)]
    visited = set()
    while q:
        x, y, dst = q.pop(0)
        if (x,y) == (ex,ey):
            return dst
        for nx, ny in valid_neighbors4(m, x, y):
            if m[(nx, ny)] == '#':
                continue
            if (nx, ny) not in visited:
                q.append((nx, ny, dst+1))
                visited.add((nx, ny))


def can_reach(m, ex, ey):
    q = [(0,0,0)]
    visited = set()
    while q:
        x, y, dst = q.pop(0)
        if (x,y) == (ex,ey):
            return True
        for nx, ny in valid_neighbors4(m, x, y):
            if m[(nx, ny)] == '#':
                continue
            if (nx, ny) not in visited:
                q.append((nx, ny, dst+1))
                visited.add((nx, ny))
    return False


def solve2(inp, max_dim=6):
    inp = inp.strip().split('\n')
    m = dict()

    for x in range(max_dim+1):
        for y in range(max_dim+1):
            m[(x,y)] = '.'

    for l in inp:
        x, y = [int(x) for x in l.split(',')]
        m[(x,y)] = '#'
        if not can_reach(m, max_dim, max_dim):
            return (x,y)


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual, max_dim=70, max_steps=1024)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')

    actual_ans = solve2(actual, max_dim=70)
    print(f'actual 2:\n {actual_ans}')
