from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""

actual = """
#..#.#.O...OO....##O....#....O.O#.......O.O.#.O..#..........O...#OO.O..OO..#.#..O.O.OO...#.OOO...OO.
..O..O#OO#....#.#O.#......#...O...O..O##.....O..........OOO.#......#OOO....#.#..O..O......OO....O.OO
O..#O..#O#...O#....O#.O...#.#..##O.O#OOO..OOOOOO.O.#O.O....O......OO#O#..O.........O.#....O..O......
O.O.....#O##..OO.........#.........O.#...#..#...OO##......O.....O..OO#.#.##..OO.........O#.#....#.#.
......#....#OOOO..O#O...#...O#....O#..#..OO##..###.#.O#.O...#O.#..........O..##....O#O....OO.....O##
..##.#O...#......#.O...O.#O.O....#....#..##.........#.O#O.O.#.####..O#.O#......O...#.#.#O..#O...OO#.
.OO.O....O#.O..O.......O.OO#O....#..O.#....OO##..O.O....O...O.#....#......O....#.O..OO....OO..#....#
..OOO......#..#.....#.O.........O....OO..##.OO##...#.#.O#.#......#....###...#..#...##....#..O#...O..
O#.O.O#.O......#..O..O.OO##...O.....O...##...O.OO.O..##....#.O......O#.....O.OO.O..O.........#..#..O
.##..#.....#....#...O.O#O#...##O....O..O.#O#.#OO.#..O#..O..#O###...........#.##O.###O...O.#....O#..O
.#.#.#O...OO....O.###........OOO...#.#.O.....O.....#..#....#...O....O.#O...O.O.#.#...#O#O#O.#O.O...O
.#......O.O.#..O#..#......#.....O...#.O.....O.......#.......#..O...#.#.#.##.#.#...O...........###O.#
#..O..#....##O##..#.#.OO..O#O........O#..##O....#OOO..O.#.#.#..##.OO.#..O.#...O..O.O......#..O......
O#O.#...O...O....#....O..O#...O#..#O.....#..#....#.O.O##.#.O.O#O#......#.##..O.O#.O.....O...O#O..OO#
.OO#.....O....O.##...#.......#O#..OO.OO#.#..O.#.O.O..O.#.O.O..OO.O...OOO...#O..........#..#.O.O#...O
O..O.#......#.O.O....#..O.....O...#....O..##.#.###....#.#...#O....O........O...O...OO...##..O.OO#..#
.O.O.####.#.O....O#..O.O#.##.OO..#.....O......OO..#.O.O...#..#....#..O..O..O#O......#O.OO...##O...O.
.O.....O.........#...O..O..O.O#..##.#...O#.......O.##O.....#.#.#..O..O...#.OO#.#.O..#...O..O.O......
......O.O...O......O#.O.#OO.....#..#..........O..OOO...O...#.#..O#....O.#.O..O.#O..O..#.#..#.O..#...
##.#.#O...O.#O..O..#.OO..###.......O....OO......#...O...O.#...O..O.#...#...O.O#..##O#..#...O.#....OO
.OO#..#.#.#O..O.O..O#....#.O......###.O.O.O.#.......##...O##OO#.....##..O#.#..#.#.O.#.#...O..O.#...#
#...OO..O..OO......O..#..#...O....O.OOOO##.....#O.....#.#..#..##.......O..O.#...#.#..#.OO#...O.O..O.
##...O.OOO#.....#..O#..OO......OO#O.#O.#....#.OOO..#..#OO.O.O..#.O......OO.............#.O#.OO..#OO.
.O#.#.....O....O#...#...O....O#O#........#O#.O.#.O...O.O..#O...O......#..O.#............#...##O#...O
#...O.......#.O.O..##.O.#....O..#.....O.O...#...O.O..O.....O.OO..O..##..O...O..O......O...OO.OO.O.O.
O......#......#OO...OO#.#O#....#....#.O.OO.#...O.#.#..O..#O..#....O..O....#....#....##.....O.OO#.#O.
...O.O..#..#.O.#.....##.O.O.#...O..O..#.....#..OO#...O..###..#.....#.#O.....O.....##.#....O..O...O##
#..#O#O.OO.#...O#..##.#..O.O.#....O#.#OOO..#O...OO....O.O#O.O..O#..#..O#.#.#O.##.#O.#O..O...#...#OO.
.....O.....OO.....O.O#..OO...O.......#O....O....OO.O#.......#.O.#.O.O#O.#.....#....O.O.#..#.....O.OO
...OOOO....##.O.....OOO.O..OO...O#..O...#O....O..O#....OO...#.#....O#.O.#......#O.O....O.......O..O.
...#.##.##O#O#....O....#.#...#........#...#.O..#.#O.....####.O#....#.O#......O...#....#.O..#..O.#.O.
..O.......O..O.###.....#......##.#.##.OO..OO........OOO..#.O..O.....O...#O....##..O.OOOO......O#.O..
.#..O.O.O..#.#.#..O##O.#.......O..#....O.O....#....#.#.#O..##.....O.#O.....##O.#..#..O..#..OO....#.#
...O.....O#..O#O#...O....##..O.....O..#.O...#..O..#....O#O...OO..OO.#........O............#....O...O
.##OOO###..O..OO..##O#....O....OO....#.O#..#O....#.##O......O.#O.#O..O......#......#.##O#OO......O#.
.#O#.....O#.....#...##...O..#O..O.#.O..#..O........O#.....#..O..OO#O...OO......O..#...O#...#.OOOO...
.........O.#.#O....#OO...##........#.#..#.#..........OO..O..O..OOO#.........O.....O#..#OO.....#.#..#
#..O.O...#..O.O##OO#..O.#O.....O.O..O.O.O.#.O.#....#.......O#O#.OO..##.....OO...#.........O.O....O.O
OO#.#.##...#....#........OO....O..OO..O#.####.....#OO..#.....#........OO.#..#O..#.O#O#O.O..OO#O.O.O#
#....O.O#..#O...OO..O.OOO.#.O.##.##..O..#O#.....O.....#O.O#.#...#...O.O.........O..#...#....O...O.#.
....#O..OO..O......#O#....O.O....#..#....#....#.....OOO##.O..#..####..##.#..##..O...O.....O#....OOO.
O...O..O#OO.####O..#OO..#.#.O....O.#.O.##........#..OOO...O....O........O.O.O.O.OOO..#OOO.#.#OO..#..
O#O#.#..#..O..#.....#.#......O..O...O.O...#..O..#.O.....#O.....#.......#.O.O.......O...#....O..OOO#O
.#...O...#.O......O....O....O.##.OO...O......#..O#O......O..O.........O.O...#.....#...#.##......#O..
##O#.O......#.O..O..O.OO..##OO##.#O..O.#OO...O#..O.O.O..#.OO...O#O##O......#.#.#....O..O.......O...#
O.#O.OO##....OO.......O......#....#O##....#....O#O......O..#.#.....O.OO.....O.#..O.#OO.O..OO.#..#.#.
O.#.#.....#.O#.........O....O.#.O.#..O....O....OO.O#.#...O.O#..OO#O...#..#..#....#.##..OO.....#.....
.#O.#O...O..#.OO#..O....#....#.#####............OO.O..OO.#....OO......#O...O.....O.#O..#.....#...O.O
#.#....OO.O.O...O....O......#...#....#...##..#.#.....O..O#.#O.#.OO.##.O.#..........OO.O#.......##O#.
O.O..O..##...#..........O.#.#.....O.#...O#.O..O........#.O#O......OO.#....OO..O.....O.O......#.OO..O
#...#O..OO...#O#.OO#.O..OO.O.O.O##.O#O##......O#..O.#O...##...OOO...#O...O...O..O.O.##.#.......##..O
.#.O#O........###O.##.O#..#OO.O.....OO......O......O.O#.....#O#...#...#.O......O.#.....#.O.####.O...
..#..OOO...O#.###OOO#.#.O#....##O..#O.##......O.##...O...#...O....O.....#.O.#....#.......O..##...O.#
OOO.##.#..OOO.....O...#..##.O...#...#.O##.......#.OO#..#.#...O.....#.#...##.O.O.O....#.O....O#..O...
#..#..OO.....#O.....O#..O.O......O.###O.#..#..OO.#.O.#...OO...#..O.#O#..#.#..O.O..O....OO#...O..#...
.#.O..#...O.#.O.#.OO..O..#.O..OOO.O......O.#.#O.......OO...O#.......O.O.....#..#.......O...O.O..##O#
.O#....#O.#.....#......O...O........O...O.O........OO.O#.O...#.#....O..#.#O...#.OO#..#OO#.....O...##
........O..#..#.O###O..O..O.O...###.O...#..O..O.O#O...#..O#O#....O.#.....O..#..OO.O.O...O.......#OO.
#.OO..O..O..#.O..#..O....O.#O#.OO.O#.#...#...........O..O..O#.O....#......#........O....O.O.O.#..O..
.O........#......#O...#O#...##O##...O.....#.O...##O.#.#O....O#...#O....#OO..#.#.#...#..#O.#......O.O
O#..O..#O...O..O.........O......#.OO.O#.O..O....O........#.O..#...OOO.#..O.##O....O..O#.#..#O#..O##O
.#..#.....#....#..O.O..O..#..OO##O..####.............O.#OO....#.O.....#OO...OO..#O#.#.#..OO.........
..#O..#...O.O....OO.O#.#O.##...#....#OOO...O.....#......#....O##OO....#....#....#O#.O.#.#..O...#..O.
...OO#..#..O....O.OO.#O##..O.....#..#....##.O.#.O....O....O.OO#.#O.OO.OO.#O.........#..##....O..O...
.O#.........O.....#.OO.OO.O.O..O.O...#.O...O.....O..OO..#OO....O.OO..#.#O.O.#..OO..O....O.O..O#O..OO
##.#..O#....O...#...O....#.......#.#..#..O...#O##...O#...O...#..........O.#O....OO..........#.......
.OO...O.#............O.#..#..O...#.#...#.O##OO#...OOO..O..#.OO..#.......#OO.............O.#..#O.#...
...#.#O.#....#.##..........#...#OO.O..#.O.....O.O..#.#O.....#..#O............OO#O..#O.....O...OO..O#
#O#.O.....O.......#.......OO#..O.......O#...O........O..#.#.........OO..#....#....O...O.....#..O.#..
....O..O.##..#.....O....##..OOO....O.O....O.....OO#O.O#.....##O.##.O.O.#..OO.OO.##.O.#........OO....
.O.O#...#OO.#..O.#..#.##.#.......O#O.O......O.O......OO..O....#.O........#.#....#.O#O.#..O#O......O.
.OO..#.O.#.....O#O..#..#.#....O.O####.#.O.O#OO......O........#O.O#OO#O..O.O......O.O.O#...#.O..O...O
....O..O...##...##.##.O...#......#.O..O#O...O#O..OO....OO.#..#O#.OOO.#..#..O....#OO....#...O.#O..OO.
#..O#..#..#..O.O.O..#..O.O#.O.....OO....O...O.OO#OO....O.#O..O.O......O..OOO...O#OO..OO.O#....O.OO..
O.O.....O...##..#...#.O.#.#..O..O................O.#..OO.#....#......O#O..O.#.O.#..#O...........O..#
.....OO..O..OO...O.#..........O.#O.........OO#.............#..OO...##.#.#.OO.O.O.#.##.#.OO.OOO......
...#...#OOO.OOO..OO..##O.O.......O#.#O....O...#.##.##.##.#.O..O.O#O....O.O...O.#.O...O........O..O..
.O.....#.O#..#..##.OO......#........#...O.#O.#..O#O.O.OO...##......O..O.....#..O...O.O.OO.O.O.#O##.O
O....O.O..#.#...#..O.#O...#O.O..OOO.....O.#..O.O.#..#...#..O.....#..#..##...........###.....#...OO.#
..#.....O.OO...O#........O..#O.....O.....OO...#..#.OOO......O#.#.O.O.##O.#..........O.#..O..OOO.....
#..O.#O#.#.......#..O..#..#...#.O..#.....O........O.#..#OOO...O......#..O...O..#....#..O.........#..
..O.OO..#O....OOOO...O....O#O....##OO.O.O..O.O......O..O.OO....O.OOO.O......#..O...#O....O...#.OO#..
O.#O....OO....##.O......O...O..O.#....O#OO.O..#....O....##O..O....O..#.O...#...OO.O..O.O#.....O.OO..
#.#O....O..#.O#..O...O#...O.O..O..........OO.......O#......O.......##.#..#.###.#O.O.......OO..#.O#O.
O..##...O#O...........OO..#.#O...#OO......O#OO.#OO.#..O#OO#.#O....OO.##..O.#O.#..#.O.#.#..#O.OO.O.OO
O.####..O#..O#....#.O#.O.#......O..O..##...#........O.......OO##.O.#.....O..O#..O...#..OO.....#....O
...####..O..O#.#..OOO.....OO..............O.#OO.O#..##OO...#....O..#.##........##.O....O.....#..#..O
..O.O..#OO#..O...O...OO...O....#...O.OO#.....#OO.....#.O......O.#O.#.#..#..........###OO#.OO...O..O.
.O#.....O...O......O.#..OO..OOO......#O#.O....O.....O..O##.O#....OO.O....O..#.....O.O.O..O....OO.O..
....OO.....##O....O##..#..OO....O.#O.OO...#....###.O....O.##..#..OOO#O#.......O...O.O..#O.......O..#
...O...O..O.......O.#O.O........#.OOOO..............O#...O.O#O.....#......O#.#.........##.#.##O.#...
.O.....O.O.O.#.O#OO#.....#..O.O#.O#.....##.....O..............#.......O...#O.#O...#.O...#.#O.....#O.
.........##...#.O.#..#...#OOOO.#.OOOO...#O....O...O#....OO..##.OO..O.#.....##.O.#.O#...OOO..#.O##.O.
#O..#....#.O....OO..OO#...#..#..O......#...#O.O....#....O...O.#.......OO....O...#...#...#.#...O....O
.OO.#O.OOO##OO..#OO#..O.O..O.#..#..#....O...OO.O..##..#.....OO.#...#.....#.#....O.O..#...O.#......#.
OO..#..O#O.O..O.#..............##..OO#O#O.##..O#...O..O#...O....##..##O#............###OO........##.
..O..#..#.O....O.#.........OO.#...O.....OO.#..O..#....O...#..#...##..OOO....#..O#....#.......O.#O.O#
O.O.OO..O.#.O.O.#.##.##.O..O.O...###..O..##..O#O#....O....O..O#O.........##..O#.OO.O....#O.OOO...#.#
..#....O..O.....OO..#..O.OO..#OO.OOO...OO..##.O..O......O#.O.#..#O.O#..#.....O...O....#..###.O....#.
#.......O.O.O.#....#..#O.O...OOO.......O...........#.O..O..O.O..#..#.O...O.O..O....#.O.O#....OO.O..#
"""


