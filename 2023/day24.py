from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""

with open('day24.txt', 'r') as f:
    actual = f.read()


def solve1(inp, lower=200000000000000, upper=400000000000000):
    inp = inp.strip().split('\n')
    hailstones = []
    for line in inp:
        l, r = line.split(' @ ')
        x,y,z = (int(i) for i in l.split(', '))
        dx,dy,dz = (int(i) for i in r.split(', '))

        xend,yend = get_end_in_range(lower, upper, x, y, dx, dy)
        slope, c = get_2d_equation(x, y, xend, yend, dx, dy)
        hailstones.append((x,y,xend,yend,dx,dy,slope,c))

    count = 0
    for h1, h2 in combinations(hailstones, 2):
        x1,y1,x1end,y1end,dx1,dy1,s1,c1 = h1
        x2,y2,x2end,y2end,dx2,dy2,s2,c2 = h2

        if s1 == s2:
            if c1 == c2:
                count += 1
            continue
        x = (c2 - c1) / (s1 - s2)
        y = (s1 * x) + c1
        if not (lower <= x <= upper and lower <= y <= upper):
            continue
        if is_between_bounds(x,y,x1,y1,x1end,y1end,dx1,dy1) and is_between_bounds(x,y,x2,y2,x2end,y2end,dx2,dy2):
            count += 1
    return count


def is_between_bounds(x, y, xs, ys, xe, ye, dx, dy):
    num_steps = (xe - xs) / dx
    
    nx = (x - xs) / dx
    between = 0 <= nx <= num_steps
    return between


def get_2d_equation(x1, y1, x2, y2, dx, dy):
    slope = dy / dx
    c = y2 - x2 * slope
    return slope, c    


def get_end_in_range(lower, upper, x, y, dx, dy):
    xend, yend = x, y
    xbound = upper if dx > 0 else lower
    ybound = upper if dy > 0 else lower

    nx = (xbound - x) / dx
    ny = (ybound - y) / dy

    num_steps = min(nx, ny)
    xend, yend = x + num_steps * dx, y + num_steps * dy
    return xend, yend


from z3 import Int, Ints, Solver


def solve2(inp):
    inp = inp.strip().split('\n')
    hailstones = []
    for line in inp:
        l, r = line.split(' @ ')
        x,y,z = (int(i) for i in l.split(', '))
        dx,dy,dz = (int(i) for i in r.split(', '))
        hailstones.append((x,y,z,dx,dy,dz))

    s = Solver()
    a,b,c,da,db,dc = Ints('a b c da db dc')

    for i, h in enumerate(hailstones):
        x,y,z,dx,dy,dz = h
        t = Int(f"t{i}")
        s.add(a + da * t == x + dx * t)  
        s.add(b + db * t == y + dy * t)  
        s.add(c + dc * t == z + dz * t)  

    s.check()
    m = s.model()
    return m[a].as_long() + m[b].as_long() + m[c].as_long()


if __name__=='__main__':
    example_ans = solve1(example, lower=7, upper=27)
    print(f'example 1:\n {example_ans}')
    assert example_ans == 2

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')
    assert example_ans == 47

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

