from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = """
        ...#
        .#..
        #...
        ....
...#.......#
........#...
..#....#....
..........#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
""".split('\n')

f  = open('day22.txt')
actual = f.readlines()


FACING = ['>', 'v', '<', '^']

delta = {
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
    '^': (-1, 0)
}



def categorize_points(grid, size):
    if size == 4:
        return categorize_points4(grid)
    else:
        return categorize_points50(grid)


# I hardcoded these through visual inspection
def categorize_points50(grid):
    faces = defaultdict(list)
    bounds = dict()

    lower = 1000000
    for y in range(50):
        cnt = 0
        for x, char in enumerate(grid[y]):
            if char != ' ':
                lower = min(x, lower)
                face = 1 if cnt < 50 else 2

                faces[(y,x)] = face
                cnt += 1
    bounds[1] = ((0, 50), (lower, lower+50))
    bounds[2] = ((0, 50), (lower+50, lower+100))
    bounds[3] = ((50, 100), (lower, lower+50))
    bounds[4] = ((100, 150), (lower-50, lower))
    bounds[5] = ((100, 150), (lower, lower+50))
    bounds[6] = ((150, 200), (lower-50, lower))

    for y in range(50, 100):
         for x, char in enumerate(grid[y]):

            if char != ' ':
                faces[(y,x)] = 3
                faces[2].append((y,x))

    for y in range(100, 150):
        cnt = 0
        for x, char in enumerate(grid[y]):
            if char != ' ':
                face = 4 if cnt < 50 else 5
                faces[(y,x)] = face
                cnt += 1

    for y in range(150, 200):
         for x, char in enumerate(grid[y]):
            if char != ' ':
                faces[(y,x)] = 6

    return faces, bounds


def categorize_points4(grid):
    faces = defaultdict(list)
    bounds = dict()

    lower = 1000000
    for y in range(4):
        cnt = 0
        for x, char in enumerate(grid[y]):
            if char != ' ':
                lower = min(x, lower)
                face = 1 if cnt < 4 else 2

                faces[(y,x)] = face
                cnt += 1
    bounds[1] = ((0, 4), (lower, lower+4))
    bounds[2] = ((4, 8), (lower-8, lower-4))
    bounds[3] = ((4, 8), (lower-4, lower))
    bounds[4] = ((4, 8), (lower, lower+4))
    bounds[5] = ((8, 12), (lower, lower+4))
    bounds[6] = ((8, 12), (lower+4, lower+8))
    for y in range(4):
       for x, char in enumerate(grid[y]):
          if char != ' ':
              faces[(y, x)] = 1

    for y in range(4,8):
        cnt = 0
        for x, char in enumerate(grid[y]):
            if char != ' ':
                face = -1
                if cnt < 4:
                    face = 2
                elif 4 <= cnt < 8:
                    face = 3
                else:
                    face = 4
                faces[(y,x)] = face
                cnt += 1

    for y in range(8, 12):
        cnt = 0
        for x, char in enumerate(grid[y]):
            if char != ' ':
                face = 5 if cnt < 4 else 6
                faces[(y,x)] = face
                cnt += 1

    return faces, bounds


def print_categorized(grid, faces):
    for y in range(len(grid)):
        row = []
        for x in range(len(grid[0])):
            row.append(str(faces.get((y, x), ' ')))
        print(''.join(row))


DIRS_EXAMPLE = {
    # R D L U
    1: [(6, 180), (4, 0), (3, 90), (2, 180)],
    2: [(3, 0), (5, 180), (6, 270), (1, 180)],
    3: [(4, 0), (5, 90), (2, 0), (1, 270)],
    4: [(6, 270), (5, 0), (3, 0), (1, 0)],
    5: [(6, 0), (2, 180), (3, 270), (4, 0)],
    6: [(1, 180), (2, 90), (5, 0), (4, 90)]
}