def solve1(inp):
    inp = inp.strip().split('\n')
    mapping = to_grid_map(inp)
    max_y = len(inp)
    max_x = len(inp[0])

    for x in range(max_x):
        for y in range(max_y):
            val = mapping[(x,y)]
            if val == 'O':
                new_y = highest_y(mapping, x, y)
                if new_y is not None and new_y != y:
                    mapping[(x,new_y)] = 'O'
                    mapping[(x,y)] = '.'

    total = 0
    for k, v in mapping.items():
        if v == 'O':
            total += (max_y - k[1])    

    return total


def do_cycle(inp):
    inp = inp.strip().split('\n')
    mapping = to_grid_map(inp)
    max_y = max(k[1] for k in mapping.keys())
    max_x = max(k[0] for k in mapping.keys())

    # up
    for x in range(max_x+1):
        for y in range(max_y+1):
            val = mapping[(x,y)]
            if val == 'O':
                new_y = highest_y(mapping, x, y)
                if new_y is not None and new_y != y:
                    mapping[(x,new_y)] = 'O'
                    mapping[(x,y)] = '.'
    # left
    for x in range(max_x+1):
        for y in range(max_y+1):
            val = mapping[(x,y)]
            if val == 'O':
                new_x = lowest_x(mapping, x, y)
                if new_x is not None and new_x != x:
                    mapping[(new_x,y)] = 'O'
                    mapping[(x,y)] = '.'

    # down
    for x in range(max_x+1):
        for y in range(max_y-1, -1, -1):
            val = mapping[(x,y)]
            if val == 'O':
                new_y = lowest_y(mapping, x, y)
                if new_y is not None and new_y != y:
                    mapping[(x,new_y)] = 'O'
                    mapping[(x,y)] = '.'

    # right
    for x in range(max_x, -1, -1):
        for y in range(max_y+1):
            val = mapping[(x,y)]
            if val == 'O':
                new_x = highest_x(mapping, x, y)
                if new_x is not None and new_x != x:
                    mapping[(new_x, y)] = 'O'
                    mapping[(x,y)] = '.'

    return '\n'.join(''.join(mapping.get((x, y), ' ') for x in range(max_x+1)) for y in range(max_y+1))


