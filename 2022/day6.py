from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = """
mjqjpqmgbljsphdztnvjfqwrcgsmlb
"""


def solve(inp, target):
    inp = list(inp.strip())
    charset = set()
    chars = []
    
    for i, c in enumerate(inp):
        if c in charset:
            c0 = None
            while c0 != c:
                c0 = chars.pop(0)
                charset.remove(c0)
        chars.append(c)
        charset.add(c)

        if len(charset) == target:
            return i + 1


if __name__=='__main__':
    example_ans = solve(example, 14)
    print(f'example:\n {example_ans}')

    actual_ans = solve(parse_lines('day6.txt')[0], 14)
    print(f'actual:\n {actual_ans}')

