from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace
from functools import cache


example = r"""
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
"""


with open('day13.txt', 'r') as f:
    actual = f.read() 


from dataclasses import dataclass

@dataclass(frozen=True)
class Machine:
    a_button: tuple
    b_button: tuple
    prize: tuple


import sys

cache = dict()

def compute_min_tokens(x, y, machine):
    if (x, y) == machine.prize:
        return 0
    if (x, y, machine) in cache:
        return cache[(x, y, machine)]
    ax, ay = x + machine.a_button[0], y + machine.a_button[1]
    bx, by = x + machine.b_button[0], y + machine.b_button[1]

    cost = sys.maxsize
    if ax <= machine.prize[0] and ay <= machine.prize[1]:
        cost = min(cost, 3 + compute_min_tokens(ax, ay, machine))
    if bx <= machine.prize[0] and by <= machine.prize[1]:
        cost = min(cost, 1 + compute_min_tokens(bx, by, machine))
    cache[(x, y, machine)] = cost
    return cost


def solve1(inp):
    inp = inp.strip().split('\n\n')
    machines = []
    for group in inp:
        lines = group.split('\n')
        a = lines[0].split(': ')[1].split(', ')
        ax = int(a[0].split('+')[1])
        ay = int(a[1].split('+')[1])
        b = lines[1].split(': ')[1].split(', ')
        bx = int(b[0].split('+')[1])
        by = int(b[1].split('+')[1])
        p = lines[2].split(': ')[1].split(', ')
        px = int(p[0].split("=")[1])
        py = int(p[1].split("=")[1])
        machines.append(Machine(a_button=(ax,ay), b_button=(bx, by), prize=(px,py)))

    total = 0
    for machine in machines:
        cost = compute_min_tokens(0, 0, machine)
        if cost <= 500:
            total += cost
    return total


def compute_min_tokensb(machine):
    ax, ay = machine.a_button
    bx, by = machine.b_button
    px, py = machine.prize

    nb = (px*ay - py*ax) / (ay*bx - by*ax)
    na = (px*by - py*bx) / (by*ax - bx*ay)

    if int(nb) == nb and int(na) == na:
        return 3 * na + nb
    return -1


def solve2(inp):
    inp = inp.strip().split('\n\n')
    machines = []
    for group in inp:
        lines = group.split('\n')
        a = lines[0].split(': ')[1].split(', ')
        ax = int(a[0].split('+')[1])
        ay = int(a[1].split('+')[1])
        b = lines[1].split(': ')[1].split(', ')
        bx = int(b[0].split('+')[1])
        by = int(b[1].split('+')[1])
        p = lines[2].split(': ')[1].split(', ')
        px = int(p[0].split("=")[1]) + 10000000000000 
        py = int(p[1].split("=")[1]) + 10000000000000
        machines.append(Machine(a_button=(ax,ay), b_button=(bx, by), prize=(px,py)))

    total = 0
    for machine in machines:
        cost = compute_min_tokensb(machine)
        if cost != -1:
            total += cost
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

