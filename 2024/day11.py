from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
125 17
"""

actual = r"""
2 72 8949 0 981038 86311 246 7636740
"""


def compute_counts(stone_counts, steps):
    for i in range(steps):
        new = defaultdict(int) 
        for s, prev in stone_counts.items():
            if s == 0:
                new[1] += prev
            elif len(str(s)) % 2 == 0:
                strs = str(s)
                mid = len(strs)//2
                lh, rh = strs[:mid], strs[mid:]
                new[int(lh)] += prev
                new[int(rh)] += prev
            else:
                new[s*2024] += prev
        stone_counts = new
    return sum(stone_counts.values())


def solve1(inp):
    inp = inp.strip().split('\n')
    stones = [int(x) for x in inp[0].split()]
    counts = Counter(stones)
    return compute_counts(counts, 25)


def solve2(inp):
    inp = inp.strip().split('\n')
    stones = [int(x) for x in inp[0].split()]
    counts = Counter(stones)
    return compute_counts(counts, 75)


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

