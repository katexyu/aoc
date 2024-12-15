from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example1 = r"""
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
"""

example2 = """
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
"""

example = r"""
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""

with open('day15.txt', 'r') as f:
    actual = f.read()


dirs = {
    '<': (-1, 0),
    'v': (0, 1),
    '^': (0, -1),
    '>': (1, 0)    
}


def do_step(m, d, x, y):
    if d not in dirs:
        return x, y
    dx, dy = dirs[d]
    nx, ny = x+dx, y+dy
    nv = m[(nx, ny)]
    if nv == '.':
        m[(x, y)] = '.'
        m[(nx, ny)] = '@'
        return (nx, ny)
    if nv == '#':
        return (x, y)
    # Otherwise nx, ny contains a box
    # Keep checking in the same direction until we hit a space or wall
    lx, ly = nx, ny
    while (lx, ly) in m:
        lx+= dx
        ly+= dy
        lv = m[(lx, ly)]
        if lv == '.':
            m[(lx, ly)] = 'O'
            m[(nx, ny)] = '@'
            m[(x, y)] = '.'
            return (nx, ny)
        elif lv == '#':
            break
    return (x, y)


def sum_boxes(m):
    tot = 0
    for c, v in m.items():
        if v == 'O':
            x, y = c
            tot += 100*y+x
    return tot


def solve1(inp):
    inp = inp.strip().split('\n\n')
    m = to_grid_map(inp[0].split('\n'))
    dirs = inp[1].strip('\n')

    x,y = find_starting_coords(m, '@')

    for d in dirs:
        x, y = do_step(m, d, x, y)

    return sum_boxes(m)


def vertical_overlap(m, x, y, dy):
    pts = set()
    v = m[(x, y)]
    if v == ']':
        x -= 1
    pts.add((x, y))
    q = [(x, y)]
    blocked = False
    while q:
        xx, yy = q.pop(0)
        lx, ly = xx, yy+dy
        rx, ry = xx+1, yy+dy
        lv = m[(lx, ly)]
        rv = m[(rx, ry)]
        if lv == '#' or rv == '#':
            blocked = True
        if lv == '[' and (lx, ly) not in pts:
            pts.add((lx, ly))
            q.append((lx, ly))
        if lv == ']' and (lx-1, ly) not in pts:
            pts.add((lx-1, ly))
            q.append((lx-1, ly))
        if rv == ']' and (rx-1, ry) not in pts:
            pts.add((rx-1, ry)) 
            q.append((rx-1, ry))
        if rv == '[' and (rx, ry) not in pts:
            pts.add((rx, ry))
            q.append((rx, ry))
    return pts, blocked


def move_pts_vertical(m, pts, dy):
    sorted_pts = sorted(pts, key=lambda y: y[1]*-1*dy)
    for lx, y in sorted_pts:
        rx = lx+1
        ny = y + dy
        m[(lx, ny)] = m[(lx, y)]
        m[(rx, ny)] = m[(rx, y)]
        m[(lx, y)] = '.'
        m[(rx, y)] = '.'


def do_step2(m, d, x, y):
    if d not in dirs:
        return x, y
    dx, dy = dirs[d]
    nx, ny = x+dx, y+dy
    nv = m[(nx, ny)]
    if nv == '.':
        m[(x, y)] = '.'
        m[(nx, ny)] = '@'
        return (nx, ny)
    if nv == '#':
        return (x, y)
    # Otherwise nx, ny contains a box
    # Keep checking in the same direction until we hit a space or wall
    lx, ly = nx, ny
    while (lx, ly) in m:
        lx+= dx
        ly+= dy
        lv = m[(lx, ly)]
        if lv == '.':
            # simple if horizontal, just shift everything in one direction
            if (abs(dx) > 0):
                for xx in range(lx, nx, -1*dx):
                    m[(xx, ly)] = m[(xx-dx,ly)]
                m[(nx, ny)] = '@'
                m[(x, y)] = '.'
                return (nx, ny)
            else:
                # Check how many boxes need to be moved up or down
                pts, blocked = vertical_overlap(m, nx, ny, dy)
                if not blocked:
                    move_pts_vertical(m, pts, dy)
                    m[(nx, ny)] = '@'
                    m[(x, y)] = '.'
                    return (nx, ny)
        elif lv == '#':
            break
    return (x, y)


def sum_boxes2(m):
    tot = 0
    for c, v in m.items():
        if v == '[':
            x, y = c
            tot += 100*y+x
    return tot


def solve2(inp):
    inp = inp.strip().split('\n\n')
    raw_map = inp[0].split('\n')
    new_map = []
    for line in raw_map:
        newline = ''
        for c in line:
            if c == '#':
                newline += '##'
            elif c == 'O':
                newline += '[]'
            elif c == '.':
                newline += '..'
            elif c == '@':
                newline += '@.'
            else:
                raise 'should not get here'
        new_map.append(newline)

    m = to_grid_map(new_map)
    print_grid_map(m)
    dirs = inp[1].strip('\n')

    x,y = find_starting_coords(m, '@')

    for d in dirs:
        x, y = do_step2(m, d, x, y)

    return sum_boxes2(m)


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

