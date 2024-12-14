from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""

actual = r"""
..#.....##......#............#..................................#.....#..............#................#.........................#.
..........................................................................................................#..........#...#.......#
..................#....................#.......................................#.....#....#............#.......#..................
......#...#..##....................................................................#...#.......#..........#..#.....#..............
..#..#.#.............#.#.........#.........##..................#..............#..........................#........................
#..........#.................#..........#...............................#..#.................#.......##..##..#.#..................
......................#......................................................#........................#......................#....
........................#.#.....................................#..............................#.......#.............#.....#......
#.................#...#......#..........#.......#.....#............................................#...........##.........#.....#.
...........................................#.....#............##...............#..............................#...................
.....#..............#......................................#..........#............#..................##...............#......###.
..............#..#.....................................##................#............................#............#......#.......
#........#...................................................#..........................................#.........................
.................................................................................#................................#....#..#..#....
.............................#.###.........#.#...............#..........................................##........................
......................................................................................................................#.........#.
...............#............#............#...#.........#............#.............................#.#........................#....
........................#...............#...............#........#.........#................#....#.#....................#.........
........#...............#...........................................................................................#.............
.................#..........................................................#.....................................................
........#.#.#...................#..#.......#...........#..#............#......#.....................#.....#.........#..#..........
..#.......#..................................................................................................#......#.............
................##...##......................#....................................................#..............................#
............#......................................#...........................#.#...#...............#.....................##.....
..........#...................#.....................#...........................................##................................
.#.......................#...............................................................#........................................
...................................................................#..#................#.....#....................#...............
...........#...........................................................#..........................................................
.....#....#..#..........................................................#..................#.....................##...............
...#................................#.....#...................#...............##...........#..............#.......................
.......##.....#.............#..#.......................................................................#......................#...
......................................#....#.............................................#...#....................#...............
.......#.......#...............#..#.....#..............................#.#......#...............#.................................
......................#.......#.......#..........................................................#................#...........#...
..............................#........................#.......#..#...............................#...............................
...........................#..........#..##.......................#................#..............................................
..............#............#...##........#.................................#................#....#........................#..#....
..............#.........#............................................#.............#......#......#.#....#.........................
.......................#.................................#..#..#..#..............................................#................
........................###..#...............................................................#.........#................#......#..
#........................................................................................#........................................
........................................#..............................##.....#.........................#...........#.............
.............#.........#...#................#..#..........#.....#...........................................................#.....
.......................................#......#.............................#.........#................#..........................
..........................................................#......................#...........#...#.......#........................
#.....................................#.#...#.............................................................#...........#........#..
............................#..................................................................................#............#.....
#.................#.................................................................#..............#...................#..........
........#...................................................................#...............................................#.....
.................#...#..................#.............................................................#.......#...................
...#.....#.................................................................................................#..........#...........
..........#...................................#....#................#......#........................................#.......#.....
.....................................#...............#................................................................#...........
.#............#................................................................#.............................................#....
...........#.........#.....................#...........#^.......................#.....................#..........#................
.....#........#.................................................................................................#.......#.........
..........#..........................#.......#......................#..............................#....#......................#..
...#.........................#.................#....#........#....................................................................
...............#...#........................................#................................#....#........................#.#....
...........#.......................................#......#....#.......................................................#.......#..
#.........#...............#..#..#..........#..............#...........................#...........#.....................#.........
...................#.......................................................#......................................................
.............#..............................................#.......................................#.........#...........#......#
....#......#...#.................................#.....#......#.................................#.................................
...............#...............#......................................................................#...........................
.......................#.........................................................................................................#
.............................#............................................................................#.......................
...................#..#.........#...........................#......#...............#......#.......................................
...#....................................#...................#..#...........................#............#...............#........#
...................#................................................................#............##...............................
........................#.#...................#.....................................................................#...#.........
...................#......#.......#.#......................................................#...............#......................
....#...........................#................#.............................#..#....................#........##.....#..........
.........................#......................................................#.#......................................#........
.........#.............#.................#........................................................................................
.#.#.......#..#....#.......#...#..#......................................................................#.#......................
..#.................#............................................................................#................................
.#................................#...............................................................................................
..........#............#..............................................#...#...............##...............#..................#...
................................#.........................#.......................................................................
........................................................##.......#........................#.....................#.................
......#......................................................#......#.........#........................................#.......#..
...........................................................#............#....#......#.............................................
..................................#...................................................#.................................#...#.....
.......#...#..........#............#.......#........................................#..#.................#........................
....................#........................................#........#...........................................................
.................................##..#............#.................................#.............#..................#....#.......
.#.................#..........#.....#...........#.......................................................#...................#.....
........................#.........................................................................................................
...#..........................................#...........................#.................................#.....................
............#......................................................#.................................#.........#..............#...
.............#........##.........#..................#...#.............#......#....##................#................#............
..................#...........................................................................................#.................#.
.....................#..#..#....................#........................#.........#................................#.............
..............................................#...................#............................#..............................#...
.......................#.#...................................#.............................#...................................#..
................................#...........#.............................#.............#.........#..............................#
...........................#................................#...................................................#.....#...........
..........#..........#.....#..........#..#............#..........#.................#.......#.......#........................#....#
...#.......#...#..............................................................................................#......#......#.....
...........#......................#..#.................#......#.........#.....#.............#............##................#....#.
.......#...........................................#..................#...............#.............................#.............
....#.......#.................................#..................................................................#................
..#..................................#...#............................#.........#....#..........#............................#....
....................................................#.................#...........................................#...............
............#......................................#.........#..................#.....#.#.#.#..#..................................
#..............#.......#...#.#..............#.....#.#.............................................................................
...........#.#.................................#...#........................................#................#.........#....#.....
......#.........................................#.........................#...........................................#...........
...#......#.................................#......#............................................................................#.
...#.................#....##................#...........................................#.........#....#..........................
...........#...#...#..................#...................................#......................................#......#.....#.#.
...................................#....................#................#..................................................#.....
................#.....................................#...........#......#........................................................
..............................#......#..#..............................................##........#......#......................#.#
#...........................#....#....##.....#...........................##..#...................#.....#........#.................
..........#....#.#..................#..........#..#................#.................#..................................##.......#
...................#.....................#......#...........................................................#..........#..........
........#.....#.............................#..............................................#......................................
......#............#.#.................................................................................................#..#.......
.#.........#..................................................................................#....#...........#.................#
........#.....#.......................#.........................................#...........................................#.....
...................#.......#..#......#.................##......................................#...................#..............
.............................#.................................#........#.......#..................................#.........#....
....#....#..........#....###..#...................................................#...#................................#.......#..
...................#...................................................#.......#....#........................#....................
...#................#...........#.......................#.....................................#...#......#......#.................
.......#........................#.........#.............................................................#...#...#.................
....................#.........#..............................#..........................#....................#..#.................
..#..........................#.#...................................#..................#..........#................#...............
"""

