from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
"""
example2 = r"""
2121212118-2121212124
"""

with open('day2.txt', 'r') as f:
    actual = f.read()


def solve1(inp):
    inp = inp.strip().split('\n')
    ids = inp[0].split(',')
    ans = 0
    for i in ids:
        l,r = [int(x) for x in i.split('-')]
        for x in range(l, r+1):
            if isinvalid(x):
                ans += x
    return ans


def isinvalid(num):
    n = str(num)
    if len(n) % 2 == 1:
        return False
    return n[:len(n)//2] == n[len(n)//2:]


def solve2(inp):
    inp = inp.strip().split('\n')
    ids = inp[0].split(',')
    ans = 0
    for i in ids:
        l,r = [int(x) for x in i.split('-')]
        for x in range(l, r+1):
            if isinvalid2(x):
                ans += x
    return ans


def isinvalid2(num):
    n = str(num)
    for e in range(1,len(n)//2+1, 1):
        if len(n) % e > 0:
            continue
        i,j = 0,e
        s = n[i:j]
        works = True
        while j <= len(n):
            if n[i:j] != s:
                works = False
                break
            i+= e
            j+= e
        if works:
            return True

    return False


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

