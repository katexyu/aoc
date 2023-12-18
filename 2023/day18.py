from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


with open('example18.txt') as f:
    example = f.read()

with open('day18.txt') as f:
    actual = f.read()


deltas = {
    'R': [1, 0],
    'L': [-1, 0],
    'D': [0, 1],
    'U': [0, -1],
}


def solve1(inp):
    inp = inp.strip().split('\n')
    x, y = 0, 0
    points = [(x, y)]
    num_points = 1
    for line in inp:
        parts = line.split()
        d, num, color = parts
        dist = int(num)
        dx, dy = deltas[d]
        x, y = x+dist*dx, y+dist*dy
        points.append((x,y))
        num_points += dist

    area = shoelace(points)
    # half the boundary points should be counted
    return area + num_points // 2 + 1


import numpy as np


def shoelace(points):
    """
    I blindly copied this from stackoverflow:
    https://stackoverflow.com/questions/41077185/fastest-way-to-shoelace-formula
    """
    x = []
    y = []
    for k in points:
        x.append(k[0])
        y.append(k[1])
    return 0.5 * np.abs(np.dot(x[:-1], y[1:]) + x[-1]*y[0] - np.dot(y[:-1], x[1:]) - y[-1]*x[0])


dirs = ['R', 'D', 'L', 'U']


def solve2(inp):
    inp = inp.strip().split('\n')
    x, y = 0, 0
    points = [(x, y)]
    num_points = 1
    for line in inp:
        parts = line.split()
        color = parts[2]
        dist = int(color[2:7], 16)
        d = dirs[int(color[7])]
        dx, dy = deltas[d]
        new_vals = []
        x, y = x+dist*dx, y+dist*dy
        points.append((x,y))
        num_points += dist

    area = shoelace(points)

    # half the boundary points should be counted
    return area + num_points // 2 + 1


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')
    assert example_ans == 62

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')
    assert example_ans == 952408144115

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

