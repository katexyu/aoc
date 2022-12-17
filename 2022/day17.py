from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

actual = parse_lines('day17.txt')[0] 


rocks = [
    ["@@@@"],
    [" @ ", "@@@", " @ "],
    ["@@@", "  @", "  @"],
    ["@", "@", "@", "@"],
    ["@@", "@@"]
]


def solvea(inp, target=2022):
    grid = [['.'] * 7 for i in range(target*4)]
    steps, jet_steps, cnt, num_blocked = 0, 0, 0, 0
    highest = len(grid) - 1
    new_rock = True
    rock = rocks[cnt % 5]
    x, y = 2, highest - 3
    while num_blocked < target:
        if new_rock:
            rock = rocks[cnt % 5]
            x, y = 2, highest - 3
            draw_rock(grid, rock, x, y)
            new_rock = False
            steps = 0
        elif steps % 2 == 0:
            jet_dir = inp[jet_steps % len(inp)]
            jet_steps += 1
            left = jet_dir == '<'
            if not is_blocked_sideways(left, grid, x, y, rock):
                move_rock(left, grid, x, y, rock)
                delta = -1 if left else 1
                x += delta
            steps += 1
        else:
            blocked, new_highest = move_rock_down(grid, x, y, rock, highest)
            if blocked:
                highest = new_highest
                num_blocked += 1
                new_rock = True
                cnt += 1
            else:
                y += 1
                steps += 1
    
    return len(grid) - highest - 1 


def solveb(inp, target=1000000000000):
    grid = [['.'] * 7 for i in range(10000)]
    steps, jet_steps, cnt, num_blocked = 0, 0, 0, 0
    highest = len(grid) - 1
    new_rock = True
    rock = rocks[cnt % 5]
    x, y = 2, highest - 3
    cache = defaultdict(list)
    
    while num_blocked < target:
        if new_rock:
            rock = rocks[cnt % 5]
            x, y = 2, highest - 3
            draw_rock(grid, rock, x, y)
            new_rock = False
            steps = 0
        elif steps % 2 == 0:
            jet_dir = inp[jet_steps % len(inp)]
            jet_steps += 1
            left = jet_dir == '<'
            if not is_blocked_sideways(left, grid, x, y, rock):
                move_rock(left, grid, x, y, rock)
                delta = -1 if left else 1
                x += delta
            steps += 1
        else:
            blocked, new_highest = move_rock_down(grid, x, y, rock, highest)
            if blocked:
                top_rows = serialized_top_rows(grid, new_highest)
                cnt += 1
                key = (top_rows, jet_steps % len(inp), cnt % 5)
                cache[key].append((cnt, len(grid) - new_highest - 1))
                if len(cache[key]) > 1:
                    c2, h2 = cache[key][-1]
                    c1, h1 = cache[key][-2]
                    period = c2 - c1
                    # This is the right alignment from the end
                    if (target - c1) % period == 0:
                        diff = h2 - h1
                        print(f"Found a match ({c2, h2}), ({c1, h1})")
                        print(f"Returning ({target} - {c1}) / {period} * {diff} + {h1}")
                        return ((target - c1) / period) * diff + h1
                highest = new_highest
                num_blocked += 1
                new_rock = True
            else:
                y += 1
                steps += 1
    return
    
  

def serialized_top_rows(grid, highest):
    output = []
    for i in range(min(40, len(grid) - highest - 1)):
        output.append(''.join(grid[highest+i]))
    return ''.join(output)


def print_grid(grid):
    for row in grid:
        print(''.join(row))


def draw_rock(grid, rock, x, y):
    left = x
    bottom = y
    for i, row in enumerate(rock):
        for j, char in enumerate(row):
            grid[bottom-i][left+j] = char
    return


def is_blocked_down(grid, x, y, rock):
    bottom = y
    left = x
    if y == len(grid) - 1:
        return True

    for i, row in enumerate(rock):
        for j, char in enumerate(row):
            ypos, xpos = bottom-i, left+j
            if char == '@':
                if grid[ypos+1][xpos] == '#':
                    return True 
    return False


def move_rock_down(grid, x, y, rock, highest):
    blocked = is_blocked_down(grid, x, y, rock)
    if blocked:
        new_highest = convert_rock(grid, x, y, rock)
        return True, min(new_highest, highest)
    for i, row in enumerate(rock):
        for j, char in enumerate(row):
            ypos, xpos = y-i, x+j
            if char == '@':
                grid[ypos+1][xpos] = '@'
                grid[ypos][xpos] = '.'
    return False, highest


def convert_rock(grid, x, y, rock):
    for i, row in enumerate(rock):
        for j, char in enumerate(row):
            if char == '@':
                grid[y-i][x+j] = '#'
    return y - len(rock)


def move_rock(left, grid, x, y, rock):
    delta = -1 if left else 1
    for i, row in enumerate(rock):
        for j, char in enumerate(row): 
            ypos, xpos = y-i, x+j
            if char == '@':
                grid[ypos][xpos] = '.'
    for i, row in enumerate(rock):
        for j, char in enumerate(row): 
            ypos, xpos = y-i, x+j
            if char == '@':
                grid[ypos][xpos+delta] = '@'


def is_blocked_sideways(left, grid, x, y, rock):
    delta = -1 if left else 1
    if left and x == 0:
        return True
    elif not left and x + len(rock[0]) == 7:
        return True

    for i, row in enumerate(rock):
        for j, char in enumerate(row): 
            ypos, xpos = y-i, x+j
            if char == '@' and grid[ypos][xpos+delta] == '#':
                return True

    return False

 
if __name__=='__main__':
    example_ans = solvea(example)
    print(f'example:\n {example_ans}')

    actual_ans = solvea(actual)
    print(f'actual:\n {actual_ans}')

    example_ans = solveb(example)
    print(f'example:\n {example_ans}')

    actual_ans = solveb(actual)
    print(f'actual:\n {actual_ans}')


