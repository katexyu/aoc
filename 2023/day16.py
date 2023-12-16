from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
"""

with open('day16.txt') as f:
    actual = f.read()

deltas = {
    'r': [1, 0],
    'l': [-1, 0],
    'd': [0, 1],
    'u': [0, -1],
}

def solve1(inp):
    return compute_num_energized(((0, 0), 'r'), inp)

def compute_num_energized(start, inp):
    inp = inp.strip().split('\n')
    grid = to_grid_map(inp)
    energized = dict()
    seen = set()
    beams = [start]
    while beams:
        pos, d = beams.pop()
        val = grid[pos]
        energized[pos] = '#'
        if val in '#.':
            grid[pos] = '#'
        n = new_beams(d, val, pos)
        for beam, new_d in n:
            if beam not in grid:
                continue
            if (beam, new_d) not in seen:
                beams.append((beam, new_d))
                seen.add((beam, new_d))

    return len(energized) 


front_slash = {
    'u': (1, 0, 'r'),
    'd': (-1, 0, 'l'),
    'l': (0, 1, 'd'),
    'r': (0, -1, 'u'),
}

back_slash = {
    'u': (-1, 0, 'l'),
    'd': (1, 0, 'r'),
    'l': (0, -1, 'u'),
    'r': (0, 1, 'd'),
}

def new_beams(d, val, pos):
    if val in '#.':
        dx, dy = deltas[d]
        return [((pos[0]+dx, pos[1]+dy), d)]
    if val == '/':
        dx, dy, nd  = front_slash[d]
        return [((pos[0]+dx, pos[1]+dy), nd)]
    elif val == '\\':
        dx, dy, nd = back_slash[d]
        return [((pos[0]+dx, pos[1]+dy), nd)]
    if d in ('d', 'u'):
        if val == '|':
            dx, dy = deltas[d]
            return [((pos[0]+dx, pos[1]+dy), d)]
        if val == '-':
            return [((pos[0]-1, pos[1]), 'l'), ((pos[0]+1, pos[1]), 'r')]
        raise "should not get here d, u"
    if d in ('l', 'r'):
        if val == '-':
            dx, dy = deltas[d]
            return [((pos[0]+dx, pos[1]+dy), d)]
        if val == '|':
            return [((pos[0], pos[1]-1), 'u'), ((pos[0], pos[1]+1), 'd')]
        raise "should not get here l, r"
 

def solve2(inp):
    inp_arr = inp.strip().split('\n')
    max_y = len(inp_arr)-1
    max_x = len(inp_arr[0])-1
    candidates = []
    for x in range(max_x):
        candidates.append(((x, 0), 'd'))
        candidates.append(((x, max_y), 'u'))
    for y in range(max_y):
        candidates.append(((0, y), 'r'))
        candidates.append(((max_x, y), 'l'))

    best = 0
    for c in candidates:
        best = max(best, compute_num_energized(c, inp))
    return best


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')
    assert example_ans == 46

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')
    assert example_ans == 51

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

