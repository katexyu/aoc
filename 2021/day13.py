from helpers import *
from collections import defaultdict


def solve(coords, instructions):
    for axis, val in instructions:
        new_coords = transform_coords(coords, axis, val)
        print(len(new_coords))
        break


def solveb(coords, instructions):
    new_coords = coords
    for axis, val in instructions:
        new_coords = transform_coords(new_coords, axis, val)
    print_coords(new_coords)    


def print_coords(coords):
    maxx = max(x for (x, y) in coords) + 1
    maxy = max(y for (x, y) in coords) + 1
    grid = []
    for i in range(maxy):
        row = []
        for j in range(maxx):
            row.append('.')
        grid.append(row)

    for x, y in coords:
        grid[y][x] = '#'

    print(printg(grid))


def printg(grid):
    rows = [''.join(r) for r in grid]
    return '\n'.join(rows)


def transform_coords(coords, axis, val):
    new_coords = set()
    for x, y in coords:
       if axis == 'x':
         if x < val:
            new_coords.add((x,y))
         elif x > val:
            diff = x - val
            new_coords.add((val-diff, y))
       elif axis == 'y':
         if y < val:
            new_coords.add((x, y))
         elif y > val:
            diff = y - val
            new_coords.add((x, val - diff))
    return new_coords


def get_data(filename='day13.txt'):
    ins_start = 0
    lines = parse_lines(filename)
    coordinates = []
    for i, l in enumerate(lines):
        if len(l) == 0:
            ins_start = i+1
            break 
        parts = l.split(',')
        coordinates.append((int(parts[0]), int(parts[1])))
    instructions = []
    for l in lines[ins_start:len(lines)]:
        parts = l.split(' ')
        last = parts[-1]
        last_parts = last.split('=')
        instructions.append((last_parts[0], int(last_parts[1])))
    return coordinates, instructions


if __name__=='__main__':
    coords, ins= get_data('day13.txt')
    solve(coords, ins)

    coords, ins = get_data('day13.txt')
    solveb(coords, ins)

