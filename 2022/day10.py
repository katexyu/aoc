from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


def solvea(filename):
    inp = parse_lines(filename)
    x = 1
    cycle = 1
    cycles = [20, 60, 100, 140, 180, 220]
    s = 0
    for cmd in inp:
        tokens = cmd.split(" ")
        if tokens[0] == 'noop':
            cycle += 1
            s += signal_strength(cycles, cycle, x)
        elif tokens[0] == 'addx':
            cycle += 1
            s += signal_strength(cycles, cycle, x)
            cycle += 1
            x += int(tokens[1])
            s += signal_strength(cycles, cycle, x)
    return s


def signal_strength(cycles, cycle, x):
    if cycle in cycles:
        return x * cycle
    return 0


def solve(filename):
    inp = parse_lines(filename)
    x = 0
    cycle = 0
    rows = [['.' for i in range(40)] for j in range(6)]
    for cmd in inp:
        tokens = cmd.split(" ")
        if tokens[0] == 'noop':
            draw(cycle, x, rows)
            cycle += 1
        elif tokens[0] == 'addx':
            draw(cycle, x, rows)
            cycle += 1
            x += int(tokens[1])
            draw(cycle, x, rows)
            cycle += 1
    for row in rows:
        print(''.join(row))
    return


def draw(cycle, x, rows):
    current = cycle % 40
    row = cycle // 40

    if abs(x-current) <= 1:
        rows[row][current] = '#'
    return
    

if __name__=='__main__':
    example_ansa = solvea('example10.txt')
    print(f'Part 1 example:\n {example_ansa}')

    actual_ansa = solvea('day10.txt')
    print(f'Part 1 actual:\n {actual_ansa}')

    print("Part 2 example:")
    example_ans = solve('example10.txt')

    print("Part 2 actual:")
    actual_ans = solve('day10.txt')

