from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

with open('day1.txt', 'r') as f:
    actual = f.read()


def solve1(inp):
    inp = inp.strip().split('\n')

    pos = 50
    cnt = 0
    for l in inp:
        d = l[:1]
        c = int(l[1:])
        mul = 1 if d == 'R' else -1
        pos = (pos + (mul*c)) % 100
        if pos == 0:
            cnt += 1
    return cnt 


def solve2(inp):
    inp = inp.strip().split('\n')
    pos = 50
    cnt = 0
    for l in inp:
        d = l[:1]
        c = int(l[1:])
        mul = 1 if d == 'R' else -1
        cnt += c // 100
        remainder = c % 100

        new_pos = (pos + (mul*remainder)) % 100
        if pos != 0:
            if new_pos == 0:
                cnt += 1
            elif new_pos < pos and d == 'R':
                cnt += 1
            elif new_pos > pos and d == 'L':
                cnt += 1

        pos = new_pos
    return cnt 


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

