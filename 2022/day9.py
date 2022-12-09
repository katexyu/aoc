from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


def solvea(filename):
    inp = parse_lines(filename)
    steps = []
    for l in inp:
        tokens = l.split(" ")
        steps.append((tokens[0], int(tokens[1])))

    head = (0, 0)
    tail = (0, 0)

    visited = set()

    for d, s in steps:
        cnt = s
        new_visited = set()
        if d == 'L':
            while cnt > 0:
                head = (head[0], head[1]-1)
                tail = new_move(head, tail)
                visited.add(tail)
                cnt -= 1
        elif d == 'R':
            while cnt > 0:
                head = (head[0], head[1]+1)
                tail = new_move(head, tail)
                visited.add(tail)
                cnt -= 1
        elif d == 'D':
            while cnt > 0:
                head = (head[0]-1, head[1])
                tail = new_move(head, tail)
                visited.add(tail)
                cnt -= 1
        elif d == 'U':
            while cnt > 0:
                head = (head[0]+1, head[1])
                tail = new_move(head, tail)
                visited.add(tail)
                cnt -= 1
    ans = len(visited)
    return ans 


def solve(filename):
    inp = parse_lines(filename)
    steps = []
    for l in inp:
        tokens = l.split(" ")
        steps.append((tokens[0], int(tokens[1])))

    visited = set()
    knots = [(0, 0) for x in range(10)]

    for d, s in steps:
        cnt = s
        if d == 'L':
            while cnt > 0:
                knots[0] = (knots[0][0], knots[0][1] - 1)
                for i in range(1, 10):
                    k = knots[i]
                    new = new_move(knots[i-1], knots[i])
                    knots[i] = new

                visited.add(knots[9])
                cnt -= 1
        elif d == 'R':
            while cnt > 0:
                knots[0] = (knots[0][0], knots[0][1] + 1)
                for i in range(1, 10):
                    k = knots[i]
                    new = new_move(knots[i-1], knots[i])
                    knots[i] = new
                visited.add(knots[9])
                cnt -= 1
        elif d == 'D':
            while cnt > 0:
                knots[0] = (knots[0][0]-1, knots[0][1])
                for i in range(1, 10):
                    k = knots[i]
                    new = new_move(knots[i-1], knots[i])
                    knots[i] = new
                visited.add(knots[9])
                cnt -= 1
        elif d == 'U':
            while cnt > 0:
                knots[0] = (knots[0][0]+1, knots[0][1])
                for i in range(1, 10):
                    k = knots[i]
                    new = new_move(knots[i-1], knots[i])
                    knots[i] = new
                visited.add(knots[9])
                cnt -= 1
    ans = len(visited)
    return ans 


def new_move(head, tail):
    if head[0] == tail[0]:
        if abs(head[1] - tail[1]) <= 1:
            return tail
        else:
            return (tail[0], copysign(1, head[1] - tail[1]) + tail[1])
    elif head[1] == tail[1]:
        if abs(head[0] - tail[0]) <= 1:
            return tail
        else:
            return (copysign(1, head[0] - tail[0]) + tail[0], tail[1])

    # diagonal
    if abs(head[1] - tail[1]) <= 1 and abs(head[0] - tail[0]) <= 1:
        return tail
    return (tail[0] + copysign(1, head[0]-tail[0]), tail[1] + copysign(1, head[1]-tail[1]))


if __name__=='__main__':
    example_ans = solve('example9.txt')
    print(f'example:\n {example_ans}')

    actual_ans = solve('day9.txt')
    print(f'actual:\n {actual_ans}')

