from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import lru_cache


example = r"""
029A
179A
980A
456A
379A
"""

actual = r"""
208A
586A
341A
463A
593A
"""

BUTTONS = r"""
789
456
123
 0A
"""

DPAD = r"""
 ^A
<v>
"""

DIRS = {
    (0, 1): 'v',
    (0, -1): '^',
    (1, 0): '>',
    (-1, 0): '<'
}

sign = lambda x: copysign(1, x)


def compute_complexity(code, shortest):
    return int(code[:3]) * shortest


def compute_shortest_paths(mapping):
    shortest_paths = defaultdict(list)

    for x1, y1 in mapping:
        for x2, y2 in mapping:
            v1, v2 = mapping[(x1,y1)], mapping[(x2, y2)]
            if (v1 == ' ') or (v2 == ' '):
                continue
            dx, dy = x2-x1, y2-y1
            h_seq = ''
            v_seq = ''
            d = DIRS[(0, sign(dy))]
            for i in range(abs(dy)):
                v_seq += d
            d = DIRS[(sign(dx), 0)]
            for i in range(abs(dx)):
                h_seq += d
            valid_sequences = set()
            if mapping[(x1 + dx, y1)] != ' ':
                valid_sequences.add(h_seq + v_seq + 'A')
            if mapping[(x1, y1 + dy)] != ' ':
                valid_sequences.add(v_seq + h_seq + 'A')
            shortest_paths[(v1, v2)] = list(valid_sequences)
    return shortest_paths


import sys


def shortest_button_presses(code, dpad_shortest_paths, buttons_shortest_paths, num_robots=25):
    seq = 'A' + code
    shortest_presses = ['']
    for c1, c2 in zip(seq[:-1], seq[1:]):
        new = []
        for prefix in shortest_presses:
            possible = buttons_shortest_paths[(c1, c2)]
            for p in possible:
                new.append(prefix + p)
        shortest_presses = new

    @lru_cache
    def compute_recursive(dpad_sequence, depth):
        cost = 0
        seq = 'A' + dpad_sequence
        for c1, c2 in zip(seq[:-1], seq[1:]):
            best = sys.maxsize
            for path in dpad_shortest_paths[(c1, c2)]:
                if depth == 0:
                    best = min(best, len(path))
                else:
                    best = min(best, compute_recursive(path, depth-1))
            cost += best

        return cost

    best = sys.maxsize
    for candidate in shortest_presses:
        cost = compute_recursive(candidate, num_robots-1)
        best = min(best, cost)

    return best

     
def solve1(inp):
    inp = inp.strip().split('\n')
    dpad = to_grid_map(DPAD.split('\n'))
    buttons = to_grid_map(BUTTONS.split('\n'))

    dpad_shortest_paths = compute_shortest_paths(dpad)
    buttons_shortest_paths = compute_shortest_paths(buttons)

    total = 0
    for code in inp:
        shortest = shortest_button_presses(code, dpad_shortest_paths, buttons_shortest_paths, num_robots=2)
        total += compute_complexity(code, shortest)

    return total


def solve2(inp):
    inp = inp.strip().split('\n')
    dpad = to_grid_map(DPAD.split('\n'))
    buttons = to_grid_map(BUTTONS.split('\n'))

    dpad_shortest_paths = compute_shortest_paths(dpad)
    buttons_shortest_paths = compute_shortest_paths(buttons)

    total = 0
    for code in inp:
        shortest = shortest_button_presses(code, dpad_shortest_paths, buttons_shortest_paths, num_robots=25)
        total += compute_complexity(code, shortest)

    return total


if __name__=='__main__':
    example_ans = solve1(example)
    print(f'example 1:\n {example_ans}')

    actual_ans = solve1(actual)
    print(f'actual 1:\n {actual_ans}')

    example_ans = solve2(example)
    print(f'example 2:\n {example_ans}')

    actual_ans = solve2(actual)
    print(f'actual 2:\n {actual_ans}')

