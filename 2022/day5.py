from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

actual = """
[P]     [C]         [M]            
[D]     [P] [B]     [V] [S]        
[Q] [V] [R] [V]     [G] [B]        
[R] [W] [G] [J]     [T] [M]     [V]
[V] [Q] [Q] [F] [C] [N] [V]     [W]
[B] [Z] [Z] [H] [L] [P] [L] [J] [N]
[H] [D] [L] [D] [W] [R] [R] [P] [C]
[F] [L] [H] [R] [Z] [J] [J] [D] [D]
 1   2   3   4   5   6   7   8   9 

move 4 from 9 to 1
move 6 from 3 to 1
move 7 from 4 to 1
move 2 from 8 to 5
move 1 from 9 to 7
move 1 from 8 to 5
move 3 from 6 to 4
move 6 from 1 to 5
move 14 from 1 to 2
move 1 from 6 to 1
move 2 from 6 to 2
move 9 from 5 to 9
move 2 from 4 to 5
move 2 from 5 to 3
move 6 from 9 to 6
move 4 from 1 to 2
move 2 from 1 to 2
move 5 from 6 to 1
move 1 from 4 to 9
move 4 from 9 to 4
move 2 from 3 to 7
move 2 from 4 to 9
move 2 from 9 to 6
move 5 from 2 to 9
move 1 from 4 to 9
move 1 from 4 to 3
move 5 from 9 to 8
move 1 from 6 to 5
move 3 from 7 to 5
move 2 from 1 to 6
move 5 from 6 to 8
move 1 from 9 to 4
move 1 from 6 to 5
move 9 from 2 to 7
move 1 from 2 to 3
move 1 from 4 to 6
move 8 from 5 to 4
move 1 from 6 to 1
move 2 from 8 to 6
move 1 from 6 to 4
move 7 from 4 to 6
move 1 from 3 to 1
move 1 from 3 to 4
move 3 from 4 to 1
move 2 from 3 to 4
move 2 from 4 to 5
move 3 from 5 to 7
move 7 from 8 to 2
move 5 from 1 to 2
move 12 from 7 to 6
move 2 from 1 to 9
move 2 from 9 to 1
move 1 from 7 to 5
move 6 from 2 to 3
move 5 from 2 to 6
move 6 from 2 to 6
move 4 from 3 to 1
move 3 from 2 to 1
move 1 from 5 to 4
move 7 from 1 to 2
move 1 from 4 to 8
move 7 from 2 to 9
move 5 from 2 to 8
move 2 from 6 to 8
move 21 from 6 to 9
move 8 from 9 to 1
move 2 from 6 to 1
move 3 from 8 to 7
move 6 from 6 to 4
move 7 from 1 to 8
move 1 from 9 to 1
move 7 from 7 to 3
move 1 from 7 to 4
move 1 from 7 to 4
move 7 from 8 to 1
move 5 from 4 to 8
move 10 from 1 to 2
move 3 from 1 to 4
move 3 from 2 to 9
move 1 from 4 to 5
move 3 from 3 to 6
move 1 from 6 to 4
move 1 from 6 to 7
move 1 from 7 to 8
move 7 from 2 to 4
move 10 from 9 to 1
move 10 from 4 to 5
move 2 from 5 to 2
move 2 from 2 to 1
move 11 from 8 to 9
move 7 from 1 to 4
move 1 from 6 to 1
move 1 from 8 to 3
move 1 from 4 to 6
move 6 from 4 to 5
move 1 from 5 to 7
move 1 from 6 to 8
move 6 from 1 to 6
move 19 from 9 to 2
move 1 from 1 to 8
move 1 from 4 to 7
move 9 from 2 to 6
move 1 from 9 to 2
move 2 from 8 to 1
move 1 from 1 to 9
move 7 from 3 to 6
move 3 from 9 to 2
move 5 from 2 to 6
move 1 from 9 to 3
move 15 from 6 to 7
move 6 from 6 to 7
move 1 from 1 to 9
move 5 from 6 to 2
move 1 from 6 to 1
move 6 from 5 to 8
move 1 from 3 to 4
move 1 from 9 to 7
move 6 from 8 to 1
move 3 from 4 to 6
move 1 from 6 to 1
move 3 from 5 to 2
move 1 from 5 to 7
move 5 from 1 to 5
move 2 from 6 to 9
move 2 from 9 to 2
move 7 from 5 to 1
move 1 from 5 to 7
move 1 from 5 to 9
move 20 from 7 to 1
move 23 from 1 to 7
move 1 from 1 to 2
move 4 from 7 to 9
move 4 from 9 to 8
move 1 from 9 to 2
move 16 from 7 to 6
move 4 from 1 to 5
move 9 from 7 to 6
move 11 from 2 to 6
move 1 from 1 to 9
move 1 from 1 to 7
move 1 from 8 to 2
move 1 from 9 to 7
move 4 from 5 to 2
move 3 from 8 to 3
move 2 from 2 to 4
move 2 from 7 to 4
move 4 from 4 to 9
move 28 from 6 to 9
move 5 from 2 to 7
move 8 from 6 to 5
move 6 from 2 to 6
move 2 from 7 to 3
move 5 from 5 to 7
move 1 from 5 to 9
move 14 from 9 to 4
move 18 from 9 to 8
move 5 from 6 to 4
move 6 from 7 to 8
move 1 from 2 to 6
move 19 from 4 to 7
move 1 from 2 to 5
move 1 from 9 to 3
move 2 from 5 to 2
move 14 from 7 to 3
move 1 from 5 to 3
move 12 from 8 to 6
move 6 from 6 to 5
move 4 from 5 to 4
move 21 from 3 to 4
move 10 from 8 to 3
move 2 from 3 to 2
move 7 from 4 to 6
move 2 from 8 to 1
move 2 from 2 to 3
move 5 from 7 to 2
move 2 from 1 to 4
move 3 from 3 to 7
move 2 from 5 to 7
move 2 from 2 to 7
move 2 from 2 to 3
move 7 from 4 to 1
move 3 from 1 to 4
move 3 from 2 to 5
move 2 from 1 to 5
move 7 from 4 to 3
move 15 from 6 to 2
move 1 from 1 to 4
move 1 from 5 to 1
move 14 from 3 to 1
move 9 from 4 to 1
move 5 from 7 to 1
move 1 from 3 to 5
move 1 from 4 to 2
move 20 from 1 to 2
move 17 from 2 to 5
move 1 from 3 to 7
move 5 from 7 to 3
move 6 from 5 to 1
move 3 from 3 to 2
move 10 from 1 to 9
move 3 from 5 to 6
move 12 from 5 to 6
move 1 from 5 to 1
move 15 from 6 to 5
move 13 from 5 to 3
move 1 from 5 to 1
move 10 from 3 to 2
move 3 from 3 to 2
move 1 from 5 to 3
move 2 from 3 to 6
move 1 from 3 to 4
move 2 from 6 to 4
move 3 from 4 to 2
move 8 from 9 to 4
move 8 from 4 to 8
move 7 from 2 to 1
move 5 from 8 to 7
move 2 from 2 to 3
move 13 from 1 to 2
move 2 from 3 to 8
move 2 from 9 to 7
move 3 from 8 to 1
move 2 from 1 to 2
move 2 from 8 to 4
move 6 from 7 to 2
move 3 from 1 to 8
move 1 from 7 to 5
move 24 from 2 to 1
move 2 from 8 to 5
move 15 from 1 to 4
move 1 from 5 to 8
move 9 from 1 to 4
move 2 from 8 to 5
move 26 from 2 to 4
move 1 from 5 to 8
move 1 from 5 to 8
move 50 from 4 to 1
move 1 from 8 to 9
move 1 from 4 to 6
move 1 from 4 to 9
move 22 from 1 to 5
move 1 from 6 to 2
move 1 from 5 to 8
move 1 from 2 to 4
move 1 from 8 to 1
move 28 from 1 to 3
move 2 from 9 to 4
move 21 from 5 to 8
move 1 from 1 to 8
move 1 from 5 to 8
move 1 from 5 to 7
move 3 from 4 to 8
move 1 from 7 to 9
move 1 from 9 to 7
move 20 from 8 to 4
move 2 from 8 to 1
move 1 from 7 to 6
move 2 from 1 to 4
move 27 from 3 to 1
move 4 from 8 to 4
move 1 from 6 to 9
move 19 from 4 to 2
move 5 from 2 to 5
move 1 from 4 to 1
move 1 from 9 to 2
move 17 from 1 to 9
move 1 from 3 to 8
move 15 from 9 to 2
move 2 from 4 to 8
move 2 from 5 to 8
move 2 from 5 to 9
move 3 from 9 to 8
move 9 from 1 to 2
move 2 from 1 to 3
move 4 from 4 to 5
move 2 from 5 to 7
move 1 from 8 to 5
move 2 from 3 to 8
move 4 from 5 to 2
move 1 from 9 to 6
move 5 from 8 to 5
move 1 from 7 to 9
move 29 from 2 to 3
move 1 from 8 to 6
move 1 from 9 to 7
move 2 from 2 to 8
move 2 from 5 to 2
move 2 from 7 to 5
move 4 from 5 to 9
move 1 from 5 to 9
move 10 from 3 to 4
move 10 from 4 to 7
move 1 from 3 to 4
move 5 from 2 to 9
move 5 from 8 to 6
move 1 from 6 to 5
move 2 from 6 to 3
move 4 from 6 to 7
move 1 from 5 to 2
move 2 from 2 to 7
move 5 from 7 to 8
move 8 from 7 to 2
move 6 from 8 to 7
move 14 from 2 to 5
move 3 from 7 to 3
move 1 from 4 to 7
move 2 from 7 to 2
move 3 from 2 to 8
move 3 from 8 to 5
move 8 from 9 to 1
move 3 from 7 to 2
move 2 from 7 to 4
move 17 from 3 to 6
move 8 from 1 to 6
move 16 from 5 to 2
move 1 from 5 to 2
move 1 from 3 to 1
move 21 from 6 to 7
move 1 from 4 to 8
move 7 from 7 to 8
move 1 from 1 to 3
move 11 from 7 to 2
move 7 from 2 to 6
move 8 from 8 to 5
move 2 from 7 to 4
move 4 from 5 to 6
move 8 from 2 to 8
move 17 from 2 to 3
move 4 from 5 to 3
move 7 from 6 to 9
move 2 from 6 to 9
move 1 from 4 to 1
move 1 from 4 to 2
move 3 from 6 to 2
move 1 from 6 to 8
move 1 from 4 to 1
move 1 from 7 to 5
move 10 from 9 to 2
move 1 from 5 to 6
move 1 from 8 to 2
move 1 from 1 to 4
move 12 from 3 to 4
move 1 from 6 to 2
move 2 from 8 to 6
move 1 from 1 to 2
move 1 from 9 to 8
move 2 from 8 to 7
move 6 from 3 to 2
move 1 from 3 to 5
move 8 from 4 to 9
move 22 from 2 to 9
move 7 from 3 to 5
move 3 from 8 to 2
move 2 from 7 to 8
move 3 from 6 to 9
move 1 from 2 to 9
move 1 from 6 to 2
move 4 from 8 to 5
move 5 from 5 to 9
move 1 from 3 to 6
move 1 from 5 to 6
move 2 from 4 to 1
move 2 from 2 to 4
move 4 from 4 to 6
move 1 from 1 to 5
move 5 from 6 to 3
move 35 from 9 to 1
move 4 from 9 to 1
move 1 from 4 to 7
move 3 from 3 to 7
move 37 from 1 to 7
move 2 from 2 to 3
move 3 from 3 to 7
move 1 from 5 to 8
move 2 from 1 to 8
move 2 from 5 to 2
move 1 from 6 to 9
move 16 from 7 to 1
move 5 from 1 to 5
move 3 from 8 to 2
move 10 from 7 to 9
move 6 from 7 to 9
move 3 from 2 to 1
move 4 from 5 to 3
move 2 from 1 to 2
move 5 from 7 to 9
move 5 from 7 to 9
move 5 from 5 to 3
move 8 from 3 to 7
move 6 from 9 to 4
move 8 from 7 to 3
move 2 from 3 to 6
move 1 from 6 to 7
move 1 from 6 to 7
move 5 from 4 to 9
move 3 from 7 to 1
move 2 from 2 to 8
move 1 from 8 to 6
move 6 from 1 to 8
move 1 from 7 to 9
move 1 from 3 to 9
move 4 from 3 to 2
move 8 from 1 to 6
move 1 from 3 to 9
move 5 from 8 to 4
move 2 from 3 to 1
move 1 from 8 to 2
move 4 from 9 to 1
move 2 from 1 to 5
move 1 from 8 to 5
move 11 from 9 to 5
move 1 from 2 to 8
move 10 from 5 to 4
move 1 from 1 to 9
move 3 from 5 to 4
move 5 from 2 to 3
move 1 from 5 to 1
move 9 from 9 to 4
move 1 from 6 to 7
move 1 from 3 to 9
move 4 from 3 to 1
move 1 from 2 to 4
move 1 from 1 to 4
move 1 from 4 to 7
move 5 from 1 to 3
move 1 from 3 to 2
move 1 from 8 to 3
move 3 from 9 to 5
move 1 from 2 to 9
move 4 from 1 to 4
move 1 from 7 to 4
move 2 from 5 to 8
move 1 from 7 to 6
move 4 from 3 to 1
move 1 from 5 to 8
move 1 from 3 to 4
move 22 from 4 to 1
move 11 from 1 to 9
move 2 from 1 to 4
move 11 from 1 to 6
move 8 from 6 to 7
move 1 from 8 to 7
move 7 from 9 to 2
move 6 from 7 to 6
move 2 from 4 to 9
move 2 from 7 to 1
move 14 from 6 to 3
move 2 from 3 to 1
move 3 from 6 to 7
move 6 from 1 to 3
move 8 from 9 to 6
move 7 from 4 to 6
move 7 from 6 to 8
move 1 from 9 to 1
move 2 from 9 to 8
move 4 from 3 to 4
move 1 from 8 to 4
move 1 from 4 to 3
move 6 from 3 to 7
move 7 from 2 to 5
move 8 from 4 to 6
move 1 from 7 to 2
move 1 from 5 to 7
move 6 from 7 to 3
move 1 from 7 to 1
move 8 from 8 to 4
move 8 from 4 to 2
move 3 from 7 to 3
move 6 from 5 to 6
move 15 from 3 to 1
move 21 from 6 to 1
move 4 from 2 to 6
move 5 from 6 to 5
move 1 from 2 to 6
move 1 from 4 to 5
move 1 from 4 to 3
move 1 from 8 to 6
move 4 from 5 to 7
move 18 from 1 to 4
move 2 from 5 to 7
move 6 from 7 to 6
move 1 from 3 to 2
move 6 from 1 to 2
move 3 from 3 to 9
move 3 from 9 to 4
move 1 from 8 to 3
move 1 from 6 to 5
move 6 from 2 to 5
move 1 from 5 to 9
move 1 from 3 to 5
move 2 from 6 to 8
move 2 from 1 to 4
move 5 from 4 to 6
move 15 from 4 to 9
move 5 from 9 to 1
move 2 from 6 to 2
move 6 from 6 to 3
move 1 from 8 to 6
move 6 from 5 to 9
move 3 from 6 to 5
move 2 from 4 to 7
"""

