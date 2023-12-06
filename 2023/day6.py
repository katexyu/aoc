from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


def solve1(time, dist):
    ans = 1
    for t, d in zip(time, dist):
        ans *= num_ways(t, d)
    return ans


def num_ways(t, d):
    ways = 0
    for i in range(1, t):
        time_left = t - i
        if i * time_left > d:
            ways += 1
    return ways


def solve2(time, dist):
    ans = num_ways(time, dist)
    return ans


if __name__=='__main__':
    example_ans = solve1([7,15,30], [9, 40, 200])
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1([54, 94, 65, 92], [302, 1476, 1029, 1404])
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(71530, 940200)
    print(f'example 2:\n {example_ans}')

    actual_ans = solve2(54946592, 302147610291404)
    print(f'actual 2:\n {actual_ans}')

