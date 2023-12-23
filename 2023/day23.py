from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
"""

with open('day23.txt', 'r') as f:
    actual = f.read()


def solve1(inp):
    inp = inp.strip().split('\n')
    ex, ey = len(inp[0])-2, len(inp)-1
    grid = to_grid_map(inp)
    return find_longest_path(grid, ex, ey)


def find_longest_path(grid, ex, ey):
    sx, sy = 1, 0
    longest_paths = []
    q = [(sx, sy, 0, 0,0)]
    longest = defaultdict(int)
    longest[(sx, sy)] = 0
    while q != []:
        x, y, l, fx, fy = q.pop(0)
        longest[(x,y)] = max(l, longest[(x,y)])
        if x == ex and y == ey:
            continue
        for dx, dy in [[1,0], [-1,0], [0, 1], [0, -1]]:
            xx, yy = x+dx, y+dy
            if (xx, yy) not in grid or (xx, yy) == (fx, fy):
                continue
            v = grid[(xx, yy)]
            if v == '#':
                continue
            if dy == -1 and v == 'v':
                continue
            if dx == -1 and v == '>':
                continue
            if v == '>':
                xx += 1
                q.append((xx, yy, l+2, xx-1, yy))
            elif v == 'v':
                yy += 1
                q.append((xx, yy, l+2, xx, yy-1))
            else:
                q.append((xx, yy, l+1, x, y))

    return longest[(ex,ey)]

        
def find_longest_path2(grid, ex, ey):
    vertices = [] 
    # Simplify the graph to only spots with multiple forks
    for k, v in grid.items():
        if v == '#':
            continue
        x, y = k
        valid_neighbors = 0
        for dx, dy in [[1,0], [-1,0], [0, 1], [0, -1]]:
            xx, yy = x+dx, y+dy
            if (xx, yy) in grid and grid[(xx,yy)] != '#':
                valid_neighbors += 1
        if valid_neighbors > 2:
            vertices.append((x,y))

    # Find all pair distances without hitting another vertex

    sx, sy = 1, 0

    pairs_length = defaultdict(list)

    # Add start and end
    vertices.append((sx, sy))
    vertices.append((ex, ey))

    for v1, v2 in combinations(vertices, 2):
        v1x, v1y = v1
        v2x, v2y = v2
        l = find_length_between(grid, v1x, v1y, v2x, v2y, vertices)
        if l is not None:
            pairs_length[(v1x, v1y)].append((v2x, v2y, l))
            pairs_length[(v2x, v2y)].append((v1x, v1y, l))

    longest = defaultdict(int)
    update_longest(sx, sy, set(), pairs_length, longest, 0)
    return longest[(ex, ey)]


def update_longest(x, y, visited, adj, longest, path_length):
    if (x,y) in visited:
        return

    visited.add((x,y))

    longest[(x,y)] = max(longest[(x,y)], path_length)
    for xx, yy, l in adj[(x,y)]:
        update_longest(xx, yy, visited, adj, longest, l+path_length)
    visited.remove((x,y))


def find_length_between(grid, sx, sy, ex, ey, vertices):
    q = [(sx, sy, 0, sx, sy)]
    x2, y2 = -1, -1
    while q != []:
        x, y, l, fx, fy = q.pop(0)
        if (x,y) == (ex,ey):
            return l
        for dx, dy in [[1,0], [-1,0], [0, 1], [0, -1]]:
            xx, yy = x+dx, y+dy
            if (xx, yy) not in grid or (xx, yy) == (fx, fy):
                continue
            v = grid[(xx, yy)]
            if v == '#':
                continue
            if (xx, yy) in vertices and (xx, yy) != (ex, ey):
                continue
            else:
                q.append((xx, yy, l+1, x, y))
    return None


def solve2(inp):
    inp = inp.strip().split('\n')
    ex, ey = len(inp[0])-2, len(inp)-1
    grid = to_grid_map(inp)
    return find_longest_path2(grid, ex, ey)


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')
    assert example_ans == 94

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')
    assert example_ans == 154

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

