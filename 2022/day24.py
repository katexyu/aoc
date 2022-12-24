from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = """
#.######
#>>.<^<#
#.<..<<#
#>v.><>#
#<^v^^>#
######.#
"""

actual = """
#.########################################################################################################################
#>v>^>^<<^>v^>vv<.><>v^>vvv><.>^^.<.^>^vv>v^v>.>>>.v^>>^<v<v<.<<>v^v<^>^<<v>^<<v>><>^v<.^v^^v<v>>>^<.v<^^v>^^<>><v^v^<.v.#
#.>.^<.>^<v<.v>v^<^>>^v^>v>v<.v>v^v.>^><>v<>.^v><>.<v^>.v<<^..>^<<^<<>vv^<v<><v<^^>>v^><.>v<v<^>^^^^>..<<><>>^>^^<.>>v...#
#<<.><<<v^vv^<>>..<<>>>^<.<v^..vv><^vv^^<^<>>v<^>.<>^>v<>^>v><v^>v^>v><>>v^>vv>v^v>.>^v<^<^><^vv<^v>v^^v^.^<>v.^<>^.>v>v<#
#<^v^^><^^<^<v^^<^^<>.<^<v>v..<v^^vvv<>><v^.<>>><>v>^v>v<v.v.vv<vv<>><>><^^<vv>.>>.<>>^>v>^v.>.><<<<>^>^>v>v>^><^^v<^vv<>#
#>><<v<>>>^^^<v^<><<>^^^<^>^v^v<^>>v.><<<<.>>^.<v^>v>^<<^<^^>^><^<>.<>vv^<v<v^<^^<v><v^vv^><.<^.^<v^^>v><^<<^^<vv^><v^v>>#
#<>>^^>vvvvv.><>>^<v^>>v^^<<>^>vv^<^^^<^v<<v^<>v^v<^>>v^vv^<>^<>^<v^v^>v<.vv<<.<vvv<><<^^^v<^<v^^v<^^v>>vv^<.>v<.v^v^vv^.#
#.>v>.>^<>v>>.^vvv<^<^><<^^>.<<v<v^>>v<<<^.<>>>v<v>>^>><>v<^>.v^.^v>v^<>><>><^.v><.>v<>^<^^>v>>v^^v^<<v>v<v>.v.^>^^^^<><>#
#>v<^^><^>.>^^^>vvv><v>>vv<v^<><^>^>^v>^><.v<^<v<>^>^.><^^<v<<><<><v^^.<v^^v^^><.>v<.<^^v^v.v>^v<^<<v<.v>..<vv<>.v<^v<>.<#
#><v>.><..v>v>^^^^<.>.<^^><^>v^^^^.><<^^v.>v<^<>vv>>>><>vv>>><>>>v.^v>>^vv<^<.>^>^><<>v^.<>.v<<<.<<vv<.v^>^<v^<>><>>^v<><#
#<^v<>^<<v>^..vv>^<<><^^<<>^<^^^v^^<^^v<^>><vv^<v<vv<vv.>^v.>^><>>v.>v>>^^v<>>v<<v>.v^vv^><v^<^><^><>>^v<v<.>^<^vv>>>>v^<#
#<>>>^^^><v<>v<^v^v.>v^<^^>>>^^<v<^.v^>.^^><<v<>><><>v<<vv>.v<v^<^^v^<<<^.>>^v^^v.^<><<>vv^>>^<<vv<^>v>><^>^v<v<>v<<.<vv<#
#<.><^.<>v<>^v.<>^>v>v>>.^>^v>>^^v>^.v.>>v>v>vv.><.^>^><.vvv<<v.>^<vv>v>^<^^v.v<<^^>v^^vv^>^.<<<<vv<><><<v>.<v<<<<^v<v>^<#
#>v^v.><^>v>vv^<>.<^<<v^^^v>>><>.^.^>vvv>v.><.>v><v^vv^<v<v>><^>>vv<v>^>vv^>v.<v<>^v>^<vv>^^>^^.^<>.v<<vvv.<v<>v^v<v>^>v>#
#>>>^>v>^^<>>v>^vvv.>^vv^<v>.<>^vv>.<vv><..^^<<^.v<>^<<^.<>^v^^v.^>.^<^>>.>>v.<^^>v>>^<<^<<><<>>^^<^><<<>^.><<<>.vv>.>v^<#
#<.>>v>^<v<.^>><^v<^vv^>v^^<^^^^.>^v<<>^>.>>>vv<.^<>v^^<v><vv.^><<..^><v^v^vv>.>v>>>^>.^^^^<>>^<<>>^vv.<^>vv..><<<.>>>^>>#
#<vv>vv>v<>^<^<^^v.v^>><>><<<.><<^<.>^>v^><>.<<^<^vv><<.>^v<.<>^>vvv>v^.^<<vv>^>>^>><^^<v.<..^..><.v...v^.^^<.v>>v<^<v^><#
#>v^>v^>><>>v><v<v>>.vvv<<^v<^^^.v<<^>.vvv<>>^.v^v.>>>>^>><>.<.><.<^>v>^<^.><^>><<^<v^>vv^>v<>^v.v<^>.<v>v<>v.><>>><.^.^<#
#.v>^v>^v<.^.>^.<^>^>>v<v>>vv<^<<^.<v^>v^^.<v^<.v^^>^<>v^^vv.v..>>vvv<vv<><<><^<vv<v^.^<^v^^vv^>>v<v<<^v<vvv>>>..>>^>.^>>#
#<vvv>>^>>^<vv><>^>><v<v<><>^<^<<^><^<v<.^v<^v^v><<>>>.<>^>^.>.<.>v<.><^><><<<>v^>vv^^..>vv.^>>.<>vv<^v>v>><>^>^^.>v<v<.<#
#>.^^<<..v<<^>>^.^vv<>vv>v^><<v^.vv^<^>>^v<vv.>v>^>>.>^.^.v<<<.^v<>v^<^<>><><>^<v^<<>v^^v>^v.v<v^>>^..<^v<>.>..^^.>^v<v>>#
#><.^v<vv>>.>^<.v<>.<<^>.<>>v^v>^>^^>>^>>>v><>v>>.>>vv.<vvvvvv>v<>.^^<>>>vv^>v..<>^<^>v<>><v^>.>v.^v>.^v>.<v><.>^<<<v>^>.#
#>^>>^vv>vv<^<^<<<>v>v>^^<^^<.>^<>vv<>^>v>>^^^^^<>^>>>v.v^>v<.^<>.v^<v>^^.>vvvv^>>v.^<v<^^>.^^^.^vv^<vv^v<vv<v^>^v^.^^.v>#
#<<^v.>>>v>^<^<.vv>vv^^^.<v^^<v^vvvv^^>^<^<<^vv.^^>.<>^.^..<>v>v^>v>><^>^^^vv<^>v>>>v>^^>^><^^>vv^>.<>^^v^<v^.><v>^^>^v>>#
#<vv><>.v<>.>^v^<v><^.<<<>v^.^><v>v><.<v^><><v<^.>vv<^^v^>v><.^...v>>^<<^><>><v^>><<v^vvv>^^>>.><<vv<v<^v<>>>>^v^>v<v>v<<#
#<.^^>^.^^>>>^<^^^^<<.>^<<<.>>>.>^<v^v>^v.>vv^..^.>.>>.<^^^v>^^vv<<>^v.>>>>^><>><v>v^v<>^^<<v^<<.vv.>^v.v^v^.>vvv..>v.>^>#
########################################################################################################################.#
"""


