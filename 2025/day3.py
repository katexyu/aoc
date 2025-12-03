from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
987654321111111
811111111111119
234234234234278
818181911112111
"""

with open('day3.txt', 'r') as f:
    actual = f.read()


def solve1(inp):
    inp = inp.strip().split('\n')
    ans = 0
    for l in inp:
        nums = [int(x) for x in l]
        first = max(nums[:-1])
        idx = nums.index(first)
        second = max(nums[idx+1:])
        ans += first * 10 + second
    return ans 


def solve2(inp):
    inp = inp.strip().split('\n')
    ans = 0
    for l in inp:
        nums = [int(x) for x in l]
        best = largest(nums, 12) 
        ans += joltage(best)
    return ans


def joltage(batteries):
    s = 0
    for i, x in enumerate(reversed(batteries)):
        s += (10 ** i)*x
    return s


def largest(batteries, num):
    if num > len(batteries):
        return None
    if num == len(batteries):
        return batteries
    end_idx = len(batteries) - num + 1
    first = max(batteries[:end_idx])
    if num == 1:
        return [first]
    idx = batteries.index(first)
    rest = batteries[idx+1:]
    best = largest(rest, num-1)
    return [first] + best


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

