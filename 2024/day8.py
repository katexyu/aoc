from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""

actual = r"""
..................................................
.......................x.................N........
..................x...............................
............x................w.........D.....a....
.........6...........i.........D..............u...
........6.......................q................u
........................i....u.w...........a.2....
....................................u.12..........
..................................f.....D....0a...
.............................Q..D......c..N..f....
..............w..................................f
.........Y.............i...............q..a.......
............................2..........O...q......
.....6..G.....................R...................
..............................N...................
.U.......G................i...J.............0.....
Y..U................F......N......................
.T......Y.............H.................2.P.......
...............T.........F.8........H.............
..T...............F...............l..............0
................G.....e........18...Q.............
.......................F....................O.....
.....Y....U...................l....g..............
U........9........................................
.....................e..q..Q......................
.......X........e......................1Q..O......
............T.................gx......0..........t
...................l......9........P..............
.y...........9...............r.5.......j.P........
..z.........d.........g......................H....
................6.......r...........P.........O...
.A........................8...r...................
.4....W...Z...........9..................s..j.....
.z..W.........y...........og......................
..3.z.....R.....L....o.........................H..
.......yZ.c..W.......p..............s.............
............1..3.........L.........S..............
.......Z..4............o.....S...........5.......s
............c........l......7.....................
.....4....p.........I.......t...........5........j
.......c....h...........C..d......................
......n..........C......L............E....j.......
.X.W..........n....R......d.I...............5.....
3.........Cn.........L...r.............e..........
...A...........Z.p.....I..S.............s.......J.
....................7.............S...X....J......
........X.............o...........................
........A....h.R.....7.t...I......................
..A.4z......y.p..h.7...........Et.................
................h........3..E..d.8................
"""
from itertools import combinations


def solve1(inp):
    inp = inp.strip().split('\n')
    m = to_grid_map(inp)

    frequencies = defaultdict(list)
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            freq = m[(x,y)]
            if freq != '.':
                frequencies[freq].append((x,y))

    antinodes = set()

    for freqs, coords in frequencies.items():
        pairs = combinations(coords, 2)
        for l, r in pairs:
            dy, dx = r[1] - l[1], r[0] - l[0]
            x1, y1 = r[0] + dx, r[1] + dy
            x2, y2 = l[0] - dx, l[1] - dy

            if 0 <= x1 < len(inp[0]) and 0 <= y1 < len(inp):
                antinodes.add((x1, y1))
            if 0 <= x2 < len(inp[0]) and 0 <= y2 < len(inp):
                antinodes.add((x2, y2))

    return len(antinodes) 


import math


def solve2(inp):
    inp = inp.strip().split('\n')
    m = to_grid_map(inp)

    frequencies = defaultdict(list)
    for y in range(len(inp)):
        for x in range(len(inp[0])):
            freq = m[(x,y)]
            if freq != '.':
                frequencies[freq].append((x,y))

    antinodes = set()

    for freqs, coords in frequencies.items():
        pairs = combinations(coords, 2)
        for l, r in pairs:
            dy, dx = r[1] - l[1], r[0] - l[0]
            antinodes.add(l)
            antinodes.add(r)

            f = math.gcd(dy, dx)
            dy /= f
            dx /= f

            x1, y1 = r[0] + dx, r[1] + dy
            x2, y2 = l[0] - dx, l[1] - dy

            while 0 <= x1 < len(inp[0]) and 0 <= y1 < len(inp):
                antinodes.add((x1, y1))
                x1 += dx
                y1 += dy
            while 0 <= x2 < len(inp[0]) and 0 <= y2 < len(inp):
                antinodes.add((x2, y2))
                x2 -= dx
                y2 -= dy

    return len(antinodes) 


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

