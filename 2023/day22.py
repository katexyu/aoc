from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
"""

with open('day22.txt', 'r') as f:
    actual = f.read()

from dataclasses import dataclass


@dataclass
class Brick:
    _id: int
    minx: int
    maxx: int
    miny: int
    maxy: int
    minz: int
    maxz: int
    supported: bool = False

    def is_supported_by(self, brick):
        if self.minz != brick.maxz + 1:
            return False
        if self.minx > brick.maxx or self.maxx < brick.minx:
            return False
        if self.miny > brick.maxy or self.maxy < brick.miny:
            return False
        return True


def solve1(inp):
    inp = inp.strip().split('\n')
    bricks = []
    for i, line in enumerate(inp):
        l, r = line.split('~')
        l = [int(x) for x in l.split(',')]
        r = [int(x) for x in r.split(',')]
        bricks.append(Brick(i, l[0], r[0], l[1], r[1], l[2], r[2]))

    supported_by = defaultdict(list)
    bricks.sort(key=lambda b: b.maxz)

    while True:
        for i, b in enumerate(bricks):
            if b.supported:
                continue
            if b.minz == 1:
                b.supported = True
                continue
            done = False
            for bb in bricks[:i]:
                if b.is_supported_by(bb):
                    b.supported = True
                    supported_by[b._id].append(bb)
                    done = True
            if done:
                continue
            b.minz -= 1
            b.maxz -= 1
            break
        if all(b.supported for b in bricks):
            break

     
    # z is the direction bricks are falling
    only_supporters = set()
    for k, v in supported_by.items():
        if len(v) == 1:
            only_supporters.add(v[0]._id)
    return len(bricks) - len(only_supporters)


def solve2(inp):
    inp = inp.strip().split('\n')
    bricks = []
    for i, line in enumerate(inp):
        l, r = line.split('~')
        l = [int(x) for x in l.split(',')]
        r = [int(x) for x in r.split(',')]
        bricks.append(Brick(i, l[0], r[0], l[1], r[1], l[2], r[2]))

    supported_by = defaultdict(list)
    bricks.sort(key=lambda b: b.maxz)

    supporting = defaultdict(list)
    while True:
        for i, b in enumerate(bricks):
            if b.supported:
                continue
            if b.minz == 1:
                b.supported = True
                continue
            done = False
            for bb in bricks[:i]:
                if b.is_supported_by(bb):
                    b.supported = True
                    supported_by[b._id].append(bb)
                    supporting[bb._id].append(b)
                    done = True
            if done:
                continue
            b.minz -= 1
            b.maxz -= 1
            break
        if all(b.supported for b in bricks):
            break

    total = 0
     
    for b in bricks:
        total += check_num_falls(b._id, supporting, supported_by)

    return total


def check_num_falls(brick_id, supporting, supported_by):
    falling = set()
    do_removal(brick_id, supporting, supported_by, falling)
    # Don't count itself
    return len(falling) - 1


def do_removal(brick_id, supporting, supported_by, falling):
    falling.add(brick_id)
    for s in supporting[brick_id]:
        if s._id in falling:
            continue
        b = supported_by[s._id]
        if all(x._id in falling for x in b):
            falling.add(s._id)
            do_removal(s._id, supporting, supported_by, falling)
    

if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')
    assert example_ans == 5

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')
    assert example_ans == 7

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

