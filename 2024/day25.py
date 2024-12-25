from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
"""

with open('day25.txt', 'r') as f:
    actual = f.read()


def matches(key, lock):
    for k, l in zip(key, lock):
        if k > l:
            return False
    return True


def solve1(inp):
    inp = inp.strip().split('\n\n')

    keys = []
    locks = []
    for i in inp:
        s = to_grid_map(i.split('\n'))
        if i[0] == '#':
            heights = []
            for x in range(5):
                for y in range(7):
                    if s[(x,y)] == '.':
                        heights.append(y-1)
                        break
            keys.append(heights)
        elif i[0] == '.':
            heights = []
            for x in range(5):
                for y in range(7):
                    if s[(x,y)] == '#':
                        heights.append(y-1)
                        break
            locks.append(heights)

    cnt = 0
    for k in keys:
        for l in locks:
            if matches(k, l):
                cnt += 1

    return cnt


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