def highest_y(mapping, x, y):
    for yi in range(y, 0, -1):
        val = mapping[(x, yi-1)]
        if val != '.':
            return yi
    return 0

def lowest_y(mapping, x, y):
    max_y = max(k[1] for k in mapping.keys())
    for yi in range(y, max_y):
        val = mapping[(x, yi+1)]
        if val != '.':
            return yi
    return max_y


def highest_x(mapping, x, y):
    max_x = max(k[0] for k in mapping.keys())
    for xi in range(x, max_x):
        val = mapping[(xi+1, y)]
        if val != '.':
            return xi
    return max_x

def lowest_x(mapping, x, y):
    for xi in range(x, 0, -1):
        val = mapping[(xi-1, y)]
        if val != '.':
            return xi
    return 0


CYCLES = 1000000000

def solve2(inp):
    m = inp
    seen = dict()
    rev = []
    initial_offset = 0
    for i in range(CYCLES):
        m = do_cycle(m)
        if m in seen:
            initial_offset = seen[m]
            rev = rev[initial_offset:]
            break
        seen[m] = i
        rev.append(m)

    cycle_length = len(rev)
    offset = (CYCLES - initial_offset - 1) % cycle_length
    m = rev[offset] 

    return compute_load(m)


def compute_load(m):
    total = 0
    mapping = to_grid_map(m.split('\n'))
    max_y = max(k[1] for k in mapping.keys()) + 1

    for k, v in mapping.items():
        if v == 'O':
            total += (max_y - k[1])
    return total


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')
    assert example_ans == 136

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')
    assert example_ans == 64

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

