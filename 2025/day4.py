from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

with open('day4.txt', 'r') as f:
    actual = f.read()


def solve1(inp):
    inp = inp.strip().split('\n')
    g = to_grid_map(inp)
    ans = 0
    for x, y in g:
        if g[(x,y)] == '.':
            continue
        c = sum(g[(xx,yy)] == '@' for xx, yy in valid_neighbors8(g, x, y))
        if c < 4:
            ans += 1
    return ans


def solve2(inp):
    inp = inp.strip().split('\n')
    g = to_grid_map(inp)
    ans = 0
    while True:
        rolls = set()
        for x, y in g:
            if g[(x,y)] == '.':
                continue
            c = sum(g[(xx,yy)] == '@' for xx, yy in valid_neighbors8(g, x, y))
            if c < 4:
                rolls.add((x,y))
        if len(rolls) == 0:
            break
        ans += len(rolls)
        for x,y in rolls:
            g[(x,y)] = '.'
        rolls = set()
    return ans


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

