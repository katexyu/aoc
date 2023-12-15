from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = """
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
"""

with open('day15.txt') as f:
    actual = f.read()


def solve1(inp):
    inp = inp.strip().strip('\n').split(',')
    total = 0
    for item in inp:
        total += get_hash(item) 
    return total


def get_hash(item):
    val = 0
    for c in item:
        val += ord(c)
        val *= 17
        val = val % 256
    return val


def solve2(inp):
    inp = inp.strip().strip('\n').split(',')
    hm = [[] for i in range(256)]
    seen = set()
    for item in inp:
        if '=' in item:
            parts = item.split("=")
            focal = int(parts[1])
            label = parts[0]
            box = get_hash(label)
            arr = hm[box]
            done = False
            for i, elem in enumerate(arr):
                if elem[0] == label:
                    elem[1] = focal
                    done = True
                    break
            if not done:
                arr.append([label, focal])
                seen.add(label)
        elif '-' in item:
            label = item[:len(item)-1]
            if label in seen:
                box = get_hash(label)
                seen.remove(label)
                arr = hm[box]
                to_remove = None
                for i, elem in enumerate(arr):
                    if elem[0] == label:
                        to_remove = elem
                        break
                arr.remove(to_remove)
    total = 0
    for i in range(256):
        box = hm[i]
        for j, elem in enumerate(box):
            val = (i+1) * (j+1) * elem[1]
            total += val
    return total


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')
    assert example_ans == 1320
    
    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')
    assert example_ans == 145

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