deltas = {
  '^': [0, -1],
  '>': [1, 0],
  '<': [-1, 0],
  'v': [0, 1]
}

turn = {
  '^': '>',
  '>': 'v',
  'v': '<',
  '<':'^'
}


def get_positions(m, x, y):
    positions = set()
    while (x,y) in m:
       positions.add((x,y))
       cur = m[(x,y)]
       dx,dy = deltas[cur]
       nx, ny = x+dx, y+dy
       if (nx, ny) not in m:
         break
       nxt = m[(nx,ny)]
       if nxt == '.' or nxt == 'X':
           m[(x,y)] = 'X'
           m[(nx,ny)] = cur
           x, y = nx,ny
       elif nxt == '#':
           m[(x,y)] = turn[cur] 
       else:
           print("should not get here")
    return positions

def solve1(inp):
    inp = inp.strip().split('\n')
    m = to_grid_map(inp)
    x,y = -1,-1
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if inp[i][j] == '^':
                y,x = i, j
                break

    positions = get_positions(m, x, y)
    return len(positions) 


def is_looping(m, x, y):
    start_x, start_y = x,y
    seen = set()
    while (x,y) in m:
       cur = m[(x,y)]
       if (cur, x, y) in seen:
         m[(x,y)] = '.'
         m[(start_x, start_y)] = '^'
         return True
       seen.add((cur, x, y))
       dx,dy = deltas[cur]
       nx, ny = x+dx, y+dy
       if (nx, ny) not in m:
         m[(x,y)] = '.'
         m[(start_x, start_y)] = '^'
         return False
       nxt = m[(nx,ny)]
       if nxt == '.' or nxt == 'X':
           m[(x,y)] = '.'
           m[(nx,ny)] = cur
           x, y = nx,ny
       elif nxt == '#':
           m[(x,y)] = turn[cur] 


def solve2(inp):
    inp = inp.strip().split('\n')
    m = to_grid_map(inp)
    x,y = -1,-1
    for i in range(len(inp)):
        for j in range(len(inp[0])):
            if inp[i][j] == '^':
                y,x = i, j
                break

    positions = get_positions(deepcopy(m), x, y)

    s = 0
    for (xx,yy) in positions:
        if m[(xx,yy)] == '.':
            m[(xx,yy)] = '#'
            if is_looping(m, x, y):
                s += 1
            m[(xx,yy)] = '.'
    return s


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')
    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')
