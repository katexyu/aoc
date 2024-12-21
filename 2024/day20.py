from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import lru_cache


example = r"""
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
"""

with open('day20.txt', 'r') as f:
    actual = f.read()


def compute_diffs(m, sx, sy, ex, ey, can_cheat=False):
    q = deque([(sx, sy, 0, False)])
    visited = set()
    visited.add((sx, sy))
    cheats_visited = set()
    cheats = dict()

    dsts = get_dsts(m, sx, sy, ex, ey)

    while q:
        x, y, d, cheated = q.popleft()
        for nx, ny in valid_neighbors4(m, x, y):
            v = m[(nx, ny)]
            if v != '#':
                if not cheated and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    q.append((nx, ny, d+1, False))
        if not cheated:
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                nx, ny = dx+x, dy+y
                if (nx, ny) not in m:
                    continue
                enx, eny = 2*dx+x, 2*dy+y
                if (enx, eny) not in m:
                    continue
                if m[(nx, ny)] != '#':
                    continue
                if m[(enx, eny)] == '#':
                    continue
                if (x,y,enx,eny) in cheats_visited:
                    continue
                cheats[(x, y, enx, eny)] = shortest_path(dsts, x, y, enx, eny) - 2
                q.append((nx, ny, d+2, True))

    counter = defaultdict(int)

    for k, diff in cheats.items():
        counter[diff] += 1
    return counter


def solve1(inp):
    inp = inp.strip().split('\n')
    m = to_grid_map(inp)
    sx, sy = find_starting_coords(m, 'S')
    ex, ey = find_starting_coords(m, 'E')

    diffs = compute_diffs(m, sx, sy, ex, ey)
    total = 0
    for k in sorted(diffs.keys()):
        # print(f"diff={k} cnt={diffs[k]}")
        if k >= 100:
            total += diffs[k]
    return total


def get_dsts(m, sx, sy, ex, ey):
    dsts = dict()
    q = deque([(sx, sy, 0)])
    dsts[(sx, sy)] = 0

    while q:
        x, y, d = q.popleft()

        for nx, ny in valid_neighbors4(m, x, y):
            v = m[(nx, ny)]
            if v != '#' and (nx, ny) not in dsts:
                dsts[(nx, ny)] = d+1
                q.append((nx, ny, d+1))
    return dsts


def shortest_path(dsts, sx, sy, ex, ey):
    return dsts[(ex, ey)] - dsts[(sx, sy)]


def solve2(inp):
    inp = inp.strip().split('\n')
    m = to_grid_map(inp)
    sx, sy = find_starting_coords(m, 'S')
    ex, ey = find_starting_coords(m, 'E')

    total = 0

    dsts = get_dsts(m, sx, sy, ex, ey)
    diffs = defaultdict(int)
    for sx, sy in dsts.keys():
        for ex, ey in dsts.keys():
            no_cheat_dst = shortest_path(dsts, sx, sy, ex, ey)
            if no_cheat_dst < 0:
                continue
            cheat_dst = abs(ex-sx) + abs(ey-sy)
            if cheat_dst > 20:
                continue
            diff = no_cheat_dst - cheat_dst
            diffs[diff] += 1

    for k in sorted(diffs.keys()):
        # print(f"diff={k}, count={diffs[k]}")
        count = diffs[k]
        if k >= 100:
            total += count

    return total


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

