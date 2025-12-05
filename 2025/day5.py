from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

with open('day5.txt', 'r') as f:
    actual = f.read()


def solve1(inp):
    inp = inp.strip().split('\n\n')
    r = inp[0].split('\n')
    ids = [int(i) for i in inp[1].split('\n')]
    ranges = []
    for l in r:
        x, y = l.split('-')
        ranges.append((int(x), int(y)))
    ans = 0
    for i in ids:
        for l, r in ranges:
            if i >= l and i <= r:
                ans += 1
                break
    return ans 


def solve2(inp):
    inp = inp.strip().split('\n\n')
    r = inp[0].split('\n')
    ranges = []
    for l in r:
        x, y = l.split('-')
        ranges.append((int(x), int(y)))
    ranges.sort()
    merged = merge_ranges(ranges)
    ans = 0
    for l, r in merged:
        ans += (r - l) + 1
    return ans


def merge_ranges(ranges):
    new_ranges = []
    cur = ranges[0]
    idx = 1
    while idx < len(ranges):
        nxt = ranges[idx]
        if nxt[0] > cur[1]:
            new_ranges.append(cur)
            cur = nxt
        else:
            cur = (cur[0], max(cur[1], nxt[1]))
        idx += 1
    new_ranges.append(cur)
    return new_ranges


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