def parse_input(inp):
    crates = []
    parsed = False
    out = []
    num_columns = 0
    move_instructions = []
    for i in inp:
        if '1' not in i and not parsed and i:
            crates.append(i)
        elif 'move' not in i and i:
            col = list(map(int, i.strip().split('  ')))
            num_columns = max(col)
            parsed = True
        elif i:
            tokens = i.strip().split(' ')
            move_instructions.append((int(tokens[1]), int(tokens[3]), int(tokens[5])))
        
            
    return crates, num_columns, move_instructions


def parse_crates(crates, num_columns):
    h = len(crates)
    w = num_columns
    out = [
        ['' for x in range(w)]
        for y in range(h)
    ]

    for i, c in enumerate(crates):
        for j in range(num_columns):
            out[i][j] = c[4*j: 4*j+3].strip()
    
    flipped = []
    for x in range(w):
        col = []
        for y in range(h):
            if out[y][x] != '':
                col.append(out[y][x])
        col.reverse()
        flipped.append(col)

    return flipped


def solvea(inp):
    inp = inp.split('\n')
    crates, num_columns, moves = parse_input(inp)
    parsed = parse_crates(crates, num_columns)

    for num, from_c, to_c in moves:
        total = 0
        f_idx = from_c -1
        to_idx = to_c - 1
        while total < num:
            c = parsed[f_idx].pop()
            parsed[to_idx].append(c)
            total += 1 
    
    return get_top(parsed) 


def solve(inp):
    inp = inp.split('\n')
    crates, num_columns, moves = parse_input(inp)
    parsed = parse_crates(crates, num_columns)

    for num, from_c, to_c in moves:
        total = 0
        f_idx = from_c -1
        to_idx = to_c - 1

        to_add = []
        while total < num:
            c = parsed[f_idx].pop()
            to_add.append(c)
            total += 1
        for i in reversed(to_add):
            parsed[to_idx].append(i)
    
    return get_top(parsed) 


def get_top(crates):
    return ''.join([
        c[-1][1] for c in crates
    ])


if __name__=='__main__':
    example_ans = solve(example)
    print(f'example:\n {example_ans}')

    actual_ans = solve(actual)
    print(f'actual:\n {actual_ans}')

