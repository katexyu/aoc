from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import lru_cache


example = r"""
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
"""


with open('day19.txt', 'r') as f:
    actual = f.read()


cache = dict()
def possible(patterns, design):
    if design in cache:
        return cache[design]
    for p in patterns:
        if p == design:
            cache[design] = True
            return True
        if design.startswith(p):
            if possible(patterns, design[len(p):]):
                cache[design] = True
                return True
    cache[design] = False
    return False


def solve1(inp):
    inp = inp.strip().split('\n\n')
    patterns = inp[0].split(', ')

    designs = inp[1].split('\n')

    total = 0
    for d in designs:
        if possible(patterns, d):
            total += 1
    return total


def solve2(inp):
    inp = inp.strip().split('\n\n')
    patterns = inp[0].split(', ')
    designs = inp[1].split('\n')

    @lru_cache
    def possible_cnt(d):
        if d == '':
            return 1
        total = 0
        for p in patterns:
            if d.startswith(p):
                total += possible_cnt(d[len(p):])
        return total 

    total = 0
    for d in designs:
        total += possible_cnt(d)
    return total


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