DIRS = {
    # R D L U
    1: [(2, 0), (3, 0), (4, 180), (6, 270)],
    2: [(5, 180), (3, 270), (1, 0), (6, 0)],
    3: [(2, 90), (5, 0), (4, 90), (1, 0)],
    4: [(5, 0), (6, 0), (1, 180), (3, 270)],
    5: [(2, 180), (6, 270), (4, 0), (3, 0)],
    6: [(5, 90), (2, 0), (1, 90), (4, 0)]
}

    
def find_next(grid, x, y, facing, faces, bounds, size=50):
    dy, dx = delta[facing]
    ny, nx = y+dy, x+dx
    if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]):
        nxt = grid[ny][nx]
        if nxt != ' ':
            return ny, nx, facing
    # figure out how far along the cube you are
    offset = 0
    if dx != 0:
        offset = y % size
    else:
        offset = x % size

    dirs = DIRS if size == 50 else DIRS_EXAMPLE

    face = faces[(y, x)]
    nface = -1
    orientation = -1
    if dx == 1:
        nface, orientation = dirs[face][0]
    elif dx == -1:
        nface, orientation = dirs[face][2]
    elif dy == 1:
        nface, orientation = dirs[face][1]
    else:
        nface, orientation = dirs[face][3]

    yb, xb = bounds[nface]
    miny, maxy = yb
    minx, maxx = xb
    fidx = FACING.index(facing)

    # Figure out how to transpose where you are to the next face
    if orientation == 0:
        if dy == 1:
            # go to the top
            return miny, minx+offset, facing
        elif dy == -1:
            # go to the bottom
            return maxy-1, minx+offset, facing
        elif dx == 1:
            return minx + offset, minx, facing
        elif dx == -1:
            return minx + offset, maxx-1, facing
    elif orientation == 180:
        opposite = FACING[(fidx+2) % 4]
        if dy == 1:
            return maxy - 1, maxx - 1 - offset, opposite
        elif dy == -1:
            return miny, maxx - 1 - offset, opposite
        elif dx == 1:
            return maxy - offset - 1, maxx-1, opposite
        elif dx == -1:
            return maxy - offset - 1, minx, opposite
    elif orientation == 270:
        rotated = FACING[(fidx+1) % 4]
        if dy == 1:
            return miny + offset, maxx - 1, rotated
        elif dy == -1:
            return miny + offset, minx, rotated
        elif dx == 1:
            return miny, maxx - offset - 1, rotated
        elif dx == -1:
            return maxy - 1, maxx - offset - 1, rotated
    elif orientation == 90:
        rotated = FACING[(fidx-1) % 4]
        if dy == 1:
            return maxy - 1 - offset, minx, rotated
        elif dy == -1:
            return maxy - 1 - offset, maxx - 1, rotated
        elif dx == 1:
            return maxy-1, minx + offset, rotated
        elif dx == -1:
            return miny, minx + offset, rotated


def solvea(inp):
    m = inp[1:-3]
    m = [r.strip('\n') for r in m]
    max_width = max(len(row) for row in m)
    m = [row.ljust(max_width, ' ') for row in m]

    path = inp[-2]

    grid = list(map(list, m))
    y = 0
    x = grid[0].index('.')

    facing = '>'
    ans = ''
    while path:
        r = path.index('R') if 'R' in path else len(path) -1
        l = path.index('L') if 'L' in path else len(path) -1
        nxtidx = min(l, r) + 1
        instr = path[:nxtidx]
        steps = int(instr[:-1]) if nxtidx != len(path) else int(instr)

        path = path[nxtidx:]
        if nxtidx != len(path):
            d = instr[-1]

        cnt = steps
        dy, dx = delta[facing]
        while cnt > 0:
            if grid[y][x] != ' ':
                grid[y][x] = facing
            ny, nx = (y+dy) % len(grid), (x+dx) % len(grid[y])
            nxt_row = grid[ny]
            nxt = nxt_row[nx]
            while nxt == ' ':
                ny, nx = (ny+dy) % len(grid), (nx+dx) % len(grid[ny])
                nxt = grid[ny][nx]
            if nxt == '#':
                break
            if nxt == '.' or nxt in FACING:
                y, x = ny, nx
                cnt -= 1

        idx = FACING.index(facing)
        if d == 'L':
            facing = FACING[(idx-1) % 4]
        elif d == 'R':
            facing = FACING[(idx+1) % 4]

    row = y
    col = x
    f = FACING.index(facing)

    print(f"r={row}, c={col}, f={f}")
    return (row+1) * 1000 + (col+1) * 4 + f


def solveb(inp, size=50):
    m = inp[1:-3]
    m = [r.strip('\n') for r in m]
    max_width = max(len(row) for row in m)
    m = [row.ljust(max_width, ' ') for row in m]

    faces, bounds = categorize_points(m, size=size)

    path = inp[-2]

    grid = list(map(list, m))
    y = 0 
    x = grid[0].index('.')
    
    facing = '>'
    ans = ''
    while path:
        r = path.index('R') if 'R' in path else len(path) -1
        l = path.index('L') if 'L' in path else len(path) -1
        nxtidx = min(l, r) + 1
        instr = path[:nxtidx]
        steps = int(instr[:-1]) if nxtidx != len(path) else int(instr)
        
        path = path[nxtidx:]
        if nxtidx != len(path):
            d = instr[-1]

        cnt = steps
        while cnt > 0:
            if grid[y][x] != ' ':
                grid[y][x] = facing
            ny, nx, nfacing = find_next(grid, x, y, facing, faces, bounds, size=size)

            nxt_row = grid[ny]
            nxt = nxt_row[nx]
            if nxt == ' ':
                raise "Got blank, This shouldn't happen"
            if nxt == '#':
                break
            if nxt == '.' or nxt in FACING:
                facing = nfacing
                y, x = ny, nx
                cnt -= 1

        idx = FACING.index(facing)
        if d == 'L':
            facing = FACING[(idx-1) % 4]
        elif d == 'R':
            facing = FACING[(idx+1) % 4]
   
    row = y
    col = x
    f = FACING.index(facing) 
            
    print(f"r={row+1}, c={col+1}, f={f}")
    return (row+1) * 1000 + (col+1) * 4 + f 


if __name__=='__main__':
    example_ans = solvea(example)
    print(f'example:\n {example_ans}')

    actual_ans = solvea(actual)
    print(f'actual:\n {actual_ans}')

    example_ans = solveb(example, size=4)
    print(f'example:\n {example_ans}')

    actual_ans = solveb(actual, size=50)
    print(f'actual:\n {actual_ans}')
