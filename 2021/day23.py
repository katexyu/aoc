from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache
import json
import sys


example = """
#############
#...........#
###B#C#B#D###
  #D#C#B#A#
  #D#B#A#C#
  #A#D#C#A#
  #########
"""


actual = """
#############
#...........#
###C#A#B#C###
  #D#C#B#A#
  #D#B#A#C#
  #D#D#B#A#
  #########
"""

ENERGY = {
    'A': 1,
    'B': 10,
    'C': 100,
    'D': 1000
}


POSITIONS = {
    'A': 3,
    'B': 5,
    'C': 7,
    'D': 9
}

WAITING_AREAS = {(1,x) for x in [1,2,4,6,8,10,11]}

INVALID_SPOTS = {(1,3), (1,5), (1,7), (1,9)}

def copy_state(state):
    """
    Much faster than deepcopy
    """
    return [row[:] for row in state]


def solve(inp):
    inp = inp.strip().split('\n')
    inp = list(map(list, inp))
    print_state(inp)
    visited = set()
    
    q = [(0, state_from_arr(inp))]

    best_cost = dict()

    valid_spots = [w for w in WAITING_AREAS] + [(r,c) for r in [2,3,4,5] for c in [3,5,7,9]]
    while q:
        cost, s = heappop(q)
        state = to_arr(s)
        if is_organized(state):
            return cost

        # Else add possible next steps:
        for (row, col) in valid_spots:
            v = state[row][col]
            if v == '.':
                continue
            if POSITIONS[v] == col and is_done(state, row, col): 
                continue
            if state[row-1][col] in POSITIONS:
                # This amphipod is blocked
                continue
            pos_steps = all_steps(state, row, col, cost)
            for new_cost, steps in pos_steps:
                new_state = copy_state(state)
                new_state[row][col] = '.'
                new_state[steps[0]][steps[1]] = v
                key = state_from_arr(new_state)
                if key not in best_cost or best_cost[key] > new_cost: 
                    heappush(q, (new_cost, state_from_arr(new_state)))
                    best_cost[key] = new_cost

    return -1


def print_state(state):
    s ='\n'.join(''.join(x for x in s) for s in state)
    print(f'State:\n{s}\n')


def state_from_arr(arr):
    return tuple(tuple(r) for r in arr)


def to_arr(s):
    return list(list(r) for r in s)


def all_steps(state, row, col, cost):
    val = state[row][col]
    steps = []
    waiting = (row, col) in WAITING_AREAS
     
    q = deque(valid_neighbors(state, row, col, 1))
    visited = {(row, col)}
    for r, c, ns in q:
        visited.add((r,c))
    while q:
        r, c, num_steps = q.popleft()
        if c < len(state[r]):
            new_cost = cost + num_steps * ENERGY[val]
            if r >=2 and POSITIONS[val] == c and len(room_occupants(state, c) - {val}) == 0 and '.' not in below_occupants(state, r, c):
                steps.append((new_cost, (r,c)))
            elif not waiting and r == 1 and (r,c) not in INVALID_SPOTS:
                steps.append((new_cost, (r,c)))
                
            neighbors = valid_neighbors(state, r, c, num_steps + 1)
            for nr, nc, ns in neighbors:
                if (nr, nc) not in visited:
                    q.append((nr, nc, ns))
                    visited.add((nr, nc))
    return steps


def room_occupants(state, col):
    return {state[2][col], state[3][col], state[4][col], state[5][col]} - {'.'}


def is_done(state, row, col):
    val = state[row][col]
    if not POSITIONS[val] == col:
        return False
    for i in range(row, 6):
        if state[i][col] != val:
            return False
    return True

    
def below_occupants(state, row, col):
    o = set()
    for i in range(row+1, 6):
        o.add(state[i][col])
    return o


def valid_neighbors(state, row, col, num_steps):
    valid = []
    if row > 0 and state[row-1][col] == '.':
        valid.append((row-1, col, num_steps))
    if row < len(state)-1 and state[row+1][col] == '.':
        valid.append((row+1, col, num_steps))
    if col > 0 and state[row][col-1] == '.':
        valid.append((row, col-1, num_steps))
    if col < len(state[0])-1 and state[row][col+1] == '.':
        valid.append((row, col+1, num_steps))
    return valid


def row_is_organized(row):
    return row[3] == 'A' and row[5] == 'B' and row[7] == 'C' and row[9] == 'D'


def is_organized(m):
    return all(row_is_organized(m[x]) for x in [2,3,4,5])


def test_is_organized():
    m1 = """
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #A#B#C#D#
  #A#D#C#A#
  #########
    """
    assert not is_organized(m1.strip().split('\n'))
    m2 = """
#############
#...........#
###A#B#C#D###
  #A#B#C#D#
  #A#B#C#D#
  #A#B#C#D#
  #########
    """

    assert is_organized(m2.strip().split('\n'))


if __name__=='__main__':
    test_is_organized()
    example_ans = solve(example)
    print(f'example:\n {example_ans}')

    actual_ans = solve(actual)
    print(f'actual:\n {actual_ans}')

