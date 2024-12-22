from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
1
10
100
2024
"""

example2 = r"""
1
2
3
2024
"""

with open('day22.txt', 'r') as f:
    actual = f.read()

def mix(num, other):
    return num ^ other

def prune(num):
    return num % 16777216

def do_step(num):
    res = num * 64
    num = prune(mix(num, res))

    res = num // 32
    num = prune(mix(num, res))

    res = num * 2048
    return prune(mix(num, res))


def generate_secret_num(num, iterations=2000):
    for i in range(iterations):
        num = do_step(num)
    return num


def update_price_diffs(num, delta_sums):
    prices = [num%10]

    for i in range(2000):
        num = do_step(num)
        prices.append(num%10)

    diffs = []
    for n1, n2 in zip(prices[:-1], prices[1:]):
        diffs.append(n2-n1)

    seen_first_instance = set()
    for i in range(4, len(diffs)+1):
        last_4_diffs = tuple(diffs[i-4:i])
        if last_4_diffs not in seen_first_instance:
            seen_first_instance.add(last_4_diffs)
            delta_sums[last_4_diffs] += prices[i]


def solve1(inp):
    inp = inp.strip().split('\n')
    nums = [int(x) for x in inp]

    total = 0
    for n in nums:
        res = generate_secret_num(n)
        total += res

    return total


def num_bananas_for_deltas(deltas, all_first):
    return sum(a[deltas] for a in all_first)


def solve2(inp):
    inp = inp.strip().split('\n')
    nums = [int(x) for x in inp]

    all_first = []
    # all_possible = set()

    delta_sums = defaultdict(int)

    for n in nums:
        update_price_diffs(n, delta_sums)

    return max(delta_sums.values())

if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example2)
    print(f'example 2:\n {example_ans}')

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