def find_shortest_path(walls, free, blizzards, bdir, ex, ey, grid):
    minute = 0
    q = deque()
    new_q = deque()
    new_q.append((1, 0))
    b = blizzards
    visited = set()
    while True:
        # Transition the blizzards
        nb = blizzard_step(walls, b, bdir, grid)
        locs = set(nb.values())

        visited.clear()
        q = new_q

        new_q = deque()
        while q:
            # Check possible moves
            x, y = q.popleft()
            for move in find_possible_moves(x, y, locs, walls, grid):
                nx, ny = move
                if nx == ex and ny == ey:
                    return minute + 1
                if move not in visited:
                    new_q.append(move)
                    visited.add(move)
        minute += 1
        b = nb


def find_shortest_pathb(walls, free, blizzards, bdir, ex, ey, grid):
    minute = 0
    q = deque()
    new_q = deque()
    new_q.append((1, 0))
    b = blizzards
    visited = set()
    done = False

    while not done:
        # Transition the blizzards
        nb = blizzard_step(walls, b, bdir, grid)
        locs = set(nb.values())

        visited.clear()
        q = new_q

        new_q = deque()
        while q and not done:
            # Check possible moves
            x, y = q.popleft()
            for move in find_possible_moves(x, y, locs, walls, grid):
                nx, ny = move
                if nx == ex and ny == ey:
                    minute += 1
                    done = True
                    break
                if move not in visited:
                    new_q.append(move)
                    visited.add(move)
        minute += 1
        b = nb


    done = False
    new_q = deque()
    new_q.append((ex,ey))
    while not done:

        # Transition the blizzards
        nb = blizzard_step(walls, b, bdir, grid)
        locs = set(nb.values())

        visited.clear()
        q = new_q

        new_q = deque()
        while q and not done:
            # Check possible moves
            x, y = q.popleft()
            for move in find_possible_moves(x, y, locs, walls, grid):
                nx, ny = move
                if nx == 1 and ny == 0:
                    minute + 1
                    done = True
                    b = nb
                    break
                if move not in visited:
                    new_q.append(move)
                    visited.add(move)
        minute += 1
        b = nb

    new_q = deque()
    new_q.append((1, 0))
    done = False
    while not done:
        # Transition the blizzards
        nb = blizzard_step(walls, b, bdir, grid)
        locs = set(nb.values())

        visited.clear()
        q = new_q

        new_q = deque()
        while q and not done:
            # Check possible moves
            x, y = q.popleft()
            for move in find_possible_moves(x, y, locs, walls, grid):
                nx, ny = move
                if nx == ex and ny == ey:
                    return minute 
                if move not in visited:
                    new_q.append(move)
                    visited.add(move)
        minute += 1
        b = nb


