from helpers import *
from collections import *
from itertools import *
from math import *
from heapq import heappush, heappop, heappushpop, heapify, heapreplace



def solve(x_range, y_range):
    x, y = 0, 0
    best = 0
    for vxi in range(0, x_range[1]+1):
        for vyi in range(y_range[0], abs(y_range[0])):
            vx, vy = vxi, vyi
            x, y = 0, 0
            max_y = 0
            in_target = False
            while x <= x_range[1] and y >= min(y_range[0], y_range[1]):
                x += vx
                y += vy
                if in_range(x_range, y_range, x, y):
                    in_target = True
                max_y = max(max_y, y)
                if vx > 0:
                    vx -= 1
                elif vx < 0:
                    vx += 1
                vy -= 1
            if in_target:
                best = max(best, max_y)
    return best


def solveb(x_range, y_range):
    x, y = 0, 0
    count = 0
    for vxi in range(0, x_range[1]+1):
        for vyi in range(y_range[0], abs(y_range[0])):
            vx, vy = vxi, vyi
            x, y = 0, 0
            while x <= x_range[1] and y >= min(y_range[0], y_range[1]):
                x += vx
                y += vy
                if in_range(x_range, y_range, x, y):
                    count += 1
                    break
                if vx > 0:
                    vx -= 1
                elif vx < 0:
                    vx += 1
                vy -= 1
    return count 


def in_range(x_range, y_range, x, y):
    return x >= x_range[0] and x <= x_range[1] and y >= y_range[0] and y <= y_range[1]


if __name__=='__main__':
    example_ans = solve([20, 30], [-10, -5])
    print(f'example:\n {example_ans}')

    actual_ans = solve([48, 70], [-189, -148])
    print(f'actual:\n {actual_ans}')

    example_ansb = solveb([20, 30], [-10, -5])
    print(f'example:\n {example_ansb}')

    actual_ansb = solveb([48, 70], [-189, -148])
    print(f'actual:\n {actual_ansb}')

