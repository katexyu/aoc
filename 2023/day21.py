from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""

with open('day21.txt', 'r') as f:
    actual = f.read()


def solve1(inp, num_steps):
    inp = inp.strip().split('\n')
    grid = to_grid_map(inp)

    start = (-1, -1)
    for c, v in grid.items():
        if v == 'S':
            start = c
            break

    layer = [start]
    for i in range(num_steps):
        nxt = set()
        for x, y in layer:
            for xx, yy in valid_neighbors(x,y, grid):
                nxt.add((xx,yy))
        layer = [c for c in nxt]
            
    return len(set(layer))


def valid_neighbors(x, y, grid):
    diffs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in diffs:
        xx, yy = dx+x, dy+y
        if (xx, yy) in grid and grid[(xx,yy)] != '#':
            yield (xx, yy)


def solve2(inp, num_steps):
    inp = inp.strip().split('\n')
    len_x = len(inp[0])
    len_y = len(inp)    

    grid = to_grid_map(inp)

    start = (-1, -1)
    for c, v in grid.items():
        if v == 'S':
            start = c
            break

    layer = [start]
    layer_map = { start: [start] }

    offset = len_x // 2 - 1

    
    steps = []
    for i in range(num_steps):
        nxt = set()
        nxt_map = defaultdict(set)
        for base, coords in layer_map.items():
            x, y = base
            for xx, yy, inx, iny in valid_neighbors2(x,y, grid, len_x, len_y):
                nxt.add((inx, iny))
                translate_to_output(layer_map, nxt_map, xx, yy, inx, iny, x, y) 
            
        layer = [c for c in nxt]
        layer_map = nxt_map
        if i % len_x == offset:
            steps.append(sum(len(s) for s in layer_map.values())) 


    idx = [offset + i*len_x for i, _ in enumerate(steps)]
    for i, s in zip(idx, steps):
        # To get the actual answer I just plugged in the values into wolfram alpha 
        print(i, s)
    
    print(diffs(steps))
    print(diffs(diffs(steps)))
            
    return sum(len(s) for s in layer_map.values())


def translate_to_output(layer_map, nxt_map, xx, yy, inx, iny, x, y):
    translated_coords = layer_map[(x, y)]
    for tx, ty in translated_coords:
        # compute diff from base input
        dx, dy = tx - x, ty - y
        nxt_map[(inx, iny)].add((xx+ dx, yy + dy))
    return nxt_map


def valid_neighbors2(x, y, grid, len_x, len_y):
    diffs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for dx, dy in diffs:
        xx, yy = (dx+x), (dy+y)
        nx, ny = xx % len_x, yy % len_y
        if grid[(nx, ny)] != '#':
            yield (xx, yy, nx, ny)


def diffs(t):
    return [j-i for i, j in zip(t[:-1], t[1:])]


if __name__=='__main__':
    example_ans = solve1(example, 6)
    print(f'example 1:\n {example_ans}')
    assert example_ans == 16

    actual_ans = solve1(actual, 64)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example, 5+11*10)
    print(f'example 2:\n {example_ans}')

    actual_ans = solve2(actual, 65+131*5) 
    print(f'actual 2:\n {actual_ans}')