def print_blizzards(blizzards, walls, grid, bdir):
    bi = blizzards.items()
    bc = Counter(blizzards.values())
    for y in range(len(grid)):
        row = ""
        for x in range(len(grid[0])):
            if (x,y) in walls:
                row += '#'
            elif (x,y) in bc:
                if bc[(x,y)] == 1:
                    idx = [idx for idx, val in bi if val == (x,y)][0]
                    row += bdir[idx]
                else:
                    row += str(bc[(x,y)])
            else:
                row += '.'
        print(''.join(row))



def find_possible_moves(x, y, nb, walls, grid):
    deltas = [(0,0), (1,0), (0,1), (-1,0), (0,-1)]
    minx, maxx = 0, len(grid[0])-1
    miny, maxy = 0, len(grid)-1
    moves = []
    for dx, dy in deltas:
        nx, ny = x+dx, y+dy
        if (nx, ny) not in walls and (nx, ny) not in nb and minx <= nx <= maxx and miny <= ny <= maxy:
            moves.append((nx, ny))
        if (nx == 1 and ny == 0):
            moves.append((1, 0))
    return moves


deltas = {
    '>': (1, 0),
    '^': (0, -1),
    'v': (0, 1),
    '<': (-1, 0)
}


def blizzard_step(walls, blizzards, bdir, grid):
    minx, maxx = 0, len(grid[0])-1
    miny, maxy = 0, len(grid)-1
    new = dict()
    
    for idx, c in blizzards.items():
        val = bdir[idx]
        x, y = c
        dx, dy = deltas[val]
        nx, ny = x+dx, y+dy
        if nx == maxx:
            new[idx] = (1,y)
        elif nx == minx:
            new[idx] = (len(grid[0])-2, y)
        elif ny == maxy:
            new[idx] = (x, 1)
        elif ny == miny:
            new[idx] = (x, len(grid)-2)
        else:
            new[idx] = (nx, ny)
    return new


def solvea(inp):
    inp = inp.strip().split('\n')
    grid = list(map(list, inp))
    walls = set()
    free = set()
    blizzards = dict()
    cnt = 0
    bdir = dict()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            val = grid[y][x]
            if val == '#':
                walls.add((x,y))
            elif val == '.':
                free.add((x,y))
            else:
                bdir[cnt] = val
                blizzards[cnt] = (x,y)
                cnt += 1
    walls.add((1,0))
    
    ex, ey = len(grid[0])-2, len(grid)-1
     
    return find_shortest_path(walls, free, blizzards, bdir, ex, ey, grid)
        

def solve(inp):
    inp = inp.strip().split('\n')
    grid = list(map(list, inp))
    walls = set()
    free = set()
    blizzards = dict()
    cnt = 0
    bdir = dict()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            val = grid[y][x]
            if val == '#':
                walls.add((x,y))
            elif val == '.':
                free.add((x,y))
            else:
                bdir[cnt] = val
                blizzards[cnt] = (x,y)
                cnt += 1
    walls.add((1,0))
    
    ex, ey = len(grid[0])-2, len(grid)-1
     
    return find_shortest_pathb(walls, free, blizzards, bdir, ex, ey, grid)


if __name__=='__main__':
    example_ans = solvea(example)
    print(f'example:\n {example_ans}')

    actual_ans = solvea(actual)
    print(f'actual:\n {actual_ans}')

    example_ans = solve(example)
    print(f'example:\n {example_ans}')

    actual_ans = solve(actual)
    print(f'actual:\n {actual_ans}')

